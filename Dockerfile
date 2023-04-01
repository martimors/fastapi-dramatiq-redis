FROM python:3.11-alpine

WORKDIR /var/app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY fastapi-dramatiq-redis/ ./
COPY entrypoint.sh entrypoint.sh

ENTRYPOINT [ "sh", "./entrypoint.sh" ]