"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
    



app = FastAPI()

# Load the new CSV data
df = pd.read_csv('/app/app/filedati.csv', encoding= "latin-1", sep=";")
@app.get("/total_waste")
def read_total_waste(comune: str, anno: int):
    """
    Endpoint to get the total waste for a given "Comune" and "Anno".
    """
    data = df[(df['Comune'] == comune) & (df['Anno'] == anno)]
    if not data.empty:
        return {"Rifiuto totale (in Kg)": data["Rifiuto totale (in Kg)"].sum()}
    else:
        return JSONResponse(status_code=404, content={"message": "Data not found for the provided Comune and Anno."})

@app.get("/total_waste_sum")
def read_total_waste_sum(comune: str):
    """
    Endpoint to get the sum of all "Rifiuto totale (in Kg)" for a given "Comune" across all years.
    """
    data = df[df['Comune'] == comune]
    if not data.empty:
        return {"Rifiuto totale (in Kg) sum": data["Rifiuto totale (in Kg)"].sum()}
    else:
        return JSONResponse(status_code=404, content={"message": "Data not found for the provided Comune."})



@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}

@app.get('/get-date')
def get_date():
    """
    Endpoint to get the current date.

    Returns:
        dict: Current date in ISO format.
    """
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
