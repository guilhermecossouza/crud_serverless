FROM python:3.10-slim

#COMANDOS GLOBAIS   
RUN apt-get update && \
    apt-get install -y curl default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/* && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g serverless@3 && \
    apt-get update

WORKDIR /app

COPY ./app/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN serverless plugin install -n serverless-offline

CMD [ "serverless", "offline", "--host", "0.0.0.0" ]