from controller.user_controller import get_users

import json

routes = [
    {"http_method": "GET", "path": "/user/list/", "parameter": "{parameter}", "function": get_users}
]

def handler(event, context):
    http_method = event.get("httpMethod", None)
    path = event.get("path", None)    
    path, parameter = path.split("data=", 1)
    
    for route in routes:
        if http_method == route["http_method"] and path == route["path"]:
            return route["function"](event, context, parameter)
        
    return {
        "statusCode": 404,
        "body": json.dumps({"message": "Url não encontrada."}, ensure_ascii=False)   
    }
