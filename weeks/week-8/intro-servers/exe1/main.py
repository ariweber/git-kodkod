from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_ping():
    return{"status": "ping"}