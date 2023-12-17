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
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_success_read_item():
    response = client.get("/query/Albert Einstein")
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
