from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from contextlib import contextmanager

parameters = dict(
    host =  "db",
    database = "bdUsuarios",
    user = "root",
    password = "root"
)

@contextmanager
def open_connect():
    conn = connect(**parameters)
    try:
        yield conn
    except ProgrammingError as e:
        raise e.msg
    finally:
        if conn and conn.is_connected:
            conn.close()
