from src.Main import *
from unittest.mock import patch

# Lista para armazenar os usuários
lista_usuarios = []

def test_helloworld():
    result = helloworld()
    yield result
    assert result == {"message": "Hello World"}

def test_calculadora(num1: int, num2: int):
    with patch (num1 == 10, num2 == 5):
        result = calculadora(num1, num2)
        yield result
        assert result["soma"] == 15
        assert result["subtracao"] == 5
        assert result["multiplicacao"] == 50
        assert result["divisao"] == 2.0

#testar modo do professor depois
def test_num_aleatorio():
    result = num_aleatorio()
    yield result
    assert isinstance(result["num_aleatorio"], int)
    assert 10 <= result["num_aleatorio"] <= 500000
    
def test_criar_usuario():
    usuario_teste = Usuario(id=1, nome="Teste", email="teste@teste")
    yield usuario_teste
    assert usuario_teste == criar_usuario (usuario_teste)

def test_atualizar_usuario():
    result1 = atualizar_usuario(-5)
    result2 = atualizar_usuario(1)
    yield result1, result2
    assert not result1
    assert result2

def test_deletar_usuario():
    result1 = deletar_usuario(-5)
    result2 = deletar_usuario(1)
    yield result1, result2
    assert not result1
    assert result2

def test_listar_usuarios():
    result = listar_usuarios()
    yield result
    assert result
    assert not len(result) != -1
    assert not len(result) == 0
    