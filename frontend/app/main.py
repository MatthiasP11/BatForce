from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# The following code sets up a Flask web application. It includes routes to handle user requests
# and to interact with a FastAPI backend service. The app also uses templates to render HTML pages.

# Secret key configuration for Flask app
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key for session management

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_URL = 'http://backend:80'  # URL of the FastAPI backend service, typically set in a docker-compose environment

@app.route('/internal', methods=['GET', 'POST'])
def internal():
    """
    The '/internal' route handles GET and POST requests.
    On a POST request, it sends a request to the FastAPI backend to retrieve data based on user input.
    It then renders the 'internal.html' template with the retrieved data.
    """
    rifiuto_data = None  # Variable to store data from the backend

    # Handling POST request to fetch data
    if request.method == 'POST':
        comune = request.form.get('comune')  # Getting 'comune' from form data
        anno = request.form.get('anno')  # Getting 'anno' (year) from form data
        if anno:
            # Making a request to the FastAPI backend
            response = requests.get(f"{FASTAPI_BACKEND_URL}/rifiuto/{comune}/{anno}")
        
            # Checking if the response from backend is successful
            if response.status_code == 200:
                rifiuto_data = response.json()  # Parsing the JSON data from the response

    # Rendering the 'internal.html' template with the fetched data
    return render_template('internal.html', rifiuto_data=rifiuto_data)

@app.route('/')
def index():
    """
    The root route ('/') of the application. It simply renders the 'index.html' template.
    """
    # Rendering the 'index.html' template
    return render_template('index.html')  # Ensure 'index.html' exists in the templates directory

# Conditional to ensure the script runs only if it's the main program and not imported as a module
if __name__ == "__main__":
    # Running the Flask app on host '0.0.0.0' and port 80
    app.run(host='0.0.0.0', port=80)
