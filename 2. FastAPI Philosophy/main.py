from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message' : 'Hello World'}

@app.get("/about")
def about():
    return {'message' : 'This is a FastAPI application demonstrating the philosophy of building APIs quickly and efficiently.'}