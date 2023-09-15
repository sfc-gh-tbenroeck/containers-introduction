## Building Your Docker Image
Build your Docker image using the following command:

```sh
docker build -t webapp .
```

## Run Your Application
Now run your application with the following command:

```sh
docker run -p 4000:80 webapp
```
You should be able to browse the app by going to http://localhost:4000 on your local machine.

**Note:** When using -p the mapping is local_system_port:container_port.
