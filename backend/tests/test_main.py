import os
import sys
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))
from app.main import app  

client = TestClient(app)

def test_read_main():
    """
    Test the main route of the FastAPI application.

    This test ensures that the main route ('/') is accessible and
    returns the expected response.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_api_endpoint_valid_input():
    """
    Test the API endpoint with valid input.

    This test checks the response of the API when a valid 'comune' and 'anno'
    are provided in the request. For this test, 'Affi' and '1997' are used.
    It validates both the status code and the response content.
    """
    response = client.get("/rifiuto/Affi/1997")
    assert response.status_code == 200
    assert response.json() == {"Rifiuto totale (in Kg)": "1.155.208"}

def test_api_endpoint_invalid_input():
    """
    Test the API endpoint with invalid input.

    This test checks the behavior of the API when an invalid 'comune' and 'anno'
    are provided in the request. For this test, a non-existent city and year are used.
    It validates that the status code is 404, indicating not found.
    """
    response = client.get("/rifiuto/NonExistentCity/3000")
    assert response.status_code == 404
