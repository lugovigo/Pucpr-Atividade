from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# Modelo de dados do usuário
class User(BaseModel):
    id: int
    nome: str
    email: str

# Lista simulando um banco de dados
db = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste01")
async def functeste():
    return {"message": "teste o k a "}

@app.get("/teste02")
async def functeste02():
    return {"teste": True, "num_aleatorio": random.randint(10, 500000)}

@app.post("/usuarios")
async def criar_usuario(user: User):
    db.append(user)
    return user

@app.get("/usuarios/{user_id}")
async def obter_usuario(user_id: int):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.put("/usuarios/{user_id}")
async def atualizar_usuario(user_id: int, user_update: User):
    for index, user in enumerate(db):
        if user.id == user_id:
            db[index] = user_update
            return user_update
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/usuarios/{user_id}")
async def deletar_usuario(user_id: int):
    for index, user in enumerate(db):
        if user.id == user_id:
            del db[index]
            return {"message": "Usuário deletado"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
