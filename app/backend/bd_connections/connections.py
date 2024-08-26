from mysql.connector import connect
from mysql.connector import ProgrammingError
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
                
    def deleta_tabela(self):     
        message = ""  
        with self.open_connect() as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("DROP TABLE IF EXISTS TbUsuario")
                message = "Deletado"
            except ProgrammingError as e:
                message = f"Erro: {e.msg}" 
        return message
    
    def create_tabele(self):
        strSQL = """
            CREATE TABLE IF NOT EXISTS tbUsuario(
                IdUsuario INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                PRIMARY KEY (IdUsuario) 
            )
        """
        with self.open_connect() as conexao:
            message = ""
            try:
                cursor = conexao.cursor()
                cursor.execute(strSQL)
                message = "tabela creiada"
            except ProgrammingError as e:
                message = f"Erro: {e.msg}"
        return message
            
                
            
        

       