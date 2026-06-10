from fastapi import FastAPI

app = FastAPI()

@app.get("/calc/{a}/{op}/{b}")
def calculter(a,op,b):
    if op == "add":
        return  {"operation": op, "result": int(a)+int(b)}
    elif op == "sub":
        return {"operation": op, "result": a-b}
    elif op == "mul":
        return {"operation": op, "result": a*b}
    elif op == "div":
        if b == 0:
            return {"operation": op, "result": "invalid, zero is not divisible."}
        else:
            return{"operation": op, "result": a/b}
        

        

