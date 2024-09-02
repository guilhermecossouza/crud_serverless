from bd_connections.open_connection import open_connect
from mysql.connector.errors import ProgrammingError

def delete_table():
    with open_connect() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("DROP TABLE IF EXISTS TbUsuarios")
            return "Table excluida com sucasso.."
        except ProgrammingError as e:
            return f"Erro ao excluir tabela de usuarios: {e.msg}"
 
        
def create_table():    
    strSQL = """
            CREATE TABLE IF NOT EXISTS tbUsuario(
                IdUsuario INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                PRIMARY KEY (IdUsuario) 
            )
        """
    with open_connect() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(strSQL)
            return "Table criada com sucasso.."
        except ProgrammingError as e:
            return f"Erro ao excluir tabela de usuarios: {e.msg}"
        

def insert_user(nome, email) -> str:
    strSQL = "INSERT INTO tbUsuario(nome, email) VALUES(%s, %s)"
    parameters_sql = (nome, email)
    with open_connect() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(strSQL, parameters_sql)
            conexao.commit()
            return "Usuário inserido com sucesso."
        except ProgrammingError as e:
            return f"Erro: Não foi possível inserir usuário: {e.msg}"
    
    
def get_users():
    with open_connect() as conexao:
        main_dict = dict()
        main_list = list()   
        dict_error = dict()
        list_error = list()
        try:            
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM tbUsuario")
            users = cursor.fetchall() 
            dict_user = dict()
            list_user = list()
            for user in users:
                dict_user["Id"] = user[0]
                dict_user["nome"] = user[1]
                dict_user["email"] = user[2]
                list_user.append(dict_user.copy())
                dict_user.clear()
            main_dict["dadosUsuario"] = list_user.copy()
            list_user.clear()
            
            dict_error["error"] = False
            dict_error["message"] = ""
            list_error.append(dict_error.copy())
            main_dict["dadosError"] = list_error.copy()
            dict_error.clear()
            list_error.clear()
            
            main_list.append(main_dict.copy()) 
            main_dict.clear()
            return main_list
        except ProgrammingError as e:
            dict_error["error"] = True
            dict_error["message"] = f"Erro: Não foi possível buscal usuários. {e.msg}"
            list_error.append(dict_error.copy())
            main_dict["dadosError"] = list_error.copy()
            main_list.append(main_dict.copy()) 
            main_dict.clear()
            return main_list
 