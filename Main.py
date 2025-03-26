from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/teste01")
async def functeste():
    return {"message": "teste o k a "}