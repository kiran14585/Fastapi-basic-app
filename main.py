from fastapi import FastAPI
import requests
import json
from fastapi.responses import JSONResponse

from models import Addition
from routes import addition1


app = FastAPI(docs_url="/homepage")


@app.get("/getusers")
def index():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url).json()
    
    username = []
    for dict1 in response:
        username.append(dict1['username'])
    return JSONResponse(
        content={"success": True, "usernames": username},
        status_code=200,
    )
# Create a post request with 


@app.post("/addition")
def addition(payload : Addition):
    return addition1(payload.number1,payload.number2)
 
    
    



