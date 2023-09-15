## Building Your Docker Image
Build your Docker image using the following command:

```sh
docker build -t snowpark .
```

## Run Your Application
Now run your application with the following command:

```sh
docker run -it -v $(pwd)/notebooks:/notebooks -p 8888:8888 snowpark

```

## Open Jupyter
In the log out put you will see the url with token (`http://127.0.0.1:8888/tree?token=fe92648ec3f89823523e1624c71a251da612a75995f3cffb`) browse to that from your local machine.

## Run the container in the background
You can use the `-d` flag instead of `-it` to run the container in the bacground and free up your terminal shell.   To find the url and token you will want to run a `docker ps` and then get the log files of the running container `docker logs 70e70e37b7c87f3` where 70e70e37b7c87f3 is your container id.

**Tip** you don't need to put the full container id, only enough characters to be unique, ex 70e
