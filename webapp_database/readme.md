# Flask & PostgreSQL Dockerized Application

This project is a simple Flask application that interfaces with a PostgreSQL database, both running in separate Docker containers managed by Docker Compose.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed and running.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Getting Started

Follow these steps to get the application up and running:

### Step 1: Clone the Repository

Clone the repository to your local machine by creating a new folder and adding the necessary files as described in the above project description. You should have a directory structure that looks like this:

```plaintext
webapp_database/
├── app.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

### Step 2: Build and Run the Docker Containers

Open a terminal and navigate to the project directory (`flask_postgres_app`). Run the following command to build and start the Docker containers:

```bash
docker-compose up --build
```

### Step 3: Initialize the Database

Before you can interact with the application, you'll need to create a table in the PostgreSQL database to store records. Run the following command to create a `records` table:

```bash
docker-compose exec db psql -U postgres -c "CREATE TABLE records (id SERIAL PRIMARY KEY, name VARCHAR(50), age INT);"
```

### Step 4: Interact with the Application

With the services running, you can interact with the Flask application:

1. Visit `http://localhost:5000` in your web browser to see a "Hello, Docker!" message.
2. Use `curl` or a tool like Postman to interact with the `/records` endpoint:

   - To add a new record, use a POST request with JSON data:
     ```bash
     curl -X POST -H "Content-Type: application/json" --data '{"name":"John", "age":30}' http://localhost:5000/records
     ```

   - To retrieve all records, use a GET request:
     ```bash
     curl http://localhost:5000/records
     ```

### Step 5: Stopping the Application

Once you're done, you can stop the services by running the following command in the terminal:

```bash
docker-compose down
```

This command stops and removes all containers defined in the `docker-compose.yml` file.

## Understanding and Configuring Volumes

In Docker, volumes are used to persist data and share directories between containers and the host system. There are two main types of volumes: named volumes and bind mounts (non-named volumes).

### Named Volumes

Named volumes are managed by Docker and data is stored in a part of the host filesystem which is managed by Docker. The main advantage of named volumes is that Docker manages the storage location, making it easier to backup, migrate, and manage the data.

To configure a named volume, add a `volumes` section at the bottom of your `docker-compose.yml` file and specify a volume under the service:

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

In this setup:
- `postgres_data:` under the `volumes` section at the bottom creates a named volume.
- The line `- postgres_data:/var/lib/postgresql/data` in the `db` service maps the named volume to the PostgreSQL data directory inside the container.

#### Viewing Volumes:
You can view the list of volumes by running:

```bash
docker volume ls
```

#### Inspecting a Volume:
To inspect the contents of a volume or to get more details about a volume, use:

```bash
docker volume inspect postgres_data
```

#### Removing a Volume:
If you ever need to remove the volume (note this will delete the data stored in the volume), you can use:

```bash
docker volume rm postgres_data
```


### Bind Mounts (Non-Named Volumes)

Bind mounts are directories or files on the host machine that are mounted into containers. Bind mounts allow you to specify the exact mount point on the host system. It can be used for more fine-grained control of the storage.

To configure a bind mount, you specify a host path instead of a named volume. Create a directory in your project folder (or anywhere on your host system), and modify the `docker-compose.yml` file to point to that directory:

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - ./postgres_data:/var/lib/postgresql/data
```

In this setup:
- We created a `postgres_data` directory in the same location as the `docker-compose.yml` file (you can specify any path).
- The line `- ./postgres_data:/var/lib/postgresql/data` in the `db` service binds this directory to the PostgreSQL data directory inside the container.

**Note**: Ensure that the directory has the proper permissions to allow PostgreSQL to write data to it.

### Switching Between Named Volumes and Bind Mounts

To switch between named volumes and bind mounts, modify the `volumes` section under the `db` service in the `docker-compose.yml` file. Remember to handle data migration between the two types of volumes as necessary to prevent data loss.
