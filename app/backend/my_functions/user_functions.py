from funcoes.validation import email_validate
import json


def list_users(event, context):
    response = json.dumps(
        [
            {
                "dados": [
                    {"nome":"Guilherme001", "email": "guilhermecossouza001@gmail.com"},
                    {"nome":"Guilherme002", "email": "guilhermecossouza002@gmail.com"},
                    {"nome":"Guilherme003", "email": "guilhermecossouza003@gmail.com"},
                    {"nome":"Guilherme004", "email": "guilhermecossouza004@gmail.com"},
                    {"nome":"Guilherme005", "email": "guilhermecossouza005@gmail.com"},
                    {"nome":"Guilherme006", "email": "guilhermecossouza006@gmail.com"}
                ]
            }            
        ]
    )
    return {
        "statusCode": 200,
        "body": response
    }
    
def create_user(event, context):
    if event.get("httpMethod") == "POST":   
        data_user = json.loads(event.get("body"))
        nome = data_user.get("nome")
        email = data_user.get("email")
        if email_validate(email):
            return {
                "statusCode": 200,
                "body": json.dumps({"event": event})
            }
        else:
            return {
                "statusCode": 400,
                "body": "E-mail informado é inválido.",
                "headers": json.dumps({"Content-Type": "application/json"})
            }    
    else:
        return {
            "statusCode": 405,
            "body": "Méthodo não permitido. Use o POST",
            "headers": json.dumps({"Content-Type": "application/json"})
        }    

