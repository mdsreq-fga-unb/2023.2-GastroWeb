from fastapi import  APIRouter, Request, HTTPException
from schemas.models import ReceitaBasica
from database.connection import async_session
from database.models import Receitas


recipes = APIRouter()


@recipes.post("/receitas")
async def criar_receita( recipe:ReceitaBasica, request : Request ):

    ip = request.client.host


    async with async_session() as sessao:
        nova_receita = Receitas(
            titulo=recipe.titulo,
            ingredientes=recipe.ingredientes,
            instrucoes=recipe.instrucoes
        )
        sessao.add(nova_receita)
        await sessao.commit()
    return { "message" : "receita adicionada com sucesso!"}



""" @recipes.get("/pegarReceita")
def pegar_receitas( 
    titulo_input:BuscaTitulo, request : Request
) -> bool:
    
 """
