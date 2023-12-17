# Waste Quantification in Italian Towns

This project is designed to quantify waste in specified towns in Italy over various years. It features a FastAPI backend for data processing and a Flask frontend for user interaction, both containerized using Docker.

## Architecture

The project follows a simple client-server architecture:

1. **Frontend (Flask):**
   - Represents the user interface or client side.
   - Built with Flask, a lightweight web framework for Python.
   - Responsible for rendering web pages and user interaction, including the form for querying the backend.

2. **Backend (FastAPI):**
   - Represents the server or backend of the application.
   - Built with FastAPI, a modern web framework for building APIs with Python.
   - Handles requests from the frontend, including querying the towns and years for the waste production.
3. **Docker Compose:**
   - Orchestrates the deployment of both frontend and backend as separate containers.
   - Ensures seamless communication between frontend and backend containers.
   - Simplifies the deployment and management of the entire application.

### Communication
Bidirectional communication is established between the Frontend (Flask) and Backend (FastAPI). Docker Compose facilitates this communication, allowing the components to work together seamlessly.

## Project Structure

- `backend/`: FastAPI backend implementation.
    - Dockerfile: Dockerfile for building the backend image.
    - main.py: Main backend application file.
    - requirements.txt: List of Python dependencies for the backend.
- `frontend/`: Flask frontend implementation.
    - Dockerfile: Dockerfile for building the frontend image.
    - static/: Folder for static files (CSS, JavaScript, etc.).
    - templates/: Folder for HTML templates.
    - main.py: Main frontend application file.
    - requirements.txt: List of Python dependencies for the frontend.
- `docker-compose.yml`: Docker Compose configuration for running both frontend and backend.

## Prerequisites

- Python 3.8+
- Docker (for containerization)
- FastAPI, Flask, and additional Python libraries listed in requirements.txt

## Usage

1. Clone the repository and navigate in the directory:

    ```bash
    git clone Repository_URL
    cd BatForce
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

    This will start both the frontend and backend containers.

3. Open your web browser and navigate to [http://localhost:8080](http://localhost:8080) to access the `frontend` and [http://localhost:8081](http://localhost:8081) to access the `backend`.

4. Use the form on the frontend to query the name of the town and the year from the backend.

## Shutting Down the Docker Containers

To shut down the running Docker containers, you can use the following steps:

1. Open a terminal.

2. Navigate to the project root directory.

3. Run the following command to stop and remove the Docker containers:

    ```bash
    docker-compose down
    ```

## Starting and Stopping Containers Individually

If you need to start or stop the containers individually, you can use the following commands:

- **Start Frontend Container:**

    ```bash
    docker-compose up frontend
    ```

- **Stop Frontend Container:**

    ```bash
    docker-compose stop frontend
    ```

- **Start Backend Container:**

    ```bash
    docker-compose up backend
    ```

- **Stop Backend Container:**

    ```bash
    docker-compose stop backend
    ```

Make sure to replace `frontend` and `backend` with the appropriate service names from your `docker-compose.yml` file.

### Notes:

When stopping containers individually, the `docker-compose down` command is not required.
Now you can manage the lifecycle of your Docker containers more flexibly.


## Debugging with Visual Studio Code and Docker Extension

1. Open the project in Visual Studio Code:

    ```bash
    code .
    ```

2. Set breakpoints in your Python code as needed.

3. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

    Ensure that your Docker containers are running.

4a. Install the [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) for Visual Studio Code.
4b. Install the [Remote Development Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) for Visual Studio Code

5. Open the "Docker" view in Visual Studio Code by clicking on the Docker icon in the Activity Bar.

6. Under "Containers," you should see your running containers. Right-click on the container running your Flask or FastAPI application.

7. Select "Attach Visual Studio Code" from the context menu. This will configure the container for debugging.

8. Open the Run view in Visual Studio Code and select the "Python: Remote Attach" configuration.

9. Click the "Run" button to start the debugger.

10. Access the frontend in your web browser and trigger the actions you want to debug.

### Notes:

- Ensure that your Docker containers are running (`docker-compose up --build`) before attaching Visual Studio Code.

- Adjust the container name in the "Docker: Attach to Node" configuration if needed.

- The provided configurations assume that your Flask or FastAPI application is running with the debugger attached. Adjust the configurations if needed.

- If using Flask, ensure that the Flask application is started with the `--no-reload` option to prevent automatic reloading, which can interfere with debugging.

- Debugging FastAPI requires configuring the FastAPI application to run with the `--reload` option. Update the FastAPI Dockerfile CMD accordingly.

- After the debugger is attached, you can use breakpoints, inspect variables, and step through your code as needed.


## Adding New Modules to a Running Docker Container

1. **Install Additional Modules:**
    ```bash
    pip install new_module
    ```
   Replace `new_module` with the names of the module you want to install.

2. **Verify Installed Modules:**
    ```bash
    pip list
    ```
   This command displays a list of installed Python packages, including the newly added modules.

3. **Optional: Update requirements.txt:**
    ```bash
    pip freeze > requirements.txt
    ```
   If you want to keep track of the installed modules, you may choose to update the `requirements.txt` file inside the container.


Now, the additional Python modules are installed in the running container, and you've performed these actions directly from the VS Code terminal. If these changes are intended for production, consider updating the `requirements.txt` file and rebuilding the Docker container.

### Features
Data Processing: Analyze waste data from CSV files using Pandas in the FastAPI backend.
User Interface: Interactive web interface created with Flask for querying and displaying data.
Docker Support: Containerized setup for easy deployment and scaling.

The program, through the data entered by the user in the 'Comune' (Municipality) and 'Year' text boxes, sends a result showing, on the screen, the value of the "Total waste (in Kg)" for the municipality and year chosen by the user.

### Usage
The Flask frontend provides a web interface to interact with the FastAPI backend.
Users can query the year and town they prefer to see the amount of waste.
### Contributing
Contributions are welcome. Please read the contribution guidelines before submitting pull requests.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.

