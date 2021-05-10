from configparser import ConfigParser
import sqlite3


def make_config(*config_files):
    config = ConfigParser()
    config.read(config_files)
    return config


config = make_config('config.ini')


def make_connection(name='db'):
    conn = sqlite3.connect(config.get(name, 'db_name'), detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row

    return conn
