### Guide to Docker

<b>1. Introduction</b>
- <b>What is Docker?</b>
>Brief explanation of Docker as a platform for developing, shipping, and running applications in containers.
- <b>Why Use Docker?</b>
>Highlight benefits such as portability, efficiency, and consistency across environments.

<b>2. Key Concepts</b>
- <b>Images:</b> Pre-configured templates for creating containers.
- <b>Containers:</b> Running instances of Docker images.
- <b>Dockerfile:</b> Blueprint for creating custom images.
- <b>Volumes:</b> Persistent storage for containers.
- <b>Networks:</b> Communication between containers and external systems.

<b>3. Common Commands</b>
- <b>Basic Commands</b>
    - ```docker pull <image>```: Download an image.
    - ```docker run <image>```: Run a container.
    - ```docker ps```: List running containers.
    - ```docker stop <container_id>```: Stop a running container.
    - ```docker rm <container_id>```: Remove a container.
    - ```docker images```: List downloaded images.
    - ```docker rmi <image>```: Remove an image.
- <b>Advanced Commands</b>
    - ```docker-compose up```: Start services defined in docker-compose.yml.
    - ```docker build```: Build an image from a Dockerfile.
    - ```docker exec```: Run commands inside a running container.

<b>4. Creating a Dockerfile</b>
- What is a Dockerfile?
> A script that defines how to build a Docker image.

- <b> Sample Dockerfile</b>
```typescript
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
ADD . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "pipeline.py"]
```

<b>5. Using Docker Compose</b>
- <b>What is Docker Compose?</b>
> Tool for defining and running multi-container applications.

- <b>Sample docker-compose.yml</b>

```typescript
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    depends_on:
      - redis
  redis:
    image: "redis:alpine"
```

<b>6. Best Practices</b>
- Use .dockerignore to exclude unnecessary files.
- Keep images lightweight by using minimal base images.
- Tag images with meaningful names and versions.
- Regularly clean up unused images, containers, and volumes.


### Guide to Celery
<b>1. Introduction</b>
- <b>What is Celery?</b>
> Celery is an asynchronous task queue/job queue based on distributed message passing.
- <b>Why Use Celery?</b>
    - Efficient background task execution.
    - Supports scheduling.
    - Works well with various message brokers like RabbitMQ, Redis, etc.

<b>2. Installation</b>
- <b>Prerequisites</b>
    - Python (>= 3.x).
    - A message broker (e.g., RabbitMQ, Redis).
- <b>Installation Steps</b>
```typescript
pip install celery[redis]
```
<b>3. Key Concepts</b>
- <b>Tasks:</b> Units of work to be executed.
- <b>Workers:</b> Processes that execute tasks.
- <b>Brokers:</b> Middlemen that queue tasks (e.g., Redis, RabbitMQ).
- <b>Results Backend:</b> Stores the results of tasks.

<b>4. Setting Up Celery</b>
- <b>Basic Project Structure</b>
```
project/
├── tasks.py
├── worker.py
└── requirements.txt
```

- <b>Creating a Simple Celery App (```tasks.py```)</b>
```python
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y
```

<b>5. Running Celery</b>
- <b>Start the Worker</b>
```typescript
celery -A tasks worker --loglevel=info
```
- <b>Call Tasks</b>
```python
from tasks import add

result = add.delay(4, 6)
print(result.get())  # Output: 10
```

<b>6. Scheduling Tasks</b>
- <b>Installing the Scheduler</b>
```bash
pip install celery[redis]
```
- <b>Add a Periodic Task Modify ```celery.py```:</b>
```pyhton
from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s('hello'), name='Add every 10 seconds')
    sender.add_periodic_task(crontab(hour=7, minute=30), test.s('morning!'))

@app.task
def test(arg):
    print(arg)
```

- <b>Start the Scheduler</b>
```bash
celery -A tasks beat --loglevel=info
```
<b>7. Configuration</b>
- <b>Add a ```celeryconfig.py``` file for custom settings:</b>
```python
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True
```

<b>8. Monitoring and Debugging</b>
- <b>Flower: Celery monitoring tool.</b>
```bash
pip install flower
celery -A tasks flower
```

- <b>Common Debugging Tips:</b>
    - Check broker status.
    - Verify worker logs (--loglevel=debug).

