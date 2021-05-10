from datetime import datetime, timedelta, date
from textwrap import dedent
import sys

from . import helpers as h
from . import storage as s
from .services import make_connection


def input_payment(payment=None):
    payment = dict(payment) if payment is not None else {}
    data = {}
    data['title'] = h.prompt('Название', default=payment.get('title'))
    data['price'] = h.input_float('Цена за 1 шт', default=payment.get('price'))
    data['items_number'] = h.input_number_of_things(
    'Количество',
    default=payment.get('items_number') if payment.get('items_number') else 1,
    )
    data['total_price'] = data['price'] * data['items_number']
    data['buyedat'] = h.input_date(
    'Дата покупки',
    default=datetime.strptime(payment.get('buyedat'), "%Y-%m-%d") if payment.get('buyedat') else datetime.today()
    )             #payment.get('buyedat').strptime('%Y-%m-%d'))
    return data #++


def read_payment():
    payment_id = h.input_int('Введите ID платежа')

    with make_connection() as conn:
        payment = s.get_task(conn, payment_id)

        if payment is None:
            print(f'Платеж с {task_id} не найден')

        return payment


def add_payment(): #++
    data = input_payment()

    with make_connection() as conn:
        s.create_payment(conn, **data)

    print(f'''Платеж {data['title']} добавлен''')


def edit_payment():
    payment = read_payment()
    if payment is not None:
        data = input_payment(payment)

        with make_connection() as conn:
            s.update_payment(conn, payment['id'], **data)

        print(f'''Платеж "{payment['title']}" успешно отредактирован''') #++


def show_for_period():

    period_beginning = h.input_date('Введите начало периода (Пример: 2001-05-25):')
    period_ending = h.input_date('Введите конец периода:', default=datetime.today())
    print(period_ending, period_beginning)

    with make_connection() as conn:
        tasks = s.get_payments_per_date(conn, period_beginning, period_ending)
        #h.print_table(['id','tilte','price','number','total price','date'], tasks)

    h.print_table(['id','title','price','number','total price','date'], tasks)
    '''
    with make_connection() as conn:
        tasks = s.get_all_payments(conn)
    h.print_table(['id','title','price','number','total price','date'], tasks)
    ''' #++


def show_all_payments():
    with make_connection() as conn:
        all_payments = s.get_all_payments(conn)

    h.print_table(['id','title','price','number','total price','date'], all_payments) #++


def show_top():
    top_payment_number = h.input_int('Введите количество топ платежей')

    with make_connection() as conn:
        top_payments = s.get_top_payments(conn, top_payment_number)

    h.print_table(['id','title','price','number','total price','date'], top_payments) #++


def show_menu():
    print(dedent('''
    1. Добавить платеж
    2. Отредактировать платеж
    3. Вывести все платежи за указанный период
    4. Вывести все платежи
    5. Вывести топ самых крупных платежей
    6. Показать меню
    7. Закрыть программу
    ''')) #++


def close_program():
    print('Ещё увидимся!') #выполнение 6 пункта меню
    sys.exit(0) #++


commands_lst = {
'1': add_payment,
'2': edit_payment,
'3': show_for_period,
'4': show_all_payments,
'5': show_top,
'6': show_menu,
'7': close_program,
} #++


def main():
    with make_connection() as conn:
        s.initialize(conn, 'schema.sql')


    show_menu()

    while 1:
        menu_command = input('\nВведите команду: ').strip()
        command_lst = commands_lst.get(menu_command)

        if command_lst: #чтобы уточить есть ли такая функция
            command_lst()
        else:
            print('Вы ввели неверную команду')
