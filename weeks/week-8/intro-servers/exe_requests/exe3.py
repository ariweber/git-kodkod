from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def get_greet(name= "wolrd"):
    return {f"message: hello {name}"}
