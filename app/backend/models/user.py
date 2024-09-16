

class UserModel:
    def __init__(self) -> None:
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
        
    
    
    