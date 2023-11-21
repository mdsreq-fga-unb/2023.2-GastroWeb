from fastapi import FastAPI, APIRouter
from schemas.models import ReceitaBasica

recipes = APIRouter()

receita = []

@recipes.post("/receitas")
def criar_receita( recipe:ReceitaBasica ):
    receita.append(recipe)
    return receita

