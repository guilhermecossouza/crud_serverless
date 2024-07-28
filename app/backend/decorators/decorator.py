def methodGET(fuc):
    def wrapper(event, context):
        if event.get("httpMethod") == "GET":
            return {
                "statusCode": 200,
                "body": "funcionou"
            }
        else:
            return {
                "statusCode": 404,
                "body": "não é get"
            }
        
    return wrapper