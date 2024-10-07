from utils.connection import ConnectionDataBase
from mysql.connector import ProgrammingError

class UserModel(ConnectionDataBase):
    def __init__(self) -> None:
        super().__init__()
        self.nome = None
        self.email = None
        
    def get_nome(self):
        return self.nome

    def set_nome(self, nome) -> str:
        self.nome = nome
        
    def get_email(self):
        return self.email
    
    def set_email(self, email) -> str:
        self.email = email   
        
    def create(self):
        strSQL = "INSERT INTO TbUsuarios(nome, email) VALUES(%s, %s)"
        parametros = (self.nome, self.email)
        with self.open_connect() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(strSQL, parametros)
                conn.commit()                
            except ProgrammingError as e:
                self.connection_error = f"{str(e.msg)}"  
            except Exception as e:
                self.connection_error = f"{str(e)}"  
           
    
        
    
    
    