from models.user import UserModel

import json
import re

def create_user(event, context):
    if event.get("httpMethod") != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({
                "message": "Método não permitido. Use POST"}, ensure_ascii=False)
        }   
    try:
        body = json.loads(event.get("body"))            
    except (TypeError, json.JSONDecodeError) as e:
        return  {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Erro ao receber dados do usuário",
                "typeErro": f"{str(e)}"
            })
        }      
    
    nome = body.get("nome")
    email = body.get("email")        
    
    if not nome or not email:
        return {
            "statusCode": 401,
            "body": json.dumps({
                "message": "Os campos nome e email são obrigatórios"}, ensure_ascii=False)
        } 

    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex, email):
        return {
            "statusCode": 402,
            "body": json.dumps({"message": "Formato de email inválido"}, ensure_ascii=False)
        }
        
    object_user = UserModel()  
    object_user.set_nome(nome)
    object_user.set_email(email)
    object_user.create()
    if object_user.connection_error:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": object_user.connection_error}, ensure_ascii=False)
        }
        
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Usuário criado com sucesso"}, ensure_ascii=False)
    }
           
    
def get_users(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"function": "get_users"}, ensure_ascii=False)
    }
    
def update_user(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "function": "update_user"
        }, ensure_ascii=False)
    }
    
def delete_user(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "function": "delete_user"
        }, ensure_ascii=False)
    }
    
