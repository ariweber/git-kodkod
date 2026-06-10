from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/status")
def status():
    return  {"fastapi": f"{datetime.now()}"}

