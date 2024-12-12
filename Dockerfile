# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY ./pipeline.py /app/pipeline.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt


# Create a directory for logs
RUN mkdir /app/logs

# Bind mount the logs directory as a volume
VOLUME /app/logs


CMD ["python", "pipeline.py"]
