print("Rodando...")

from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste01")
async def functeste():
    return {"message": "teste o k a "}

@app.get("/teste02")
async def functeste02():
    return {"teste": True, "num_aleatorio": random.randint(10, 5000)}
