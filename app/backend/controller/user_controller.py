from models.user import UserModel

import json
import re

def get_users(event, context, parameter):
    httpMethod = event.get("httpMethod", None)
    if httpMethod is None or httpMethod != "GET":
        return {
            "statusCode": 405,
            "body": json.dumps({"message": "Método não permitido. Use GET"}, ensure_ascii=False)
        }
        
    object_user = UserModel()
    response = object_user.get_dados_users(parameter)
    if object_user.connection_error:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": object_user.connection_error}, ensure_ascii=False)
        }
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "", "dados": response}, ensure_ascii=False)
    }
    
    
    
