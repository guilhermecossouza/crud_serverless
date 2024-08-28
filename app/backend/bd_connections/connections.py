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
 