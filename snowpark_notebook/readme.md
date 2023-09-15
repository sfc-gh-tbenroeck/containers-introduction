## Building Your Docker Image
Build your Docker image using the following command:

```sh
docker build -t snowpark .
```

## Run Your Application
Now run your application with the following command:

```sh
docker run -it -v $(pwd)/notebooks:/notebooks -p 8888:8888 snowpark

``
