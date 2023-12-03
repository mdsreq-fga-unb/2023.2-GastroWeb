from fastapi import  APIRouter, Request, UploadFile, File, HTTPException, Query
from schemas.models import ReceitaBasica, BuscaTitulo, IdReceita
from database.connection import async_session
from database.models import Receitas, Fotos, Ingrediente
from sqlalchemy import select
import os
from typing import List

recipes = APIRouter()


@recipes.post("/receitas")
async def criar_receita( recipe:ReceitaBasica, request : Request ):

    ip = request.client.host


    async with async_session() as sessao:
        nova_receita = Receitas(
            titulo=recipe.titulo,
            instrucoes=recipe.instrucoes
        )
        sessao.add(nova_receita)
        for ingrediente in recipe.ingredientes:
                    sessao.add(
                        Ingrediente(
                            ingrediente=ingrediente.ingrediente,
                            receitas=nova_receita
                        )
                    )
                    
        await sessao.commit()
    return { "message" : "receita adicionada com sucesso!"}

@recipes.post("/foto")
async def postar_foto( file: UploadFile = File(...) ):

    async with async_session() as sessao:
        try:
            os.makedirs("uploads", exist_ok=True)
            file_path = os.path.join("uploads", file.filename)
            with open(file_path, "wb") as image_file:
                image_file.write(file.file.read())

            # Save the file path to the database
            new_photo = Fotos(
                path=file_path
                )

            sessao.add(new_photo)
            await sessao.commit()

            return {"message": "File uploaded successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@recipes.post("/fotos")
async def postar_fotos(id:int, files: List[UploadFile] = File(...)):

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
                    id_receita=id
                    )
                sessao.add(new_photo)

            await sessao.commit()

            return {"message": "Files uploaded successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@recipes.get("/getfotos")
async def read_photos():
    async with async_session() as session:
        # Assuming Fotos is your SQLAlchemy model
        result = await session.execute(select(Fotos))
        photos = result.scalars().all()

    # Now 'photos' contains the queried data
    return photos


@recipes.get("/getreceitas")
async def busca_titulo():
    async with async_session() as sessao:

        result = await sessao.execute(select(Receitas))
        busca = result.scalars().all()
    
    return busca

@recipes.get("/buscareceitas")
async def busca_titulo(titulo: str = Query(..., title="Title to search")):
    async with async_session() as sessao:
        
        query = select(Receitas).where(Receitas.titulo.ilike(f"%{titulo}%"))
        result = await sessao.execute(query)
        busca = result.scalars().all()

    return busca