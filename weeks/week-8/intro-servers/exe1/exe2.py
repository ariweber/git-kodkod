from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "my-api", "version": "1.0"}

app.get("/user/admin")
def get_admin():
    return{"roly": "admin", "access": "full"}

@app.get("/user{user_id}")
def user(user_id):
    return {"user": user_id,
            "name": "aharon",
            "mail": f'{user_id}@gmail.com'}

