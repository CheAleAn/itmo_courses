from datetime import datetime

from prettytable import PrettyTable

def prompt(msg, default=None, type_cast=None):
    while 1:
        if default is None:
            value = input(f'{msg}: ')
        else:
            value = input(f'{msg} (по умолчанию - {default}): ')

        if not value:
            return default

        if type_cast is None:
            return value

        try:
            return type_cast(value)
        except ValueError as err:
            print(err)


def input_int(msg='Введите число', default=None):
    return prompt(msg, default, int)


def input_number_of_things(msg='Введите число', default=1):
    return prompt(msg, default, int)


def input_float(msg='Введите сумму', default=None):
    return prompt(msg, default, float)


def input_datetime(msg='Введите дату', default=None, ftm='%Y-%m-%d'):
    return prompt(msg, default, lambda v: datetime.strptime(v, ftm))


def input_date(msg='Введите дату', default=None, ftm='%Y-%m-%d'):
    value = input_datetime(msg, default, ftm)

    # @fixme: скорее всего упадем если date
    if value is None:
        return default

    return value.date()


def print_table(headers, iterable):
    table = PrettyTable(headers)

    for row in iterable:
        table.add_row(row)

    print(table)
