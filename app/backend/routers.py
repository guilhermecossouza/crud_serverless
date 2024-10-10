from controller.user_controller import get_users, delete_user, create_user, update_user

import json

routes = [
    {"http_method": "GET", "path": "/user/list/", "parameter": "{parameter}", "function": get_users},
    {"http_method": "DELETE", "path": "/user/delete/", "parameter": "{parameter}", "function": delete_user},
    {"http_method": "POST", "path": "/user/insert", "parameter": "{parameter}", "function": create_user},
    {"http_method": "PUT", "path": "/user/edit/", "parameter": "{parameter}", "function": update_user}
]

def handler(event, context):
    try:
        http_method = event.get("httpMethod", None)
        path = event.get("path", None) 
        parameter = ""
        
        if "data=" in path:  
            path, parameter = path.split("data=", 1)
            
        for route in routes:
            if http_method == route["http_method"] and path == route["path"]:
                return route["function"](event, context, parameter)
            
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Url não encontrada."}, ensure_ascii=False)   
        }        
    except ValueError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Erro: {str(e)}"}, ensure_ascii=False)   
        }
    except UnboundLocalError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Erro: {str(e)}"}, ensure_ascii=False)   
        }