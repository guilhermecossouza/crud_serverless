
from bd_connections import connections

import json

def database_config(event, context):   
    if event.get("httpMethod") == "GET":
        return {
                "statusCode": 200,
                "body": json.dumps({
                    "tabela": connections.create_table(),
                    "event": event
                })
            }
        
def create_user(event, context):
    if event.get("httpMethod") == "POST":
        body = json.loads(event.get("body"))
        return {
                "statusCode": 200,
                "body": json.dumps({
                    "tabela": "ok",
                    "event": event,
                    "username": body.get("nome")
                })
            }
    else:
        return {
                "statusCode": 401,
                "body": json.dumps({
                    "tabela": "ok",
                    "event": event
                })
            }
        
    
        


        
        