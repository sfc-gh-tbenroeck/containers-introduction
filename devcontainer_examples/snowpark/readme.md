# Using a Devcontainer to Develop a Go Application

## Open Your Project in the Devcontainer

1. Press `F1` to open the command palette.
2. Type "Dev Containers: Reopen in Container" and press Enter. If the devcontainer configuration has changed, it might say "Dev Containers: Rebuild and Reopen in Container" instead.
3. VS Code will build the Docker image as per the devcontainer configuration and start the container. Your VS Code window will then reconnect to the running container.
4. You'll now be working inside the container. You can install extensions, edit files, run your project, etc., all within the isolated environment of the container.

## Working Inside the Devcontainer

1. Once inside the container, you'll notice that the VS Code terminal is now running inside the container, not on your local machine.
2. You can install software, run your application, and perform everything you'd normally do in a development environment, but it will all be isolated inside the container.
3. You can use VS Code's built-in source control features to commit and push your changes as usual, including the changes to the `.devcontainer` folder which contains your devcontainer configuration.

## Using the Snowpark Container

Notice that the VS Code terminal is now loaded into the `snowpark_env` conda Python kernel. You can create a new .ipynb in your workspace or run `cp /example/* .` in the terminal to bring the example notebook and auth.json file from the container into the local workspace. You will notice that any changes you make in the workspace will remain on your local file system.

## Run the Notebook Cells

When you run a notebook cell, VS Code will need to know which Python interpreter to use. Notice how these are not your local system interpreters, but instead those present in the Docker container. If VS Code does not prompt you for an interpreter selection, you can press `F1` and type "Python: Select Interpreter" to choose one.
