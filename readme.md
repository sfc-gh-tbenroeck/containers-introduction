# Introduction to Containers

Welcome to the introduction guide to containers. This guide aims to provide new engineers with an understanding of what containers are, their history, why they are important, and how they differ from virtualization. Additionally, we will delve into core concepts related to container technology.

## Table of Contents

1. [History of Containers](#history-of-containers)
2. [Why are Containers Important?](#why-are-containers-important)
3. [Containers vs. Virtualization](#containers-vs-virtualization)
4. [Core Concepts](#core-concepts)
5. [What are Container Images?](#what-are-container-images)
6. [Image Tagging](#image-tagging)
7. [Image Versioning](#image-versioning)
8. [Docker 101](#docker-101)

## History of Containers

Containers as a concept have been around since the early 2000s, but their popularity surged in recent years. They evolved from chroot system call, which was introduced in 1979 to isolate file systems. Later developments, like FreeBSD jails, Linux VServer, and Solaris Zones, expanded the isolation to other system resources. However, it was the introduction of Docker in 2013 that truly revolutionized the container space, providing an efficient way to package, distribute, and manage applications in containers.

## Why are Containers Important?

Containers play a critical role in modern software development for several reasons:

1. **Portability**: Containers encapsulate an application and its dependencies, making it easy to move across different environments.
2. **Microservices**: They facilitate microservices architecture by allowing the deployment of loosely coupled and independently scalable services.
3. **Resource Efficiency**: Containers share the same OS kernel, which means they consume less resources compared to traditional virtual machines.
4. **Fast Deployment**: Containers can be started almost instantly, which greatly reduces the time required to deploy applications.
5. **DevOps and CI/CD Integration**: Containers integrate seamlessly with modern DevOps tools and CI/CD pipelines, automating many aspects of the software development life cycle.

## Containers vs. Virtualization

While both containers and virtual machines (VMs) provide an environment to run applications isolated from the host system, they differ in several ways:

1. **Operating System**: VMs run a separate operating system instance on top of the hypervisor, while containers share the same OS kernel as the host.
2. **Resource Consumption**: Containers are less resource-intensive than VMs as they share the same OS kernel and avoid the overhead of running separate OS instances.
3. **Startup Time**: Containers can be started in a fraction of the time it takes to boot up a VM.
4. **Isolation Level**: VMs provide strong isolation by separating the OS instances, while containers have slightly weaker isolation as they share the same OS kernel.

## Core Concepts

### 1. Container Images
Container images are lightweight, standalone, executable packages that include the application and all its dependencies. They are immutable and provide a consistent environment to run the application.

### 2. Container Runtime
A container runtime is a system software responsible for running and managing containerized applications. Examples include Docker, containerd, and rkt.

### 3. Orchestration
Container orchestration tools like Kubernetes, Docker Swarm, and OpenShift help manage and scale containerized applications across multiple hosts, handling tasks like load balancing, networking, and storage provisioning.

### 4. Registry
A container registry is a centralized repository to store and distribute container images. Popular registries include Docker Hub, Google Container Registry, and AWS Container Registry.

# Understanding Container Images

Container images are foundational to working with containers. They contain the necessary components to run your applications, such as code, runtime, libraries, and other settings. In this section, we will delve deeper into what container images are, and how tagging and versioning function in the context of container images.

## What are Container Images?

Container images are lightweight, standalone packages that include everything needed to run a piece of software. They comprise the application code, runtime environment, libraries, and other necessary settings and dependencies. Container images are built from a configuration file called a Dockerfile, which has a simple, understandable syntax and a powerful set of commands.

An image serves as a blueprint for containers, and several containers can run the same image simultaneously, functioning independently of each other.

### Characteristics of Container Images:

1. **Immutable**: Once created, the contents of an image cannot be changed.
2. **Reusable**: Images can be reused across different environments, ensuring consistency.
3. **Portable**: Images can be shared and used across different systems, whether in development, testing, or production environments.
4. **Layered**: Images are built in layers, which allows for better use of disk space and quicker build times.

## Image Tagging

Tagging helps in differentiating between different versions of the same image. It is a means of reference that can be used to manage images more efficiently. When an image is tagged, it essentially assigns a descriptive, human-readable label to a specific image ID.

The general syntax for tagging an image is as follows:

```sh
docker tag IMAGE_ID REPOSITORY:TAG
```

### Examples of Image Tags:

1. **Latest**: Indicates the most recent version of an image.
2. **Stable**: Represents a stable and tested version of an image.
3. **Version Numbers**: Semantic versioning tags (e.g., v1.0, v1.0.1) can represent specific versions of an image.

## Image Versioning

Versioning is the process of assigning unique version numbers to individual states of software. In the context of container images, versioning helps in tracking changes, managing updates, and ensuring compatibility.

With Docker, image versioning is usually handled through tags, with each tag representing a different version of the image. This way, specific versions can be referenced, deployed, or rolled back to, as necessary.

### Versioning Strategies:

1. **Semantic Versioning**: Using a versioning scheme like `MAJOR.MINOR.PATCH` helps in understanding the nature and impact of the changes just by looking at the version number.
2. **Timestamps**: Sometimes, images are versioned with timestamps to indicate when they were created.
3. **Hashes**: In some cases, a hash of the content might be used as a version identifier, guaranteeing that the exact content is used.

## Best Practices

1. **Consistent Naming**: Use a consistent naming convention for tags to avoid confusion and to clearly indicate the purpose and stability of each version.
2. **Documentation**: Document changes thoroughly for each new version, providing users with the necessary information to understand what each version entails.
3. **Retaining Important Versions**: While it's good practice to clean up old, unused versions, ensure that important versions are retained and available for rollback if necessary.
4. **Testing**: Each new version should be thoroughly tested to ensure compatibility and stability before release.

# Docker 101

## Introduction
Docker is a powerful tool for containerizing applications and running isolated environments. Here are some basic Docker flags that you'll often use when working with Docker containers:

Here is a handy reference of commonly used Docker commands:

- `docker run IMAGE`: Run a container from the specified image.
- `docker ps`: List all running containers.
- `docker ps -a`: List all containers, both running and exited.
- `docker exec -it CONTAINER_ID /bin/bash`: Access the shell of a running container.
- `docker stop CONTAINER_ID`: Stop a running container.
- `docker rm CONTAINER_ID`: Remove a stopped container.
- `docker images`: List all locally stored Docker images.
- `docker rmi IMAGE_ID`: Remove a Docker image.
- `docker pull IMAGE_NAME`: Download a Docker image from Docker Hub.
- `docker build -t IMAGE_NAME .`: Build a Docker image from the current directory's Dockerfile.
- `docker push IMAGE_NAME`: Push a Docker image to Docker Hub (requires login via `docker login`).

## Docker Run Flags

### `-p` (Port Mapping)
This flag is used to map a network port on the host to a port in the container.

Example:
```sh
docker run -d -p 8080:80 ubuntu:latest
```

### `-v` (Volume)
The `-v` flag allows you to create a volume and mount it to a directory inside the container, which facilitates data persistence and sharing data between host and container.

Example:
```sh
docker run -d -v /path/on/host:/path/in/container ubuntu:latest
```

### `-e` (Environment Variable)
The `-e` flag allows you to set environment variables inside the container, which can be useful for passing configuration settings to your application.

Example:
```sh
docker run -d -e MY_VAR=my_value ubuntu:latest
```

### `--name`
This flag assigns a custom name to the container, making it easier to identify and manage.

Example:
```sh
docker run --name my_container ubuntu:latest
```

### `-d`
Runs the container in detached mode, meaning it runs in the background, freeing up your terminal.

Example:
```sh
docker run -d ubuntu:latest
```

### `--rm`
Automatically removes the container when it exits, which helps to prevent cluttering your system with exited containers.

Example:
```sh
docker run --rm ubuntu:latest
```

### `-it`
Often used together (`-i` to keep STDIN open and `-t` to allocate a pseudo-TTY), this flag allows you to interact with the container from the terminal.

Example:
```sh
docker run -it ubuntu:latest /bin/bash
```

## Viewing Container Logs

To view the stdout log of a running container in Docker, you can use the `docker logs` command. Here's how you can do it:

```sh
docker logs [Container_ID or Container_Name]
```

Here are some additional options you might find useful:

- **Follow Log Output**: Use the `-f` flag to follow the log output (similar to `tail -f`).

  ```sh
  docker logs -f [Container_ID or Container_Name]
  ```

- **Logs Since a Specific Time**: Use the `--since` option to show logs since a specific time.

  ```sh
  docker logs --since=2023-09-14T10:00:00 [Container_ID or Container_Name]
  ```

- **Show Last N Lines of Logs**: Use `--tail` to show only the last N lines of logs.

  ```sh
  docker logs --tail=100 [Container_ID or Container_Name]
  ```

Remember to replace `[Container_ID or Container_Name]` with the actual ID or name of your running container. You can get the ID or name of your running containers with the command:

```sh
docker ps
```

This will list all running containers along with their IDs and names.
