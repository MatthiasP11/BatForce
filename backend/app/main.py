import pandas as pd
from fastapi import FastAPI, HTTPException

# The following code is responsible for loading data from a CSV file into a pandas DataFrame.
# It then sets up a FastAPI application with endpoints to access specific data based on query parameters.

# Load the CSV file
csv_file_path = '/app/app/filedati.csv'  # Path to the CSV file containing the data
csv_data = pd.read_csv(csv_file_path, encoding='ISO-8859-1', delimiter=';')  # Loading the CSV data
csv_data['Anno'] = csv_data['Anno'].astype(int)  # Converting the 'Anno' column to integers for year representation
csv_data['Comune'] = csv_data['Comune'].astype(str)  # Ensuring the 'Comune' column is of string type
csv_data['Rifiuto totale (in Kg)'] = csv_data['Rifiuto totale (in Kg)'].astype(str)  # Converting 'Rifiuto totale' to string

app = FastAPI()  # Initializing the FastAPI app

@app.get("/rifiuto/{comune}/{anno}")
def get_rifiuto_totale(comune: str, anno: int):
    """
    Endpoint to get the total waste (Rifiuto totale in Kg) for a specified 'Comune' (city/town) and 'Anno' (year).
    The function queries the loaded CSV data to find the matching record.

    Args:
    comune (str): The name of the city or town.
    anno (int): The year for which the data is required.

    Returns:
    str: The total waste in kilograms for the specified 'Comune' and 'Anno' or an HTTP 404 error if data is not found.
    """
    # Filtering data for the specified 'Comune' and 'Anno'
    data = csv_data[(csv_data['Comune'] == comune) & (csv_data['Anno'] == anno)]
    
    # Handling the case where no data is found
    if data.empty:
        raise HTTPException(status_code=404, detail="Data not found")
    
    return data['Rifiuto totale (in Kg)'].iloc[0]  # Returning the total waste for the specified parameters

@app.get("/")
def read_root():
    """
    Root endpoint of the API.

    Returns:
    dict: A simple greeting message.
    """
    return {"Hello": "World"}  # A basic response for the root endpoint

