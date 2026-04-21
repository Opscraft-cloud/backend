from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"HelloWorld"}

@app.get("/root1/{id}")
def root1(id:int):
    return {"message":f"HelloWorldROOT1 {id}"}
@app.post("/root1")
def root1(item:dict):
    return {"message":f"HelloWorldROOT1, item:{item}"}