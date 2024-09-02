from bd_connections.connections import insert_user, get_users
from funcoes.validation import email_validate
import json


def list_users(event, context):
    data_users = get_users()
    return {
        "statusCode": 200,
        "body": json.dumps(data_users)
    }
    
def create_user(event, context):
    if event.get("httpMethod") == "POST":   
        data_user = json.loads(event.get("body"))
        nome = data_user.get("nome")
        email = data_user.get("email")
        if email_validate(email):
            response = insert_user(nome, email)
            return {
                "statusCode": 200,
                "body": json.dumps({"mensagem": response}),
                "headers": json.dumps({"Content-Type": "application/json"})
            }
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"mensagem": "E-mail informado é inválido."}),
                "headers": json.dumps({"Content-Type": "application/json"})
            }    
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"mensagem": "Méthodo não permitido. Use o POST"}),
            "headers": json.dumps({"Content-Type": "application/json"})
        }    

