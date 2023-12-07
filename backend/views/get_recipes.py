from fastapi import  APIRouter, Query
from database.connection import async_session
from database.models import Receitas, Fotos, Ingrediente, CategoriaEReceita, TagsEReceita
from sqlalchemy import select
from sqlalchemy.orm import joinedload

get_recipes = APIRouter(tags=["get"])

@get_recipes.get("/busca_categoria_e_tag")
async def get_categorias_e_tags():
    return {"message":"Deu certo"}



@get_recipes.get("/get_receita_por_id")
async def get_receitas_completas(
    receita_id: int
):
    async with async_session() as session:
        categorias_associadas = (
            await session.execute(
                select(CategoriaEReceita)
                .options(joinedload(CategoriaEReceita.categoria))
                .where(CategoriaEReceita.id_receita == receita_id)
            )
        ).scalars().all()

        if not categorias_associadas:
            return {"message": "Receita não encontrada ou sem categoria."}

        # Extrai as categorias associadas
        categorias = [categoria.categoria.categoria for categoria in categorias_associadas]


        tags_associadas = (
            await session.execute(
                select(TagsEReceita)
                .options(joinedload(TagsEReceita.tags))
                .where(TagsEReceita.id_receita == receita_id)
            )
        ).scalars().all()

        if not tags_associadas:
            return {"message": "Receita não encontrada ou sem tags"}

        # Extrai as categorias associadas
        tag = [tags.tags.tag for tags in tags_associadas]
        
        stmt = (
            select(Ingrediente)
            .join(Receitas)
            .filter(Receitas.id == receita_id)
        )
        result = await session.execute(stmt)
        ingredientes = result.scalars().all()
        ingrediente_ordenado = [ingrediente.ingrediente for ingrediente in ingredientes]

        fotin = (
            select(Fotos)
            .join(Receitas)
            .filter(Receitas.id == receita_id)
        )
        result_fotos = await session.execute(fotin)
        fotos = result_fotos.scalars().all()
        fotos_ordenadas = [foto.foto for foto in fotos]

        # Consulta a tabela Receitas para obter as informações da receita
        receita = (
            await session.execute(
                select(Receitas)
                .where(Receitas.id == receita_id)
            )
        ).scalar()

        return {
            "id_receita": receita.id,
            "titulo": receita.titulo,
            "ingredientes": ingrediente_ordenado,
            "instrucoes": receita.instrucoes,
            "categorias": categorias,
            "tags": tag,
            "fotos": fotos_ordenadas
            
        }


@get_recipes.get("/get_all_fotos")
async def read_photos():
    async with async_session() as session:
        result = await session.execute(select(Fotos))
        photos = result.scalars().all()

    return photos


@get_recipes.get("/busca_por_titulo")
async def busca_titulo(titulo: str = Query(..., title="Title to search")):
    async with async_session() as sessao:
        
        query = select(Receitas).where(Receitas.titulo.ilike(f"%{titulo}%"))
        result = await sessao.execute(query)
        busca = result.scalars().all()

    return busca


@get_recipes.get("/get_all_receitas")
async def busca_titulo():
    async with async_session() as sessao:

        result = await sessao.execute(select(Receitas))
        busca = result.scalars().all()
    
    return busca


""" @recipes.get("/obter_fotos_por_receita")
async def obter_fotos_por_receita(receita_id: int):
    async with async_session() as sessao:
        try:
            stmt = (
                select(Fotos)
                .select_from(join(Receitas, Fotos, Receitas.id == Fotos.id_receita))
                .where(Receitas.id == receita_id)
            )
            result = await sessao.execute(stmt)
            fotos = result.scalars().all()
            return fotos
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
"""

""" @recipes.get("/listar_ingredientes")
async def listar_ingredientes(receita_id: int):
    async with async_session() as sessao:
        stmt = (
            select(Ingrediente)
            .join(Receitas)
            .filter(Receitas.id == receita_id)
        )
        result = await sessao.execute(stmt)
        ingredientes = result.scalars().all()

        return ingredientes"""