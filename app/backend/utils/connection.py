import mysql.connector
import config


from mysql.connector import Error



class ConnectionDataBase:
    def __init__(self) -> None:
        self.connecton = mysql.connector.connect(
            import config
        )
    
    
    