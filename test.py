from fastapi import FastAPI
import requests
import json

app = FastAPI()


@app.get('/getusers')
def index():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url).json()
    return response

