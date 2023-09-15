# Using a Devcontainer to Develop a Go Application

## Open Your Project in the Devcontainer
1. Press `F1` to open the command palette.
2. Type "Dev Containers: Reopen in Container" and press Enter. If the devcontainer configuration has changed, it might be "Dev Containers: Rebuild and Reopen in Container".
3. VS Code will build the Docker image as per the devcontainer configuration and start the container. Your VS Code window will then reconnect to the running container.
4. You'll now be working inside the container. You can install extensions, edit files, run your project, etc., all within the isolated environment of the container.

## Working Inside the Devcontainer
1. Once inside the container, you'll notice that the VS Code terminal is now running inside the container, not on your local machine.
2. You can install software, run your application, and do everything you'd normally do in a development environment, but it will all be isolated inside the container.
3. You can use VS Code's built-in source control features to commit and push your changes as usual, including the changes to the `.devcontainer` folder, which contains your devcontainer configuration.

## Run the Application
In the VS Code terminal, you can now run `go run main.go` to run the web server. VS Code can automatically detect ports that should be opened and will map them to be accessible from your local machine. If this doesn't happen, or if you know what ports your application will use, you should modify the `.devcontainer/devcontainer.json` file and add the `"forwardPorts": []` setting.

**Example devcontainer.json**
```json
{
	"name": "Go",
	"image": "mcr.microsoft.com/devcontainers/go:1-1.21-bullseye",
	"forwardPorts": [8080]
}
```
