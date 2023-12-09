from fastapi import APIRouter, Form, File, UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.connection import async_session
from database.models import Receitas, Fotos, Ingrediente, CategoriaEReceita, TagsEReceita, Categorias, CategoriasEnum, Tags, TagsEnum
from fastapi import APIRouter, HTTPException
import os
from typing import List

update_recipes = APIRouter(tags=["Put"])

@update_recipes.put("/update_receita_por_id/{receita_id}")
async def update_receita_por_id(
    receita_id: int,
    titulo: str = Form(...),
    instrucoes: str = Form(...),
    ingredientes: List[str] = Form(...),
    files: List[UploadFile] = File(...),
    categorias: List[str] = Form(...),
    tags: List[str] = Form(...)
):
    async with async_session() as sessao:
        receita = (
            await sessao.execute(
                select(Receitas).where(Receitas.id == receita_id)
            )
        ).scalar()

        if not receita:
            raise HTTPException(status_code=404, detail="Receita não encontrada.")

        receita.titulo = titulo
        receita.instrucoes = instrucoes

        await sessao.execute(
            Ingrediente.delete().where(Ingrediente.id_receitas == receita_id)
        )

        for ingrediente in ingredientes:
            novo_ingrediente = Ingrediente(
                ingrediente=ingrediente,
                receita=receita
            )
            sessao.add(novo_ingrediente)

        await sessao.execute(
            CategoriaEReceita.delete().where(CategoriaEReceita.id_receita == receita_id)
        )
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

            assoc_categoria_receita = CategoriaEReceita(id_receita=receita_id, id_categoria=categoria_id)
            sessao.add(assoc_categoria_receita)

        await sessao.execute(
            TagsEReceita.delete().where(TagsEReceita.id_receita == receita_id)
        )
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

            assoc_tag_receita = TagsEReceita(id_receita=receita_id, id_tag=tag_id)
            sessao.add(assoc_tag_receita)

        os.makedirs("uploads", exist_ok=True)
        file_paths = []

        await sessao.execute(
            Fotos.delete().where(Fotos.id_receita == receita_id)
        )

        for file in files:
            file_path = os.path.join("uploads", file.filename)
            with open(file_path, "wb") as image_file:
                image_file.write(file.file.read())
            file_paths.append(file_path)

        for file_path in file_paths:
            nova_foto = Fotos(
                foto=file_path,
                receita=receita
            )
            sessao.add(nova_foto)

        await sessao.commit()

        return {"message": "Receita atualizada com sucesso."}
