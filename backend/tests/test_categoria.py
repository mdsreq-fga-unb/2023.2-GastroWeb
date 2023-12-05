import pytest
from views.recipes import criar_receita
from database.models import CategoriasEnum
from typing import List
import asyncio


# Teste para verificar a criação da receita com categoria
@pytest.mark.asyncio
async def test_criar_receita_com_uma_categoria():
    titulo = "Teste de receita com uma categoria"
    instrucoes = "Aqui são as instruções da receita"
    ingredientes = ["teste de ingrediente 1", "teste segundo ingrediente"]
    files = []  
    categorias = ["ALMOCO"]

    result = await criar_receita(titulo, instrucoes, ingredientes, files, categorias)

    assert "message" in result
    assert "receita adicionada com sucesso!" in result["message"]



# Teste para verificar que podemos adicionar mais de uma categoria por receita
@pytest.mark.asyncio
async def test_criar_receita_duas_categorias():
    titulo = "Teste receita com duas categorias"
    instrucoes = "Instruções para a receita"
    ingredientes = ["Primeiro ingrediente", "Segundo ingrediente"]
    files = []  
    categorias = ["JANTAR", "ALMOCO"]
    tags = ["PORCO", "CARNE", "OLEAGINOSAS"]

    result = await criar_receita(titulo, instrucoes, ingredientes, files, categorias, tags)

    assert "message" in result
    assert "receita adicionada com sucesso!" in result["message"]

