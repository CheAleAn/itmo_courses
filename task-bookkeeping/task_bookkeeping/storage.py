from datetime import timedelta, datetime, time

SQL_CREATE_NEW_PAYMENT = 'INSERT INTO book (title, price, items_number, total_price, buyedat) VALUES (?, ?, ?, ?, ?)'

SQL_UPDATE_PAYMENT = 'UPDATE book SET title=?, price=?, items_number=?, total_price=?, buyedat=? WHERE id=?'

SQL_SELECT_ALL_PAYMENTS = 'SELECT id, title, price, items_number, total_price, buyedat FROM book'

SQL_SELECT_PAYMENT_BY_PK = f'{SQL_SELECT_ALL_PAYMENTS} WHERE id=?'

SQL_SELECT_PAYMENT_PER_DATE = f'{SQL_SELECT_ALL_PAYMENTS} WHERE buyedat BETWEEN ? AND ?'

SQL_SELECT_PAYMENT_BY_TOTAL_PRICE = f'{SQL_SELECT_ALL_PAYMENTS} ORDER BY total_price DESC'


def initialize(conn, creation_schema):
    with open(creation_schema) as f:
        conn.executescript(f.read())


def create_payment(conn, title, price, items_number, total_price, buyedat):
    conn.execute(SQL_CREATE_NEW_PAYMENT, (title, price, items_number, total_price, buyedat))


def update_payment(conn, pk, title, price, items_number, total_price, buyedat):
    conn.execute(SQL_UPDATE_PAYMENT, (title, price, items_number, total_price, buyedat, pk))


def get_task(conn, pk):
    cursor = conn.execute(SQL_SELECT_PAYMENT_BY_PK, (pk,))
    return cursor.fetchone()


def get_all_payments(conn):
    return conn.execute(SQL_SELECT_ALL_PAYMENTS).fetchall()


def get_payments_per_date(conn, start_date, end_date):
    start = datetime.combine(start_date, time(0,0,0))
    end = datetime.combine(end_date, time(23,59,59))
    return conn.execute(SQL_SELECT_PAYMENT_PER_DATE, (start, end)).fetchall()


def get_top_payments(conn, number):
    return conn.execute(SQL_SELECT_PAYMENT_BY_TOTAL_PRICE).fetchmany(number)
