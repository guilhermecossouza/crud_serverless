FROM python:3.10-slim

WORKDIR /app

COPY . .

CMD [ "python", "app/backend/app_main.py" ]