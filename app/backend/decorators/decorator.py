
import json


def config(func):
    def wrapper(event, context):
        return {
                "statusCode": 200,
                "body": json.dumps({
                    "event": event,
                    "context": context
                }),
            }   
        
    return wrapper