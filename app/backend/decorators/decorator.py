from bd_connections.connections import ConnectionBdMysql
import json

def methodGET(fuc):
    def wrapper(event, context):
        if event.get("httpMethod") == "POST":
            objConexao = ConnectionBdMysql()
            with objConexao.open_connect() as conexao:
                if conexao.is_connected():
                    return {
                        "statusCode": 200,
                        "body": json.dumps({"connectBD": "conectado"})
                    }
                else:
                    return {
                        "statusCode": 400,
                        "body": json.dumps({"mensagem": "não conectado"})
                    }
        else:
            return {
                "statusCode": 401,
                "body": json.dumps({"mensagem": "Protocolo não aceito"})
            }
        
    return wrapper