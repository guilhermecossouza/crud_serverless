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
           
    def get_dados_users(self, parameter):
        strWhere = ""
        if parameter != "":
            strWhere = f"WHERE nome like '%{parameter}%'"
                        
        strSQL = f"SELECT * FROM TbUsuarios {strWhere} ORDER BY nome;"
        with self.open_connect() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(strSQL)
                dados_users = cursor.fetchall()
            except ProgrammingError as e:
                self.connection_error = f"Erro: {str(e.msg)}"
            except Exception as e:
                self.connection_error = f"Erro: {str(e)}"
            else:
                dict_dados_bd = dict()
                list_dados_bd = list()
                
                for dado_user in dados_users:
                    dict_dados_bd["idUsuario"] = dado_user[0]
                    dict_dados_bd["nome"] = dado_user[1]
                    dict_dados_bd["email"] = dado_user[2]
                    list_dados_bd.append(dict_dados_bd.copy())
                    dict_dados_bd.clear()
                
                return list_dados_bd    
            
    def delete_user(self, parameter):
        strSQl = "DELETE FROM TbUsuarios WHERE id = %s"
        strWhere = (parameter,)
        with self.open_connect() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(strSQl, strWhere)
                conn.commit()
            except ProgrammingError as e:
                self.connection_error = f"Erro: {str(e.msg)}"
            except Exception as e:
                self.connection_error = f"Erro: {str(e)}"
            else:
                return "Usuário deletado com sucesso"
            
    def get_dados_user(self, parameter):
        strSQl = "SELECT * FROM TbUsuarios WHERE id = %s"
        strWhere = (parameter,)    
        with self.open_connect() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(strSQl, strWhere)
                dados_users = cursor.fetchall()
            except ProgrammingError as e:
                self.connection_error = f"Erro: {str(e.msg)}"
            except Exception as e:
                self.connection_error = f"Erro: {str(e)}"
            else:
                dict_dados_bd = dict()
                list_dados_bd = list()
                
                for dado_user in dados_users:
                    dict_dados_bd["idUsuario"] = dado_user[0]
                    dict_dados_bd["nome"] = dado_user[1]
                    dict_dados_bd["email"] = dado_user[2]
                    list_dados_bd.append(dict_dados_bd.copy())
                    dict_dados_bd.clear()
                
                return list_dados_bd 
            
    def update_data_user(self, parameter):
        strSQL = "UPDATE TbUsuarios SET nome = %s, email = %s WHERE Id = %s"
        data = (self.nome, self.email, parameter)
        with self.open_connect() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(strSQL, data)
                conn.commit()
            except ProgrammingError as e:
                self.connection_error = f"Erro: {str(e.msg)}"
            except Exception as e:
                self.connection_error = f"Erro: {str(e)}"
            else:
                return "Usuário alterado com sucesso."
        
                
        
    
    
    