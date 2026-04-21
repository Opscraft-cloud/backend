from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"HelloWorld"}

@app.get("/root1")
def root1():
    return {"message":"HelloWorldROOT1"}