import os
import sys
from fastapi.testclient import TestClient

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app


"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
 """

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
    assert response.json() == {"person_name": 'Albert Einstein', 
                               "birthday": '03/14/1879'}


""" def test_fail_read_item():
    response = client.get("/query/Pippo")
    assert response.status_code == 200
    assert response.json() == {"error": "Person not found"} """


# The following will generate an error in pycheck
""" def test_success_read_item_module():
    response = client.get("/module/search/Albert Einstein")
    assert response.status_code == 200
    assert response.json() == {"Albert Einstein's birthday is 03/14/1879."} """


# The following is correct, can you spot the diffence?
def test_success_read_item_module():
    response = client.get("/module/search/Albert Einstein")
    assert response.status_code == 200
    assert response.json() == ["Albert Einstein's birthday is 03/14/1879."]
