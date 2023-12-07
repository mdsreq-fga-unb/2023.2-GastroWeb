from fastapi import  APIRouter, UploadFile, File, HTTPException, Form
from schemas.models import ReceitaBasica, Ingredientes
from database.connection import async_session
from database.models import Receitas, Fotos, Ingrediente, CategoriaEReceita, CategoriasEnum, Categorias, TagsEnum, Tags, TagsEReceita
from sqlalchemy import select
import os
from typing import List

recipes = APIRouter(tags=["post"])


@recipes.post("/criar_receitas")
async def criar_receita( 
    titulo: str = Form(...),
    instrucoes: str = Form(...),
    ingredientes: List[str] = Form(...),
    files: List[UploadFile] = File(...),
    categorias: List[str] = Form(...), # Entrada reestruturada!
    tags: List[str] = Form(...)
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

