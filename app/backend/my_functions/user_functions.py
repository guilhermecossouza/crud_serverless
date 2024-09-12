import json

def list_users(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }

