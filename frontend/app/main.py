"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template, request, jsonify
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://127.0.0.1:8000'  # Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class QueryForm(FlaskForm):
    comune = StringField('Comune', validators=[DataRequired()])
    anno = IntegerField('Anno', validators=[DataRequired()])
    submit = SubmitField('Get Birthday from FastAPI Backend')


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    # Fetch the date from the backend
    date_from_backend = fetch_date_from_backend()
    return render_template('index.html', date_from_backend=date_from_backend)

def fetch_date_from_backend():
    """
    Function to fetch the current date from the backend.

    Returns:
        str: Current date in ISO format.
    """
    backend_url = 'http://backend/get-date'  # Adjust the URL based on your backend configuration
    try:
        response = requests.get(backend_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('date', 'Date not available')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching date from backend: {e}")
        return 'Date not available'



@app.route('/internal', methods=['GET', 'POST'])
def internal():
    form = QueryForm()
    total_waste = None
    total_waste_sum = None
    if form.validate_on_submit():
        comune = form.comune.data
        anno = form.anno.data
        waste_response = requests.get(f'{FASTAPI_BACKEND_HOST}/total_waste', params={'comune': comune, 'anno': anno})
        sum_response = requests.get(f'{FASTAPI_BACKEND_HOST}/total_waste_sum', params={'comune': comune})
        if waste_response.ok:
            total_waste = waste_response.json()
        if sum_response.ok:
            total_waste_sum = sum_response.json()
    return render_template('internal.html', form=form, total_waste=total_waste, total_waste_sum=total_waste_sum)

  
if __name__ == '__main__':
    app.run(debug=True)