from fastapi import FastAPI
import db

app = FastAPI()

@app.post("/setup")
def run_setup():
    return {"status": "setup triggered"}

@app.get("/schema")
def get_schema():
    columns = db.get_schema()
    return {"columns": columns}

@app.get("/soliders")
def get_all_soldiers():
    return {"soldiers": []}
