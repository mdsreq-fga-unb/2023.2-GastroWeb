from fastapi import  APIRouter, Query, Depends
from fastapi.responses import FileResponse
from database.connection import async_session
from database.models import Receitas, Fotos, Ingrediente, CategoriaEReceita, TagsEReceita, Categorias, CategoriasEnum, Tags, TagsEnum
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from typing import List
from views import auth_user

get_recipes = APIRouter(tags=["Get"]) #dependencies=[Depends(auth_user.get_current_active_user)] -> para ativar a autenticação


@get_recipes.get("/get_receita_por_id")
async def get_receitas_completas(
    receita_id: int
):
    async with async_session() as sessao:
        categorias_associadas = (
            await sessao.execute(
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
            await sessao.execute(
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
        result = await sessao.execute(stmt)
        ingredientes = result.scalars().all()
        ingrediente_ordenado = [ingrediente.ingrediente for ingrediente in ingredientes]

        fotin = (
            select(Fotos)
            .join(Receitas)
            .filter(Receitas.id == receita_id)
        )
        result_fotos = await sessao.execute(fotin)
        fotos = result_fotos.scalars().all()
        fotos_ordenadas = [foto.foto for foto in fotos]

        # Consulta a tabela Receitas para obter as informações da receita
        receita = (
            await sessao.execute(
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

@get_recipes.get("/busca_categoria_e_tag")
async def get_categorias_e_tags(
    categoria: str | None = None,
    tag: str | None = None
):
    async with async_session() as sessao:
        procura = select(Receitas)

        if tag and categoria:

            subquery_tags = (
                select(TagsEReceita.id_receita)
                .join(Tags)
                .where(Tags.tag == tag)
            ).alias("subquery_tags")
            subquery_categoria = (
                select(CategoriaEReceita.id_receita)
                .join(Categorias)
                .where(Categorias.categoria == categoria)
            ).alias("subquery_categoria")

            procura = procura.join(subquery_tags, Receitas.id == subquery_tags.c.id_receita)
            procura = procura.join(subquery_categoria, Receitas.id == subquery_categoria.c.id_receita)

        else:

            if tag:
                subquery_tags = (
                    select(TagsEReceita.id_receita)
                    .join(Tags)
                    .where(Tags.tag == tag)
                ).alias("subquery_tags")

                procura = procura.join(subquery_tags, Receitas.id == subquery_tags.c.id_receita)

            elif categoria:
                subquery_categoria = (
                    select(CategoriaEReceita.id_receita)
                    .join(Categorias)
                    .where(Categorias.categoria == categoria)
                ).alias("subquery_categoria")

                procura = procura.join(subquery_categoria, Receitas.id == subquery_categoria.c.id_receita)


        procura = procura.options(joinedload(Receitas.fotos))

        result = await sessao.execute(procura)
        receitas = result.unique().scalars().all()

        resposta = []
        for receita in receitas:
            fotos_da_receita = receita.fotos[0].foto if receita.fotos else None
            resposta.append({"id": receita.id, "titulo": receita.titulo, "instrucoes": receita.instrucoes, "fotos": fotos_da_receita})
        
        
    return {"categoria":categoria, "tag":tag}, resposta


@get_recipes.get("/busca_por_titulo")
async def busca_titulo(titulo: str = Query(..., title="Title to search")):
    async with async_session() as sessao:
        
        query = select(Receitas).where(Receitas.titulo.ilike(f"%{titulo}%"))
        query = query.options(joinedload(Receitas.fotos))

        result = await sessao.execute(query)
        busca = result.unique().scalars().all()
    
    base_url = "http://localhost:5000"
    resposta = []
    for receita in busca:
        fotos_da_receita = f"{base_url}/backend/{receita.fotos[0].foto}" if receita.fotos else None
        resposta.append({
            "id": receita.id,
            "titulo": receita.titulo,
            "instrucoes": receita.instrucoes,
            "fotos": fotos_da_receita
        })

    return {"Pesquisa": titulo}, resposta


@get_recipes.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = f"uploads/{image_name}"  # Adjust the path accordingly
    try:
        return FileResponse(path=image_path, media_type="image/png")
    except Exception as e:
        print(f"Error retrieving image: {e}")
        raise

@get_recipes.get("/get_all_receitas")
async def busca_titulo():
    async with async_session() as sessao:

        query = select(Receitas)
        query = query.options(joinedload(Receitas.fotos))

        result = await sessao.execute(query)

        busca = result.unique().scalars().all()

        resposta = []

        for receita in busca:
            foto_da_receita = receita.fotos[0].foto if receita.fotos else None
            resposta.append({
                "id": receita.id,
                "titulo": receita.titulo,
                "instrucoes": receita.instrucoes,
                "foto": foto_da_receita
            })
    
    return resposta


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