from fastapi import  APIRouter, Request, UploadFile, File, HTTPException, Query, Form
from fastapi.responses import JSONResponse
from schemas.models import ReceitaBasica, Ingredientes
from database.connection import async_session
from database.models import Receitas, Fotos, Ingrediente, CategoriaEReceita, CategoriasEnum, Categorias, TagsEnum, Tags, TagsEReceita
from sqlalchemy import select, join
from sqlalchemy.orm import joinedload
import os
from typing import List
import json

recipes = APIRouter()


@recipes.post("/criar_receitas")
async def criar_receita( 
    titulo: str = Form(...),
    instrucoes: str = Form(...),
    ingredientes: List[str] = Form(...),
    files: List[UploadFile] = File(...),
    categorias: List[CategoriasEnum] = Form(...), # Entrada reestruturada!
    tags: List[TagsEnum] = Form(...)
):
    async with async_session() as sessao:
        try:
            nova_receita = Receitas(
                titulo=titulo,
                instrucoes=instrucoes
            )
          
            sessao.add(nova_receita)

            for ingrediente in ingredientes:
                novo_ingrediente = Ingrediente(
                    ingrediente=ingrediente,
                    receita=nova_receita
                )
                sessao.add(novo_ingrediente)


            for categoria_enum in categorias:
                categoria = await sessao.execute(select(Categorias).where(Categorias.categoria == categoria_enum))
                categoria = categoria.scalar_one_or_none()

                if categoria is None:
                    nova_categoria = Categorias(categoria=categoria_enum)
                    sessao.add(nova_categoria)
                    await sessao.commit()
                    await sessao.refresh(nova_categoria)
                    categoria_id = nova_categoria.id
                else:
                    categoria_id = categoria.id

                assoc_categoria_receita = CategoriaEReceita(id_receita=nova_receita.id, id_categoria=categoria_id)
                sessao.add(assoc_categoria_receita)

            for tags_enum in tags:
                tag = await sessao.execute(select(Tags).where(Tags.tag == tags_enum))
                tag = tag.scalar_one_or_none()

                if tag is None:
                    nova_tag = Tags(tag=tags_enum)
                    sessao.add(nova_tag)
                    await sessao.commit()
                    await sessao.refresh(nova_tag)
                    tag_id = nova_tag.id
                else:
                    tag_id = tag.id

                assoc_tag_receita = TagsEReceita(id_receita=nova_receita.id, id_tag=tag_id)
                sessao.add(assoc_tag_receita)
                  
            os.makedirs("uploads", exist_ok=True)

            file_paths = []

            for file in files:
                file_path = os.path.join("uploads", file.filename)
                with open(file_path, "wb") as image_file:
                    image_file.write(file.file.read())
                file_paths.append(file_path)

            for file_path in file_paths:
                nova_foto = Fotos(
                    foto=file_path,
                    receita=nova_receita
                    )
                sessao.add(nova_foto)
            
            
            await sessao.commit()
            return { "message" : "receita adicionada com sucesso!"}
        except Exception as e:
            return{"error": str(e)}

async def popula_bd():
    async with async_session() as sessao:
        if not (await sessao.execute(select(Categorias).limit(1))).first():
                for categoria_enum in CategoriasEnum:
                    categoria_db = Categorias(categoria=categoria_enum)
                    sessao.add(categoria_db)
        if not (await sessao.execute(select(Tags).limit(1))).first():
                for tag_enum in TagsEnum:
                    tag_db = Tags(tag=tag_enum)
                    sessao.add(tag_db)
                await sessao.commit() 



@recipes.get("/get_receita_por_id")
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

@recipes.post("/postar_fotos")
async def postar_fotos(id_receita:int, files: List[UploadFile] = File(...)):

    async with async_session() as sessao:
        try:
            os.makedirs("uploads", exist_ok=True)

            # Lista para armazenar os caminhos dos arquivos
            file_paths = []

            for file in files:
                file_path = os.path.join("uploads", file.filename)
                with open(file_path, "wb") as image_file:
                    image_file.write(file.file.read())
                file_paths.append(file_path)

            # Salvar os caminhos dos arquivos no banco de dados
            for file_path in file_paths:
                new_photo = Fotos(
                    foto=file_path,
                    id_receita=id_receita
                    )
                sessao.add(new_photo)

            await sessao.commit()

            return {"message": "Files uploaded successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@recipes.get("/get_all_fotos")
async def read_photos():
    async with async_session() as session:
        result = await session.execute(select(Fotos))
        photos = result.scalars().all()

    return photos


@recipes.get("/get_all_receitas")
async def busca_titulo():
    async with async_session() as sessao:

        result = await sessao.execute(select(Receitas))
        busca = result.scalars().all()
    
    return busca

@recipes.get("/busca_por_titulo")
async def busca_titulo(titulo: str = Query(..., title="Title to search")):
    async with async_session() as sessao:
        
        query = select(Receitas).where(Receitas.titulo.ilike(f"%{titulo}%"))
        result = await sessao.execute(query)
        busca = result.scalars().all()

    return busca



@recipes.get("/obter_fotos_por_receita")
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
        

@recipes.get("/listar_ingredientes")
async def listar_ingredientes(receita_id: int):
    async with async_session() as sessao:
        stmt = (
            select(Ingrediente)
            .join(Receitas)
            .filter(Receitas.id == receita_id)
        )
        result = await sessao.execute(stmt)
        ingredientes = result.scalars().all()

        return ingredientes
    