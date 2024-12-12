### Guide


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
```docker pull <image>```: Download an image.
```docker run <image>```: Run a container.
```docker ps```: List running containers.
```docker stop <container_id>```: Stop a running container.
```docker rm <container_id>```: Remove a container.
```docker images```: List downloaded images.
```docker rmi <image>```: Remove an image.
- <b>Advanced Commands</b>
```docker-compose up```: Start services defined in docker-compose.yml.
```docker build```: Build an image from a Dockerfile.
```docker exec```: Run commands inside a running container.

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

