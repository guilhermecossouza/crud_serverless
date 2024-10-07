
from mysql.connector import connect, ProgrammingError
from contextlib import contextmanager

import config.settings


class ConnectionDataBase:
    def __init__(self):
        self.connection = None
        self.connection_error = None
    
    @contextmanager    
    def open_connect(self):
        self.connection = connect(**config.settings.PARAMETROS)
        try:            
            yield self.connection
        finally:
            if self.connection and self.connection.is_connected():
                self.connection.close()

           
            
                 
            
                
            
            
            
            
    
                
    