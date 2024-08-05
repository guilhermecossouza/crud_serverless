from mysql.connector import connect
from contextlib import contextmanager

class ConnectionBdMysql:
    def __init__(self):
        self.connection = dict(
            host =  "db",
            database = "bdUsuarios",
            user = "root",
            password = "root"
        )
    
    @contextmanager    
    def open_connect(self):  
        conexao = connect(**self.connection)
        try:
            yield conexao
        finally:
            if conexao and conexao.is_connected:
                conexao.close()
            
        