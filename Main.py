from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

#http://127.0.0.1:8000/teste01
@app.get("/teste01")
async def functeste():
    return {"message": "teste o k a "}