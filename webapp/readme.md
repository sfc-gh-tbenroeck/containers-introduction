## Building Your Docker Image
Build your Docker image using the following command:

```sh
docker build -t webapp .
```

## Run Your Application
Now run your application with the following command:

```sh
docker run -p 4000:80 webapp
``
Your app should now be running on http://localhost:4000.
