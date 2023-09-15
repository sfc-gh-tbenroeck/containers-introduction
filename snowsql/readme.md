# Why Containers are Great for Packaging and Distributing CLI Tools

When it comes to the development and distribution of CLI tools, containers have revolutionized the way we manage dependencies, ensure environment consistency, and deploy applications seamlessly across various platforms.

## Packaging a CLI Tool as a Docker Image

Packaging your CLI tool as a Docker image involves several steps that facilitate easy distribution and execution in various environments. It's important to understand the roles of `ENTRYPOINT` and `CMD` instructions in the Dockerfile.

### ENTRYPOINT and CMD

Before proceeding, it’s crucial to understand the roles of `ENTRYPOINT` and `CMD` in your Dockerfile:

- `ENTRYPOINT`: This instruction configures the container to execute as an executable. It is the command that gets executed when the container starts. In CLI tools, this is typically the script or binary that runs your application.

- `CMD`: This instruction provides default arguments to the `ENTRYPOINT`. If `CMD` is used without `ENTRYPOINT`, it serves as the command that starts the application. However, when used together with `ENTRYPOINT`, it serves as the default arguments to the `ENTRYPOINT`.


## Building SnowSQL Docker Image
Using the [Installing SnowSQL Documentation](https://docs.snowflake.com/en/user-guide/snowsql-install-config) the Dockerfile was created with the required steps. Run the following command to build a docker image that will run the snowsql code:

```sh
docker build -t snowsql .
```

## Run SnowSQL
We can now run SnowSQL with the following command:

```sh
docker run snowsql <arguments>
```
You can replace `<arguments>` with the CLI tool's specific arguments or options. If you don't provide any arguments, it will use the default argument provided in the `CMD` instruction.

### SnowSQL Examples
```sh
# See the no argument help screen
docker run showsql

# Use the flag -it to interact with the Snowsql program
docker run -it snowsql -a zj26605.us-east4.gcp -u tbenroeck

# Pass SNOWSQL_PWD as an environment variable to bypass having to enter the password
docker run -it -e SNOWSQL_PWD=a-super-secure-password snowsql -a wp48969.west-us-2.azure -u containeruser
```
