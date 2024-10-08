from controller.user_controller import create_user, get_users, update_user, delete_user

import json

routes = {
    "POST /user/insert": create_user,
    "GET /user/list": get_users,
    "PUT /user/edit/{user_id}": update_user,
    "DELETE /user/delete/{user_id}": update_user    
}

def handler(event, context):
    http_method = event.get("httpMethod")
    path = event.get("path")
    route_key = f"{http_method} {path}"
    
    print(f"path-> {path}")
    
    if route_key in routes:
        return routes[route_key](event, context) 
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Url não encontrada."})   
        }