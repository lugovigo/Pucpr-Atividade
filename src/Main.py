from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# Modelo de dados do usuário
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

# Lista para armazenar os usuários
lista_usuarios = []

@app.get("/Helloworld")
async def helloworld():
    return {"message": "Hello World"}

@app.get("/Calculadora/{num1}/{num2}")
async def calculadora(num1: int, num2: int):
    return {
        "soma": num1 + num2,
        "subtracao": num1 - num2,
        "multiplicacao": num1 * num2,
        "divisao": num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"
    }

@app.get("/num_aleatorio")
async def num_aleatorio():
    return {"num_aleatorio": random.randint(10, 500000)}

# Cadastrar usuário
@app.post("/usuario/cadastro")
async def criar_usuario(usuario: Usuario):
    lista_usuarios.append(usuario)
    return usuario

# Atualizar usuário
@app.put("/usuario/atualizar/{usuario_id}")
async def atualizar_usuario(usuario_id: int, usuario: Usuario):
    for index, u in enumerate(lista_usuarios):
        if u.id == usuario_id:
            if usuario_id != usuario.id:
                raise HTTPException(status_code=400, detail="ID do usuário não corresponde ao ID fornecido")
            lista_usuarios[index] = usuario
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Deletar usuário
@app.delete("/usuario/deletar/{usuario_id}")
async def deletar_usuario(usuario_id: int):
    for u in lista_usuarios:
        if u.id == usuario_id:
            lista_usuarios.remove(u)
            return {"message": f"Usuário com ID {usuario_id} deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Listar usuários
@app.get("/usuario/lista")
async def listar_usuarios():
    if len(lista_usuarios) == 0:
        raise HTTPException(status_code=404, detail="Nenhum usuário encontrado")
    else:
        print(lista_usuarios)