from fastapi import APIRouter
from sqlalchemy.future import select
from database.connection import async_session
from database.models import Receitas, Fotos, Ingrediente, CategoriaEReceita, TagsEReceita
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

delete_recipes = APIRouter(tags=["Delete"])

@delete_recipes.delete("/delete_receita_por_id/{receita_id}")
async def delete_receita_por_id(
    receita_id: int
):
    async with async_session() as sessao:
        async with sessao.begin():
            try:
                receita = (
                    await sessao.execute(
                        select(Receitas).where(Receitas.id == receita_id)
                    )
                ).scalar()

                if not receita:
                    return {"message": "Receita não encontrada ou sem categoria."}

                # Corrigir a exclusão nas tabelas relacionadas
                await sessao.execute(delete(CategoriaEReceita).where(CategoriaEReceita.id_receita == receita_id))
                await sessao.execute(delete(TagsEReceita).where(TagsEReceita.id_receita == receita_id))
                await sessao.execute(delete(Ingrediente).where(Ingrediente.id_receitas == receita_id))
                await sessao.execute(delete(Fotos).where(Fotos.id_receita == receita_id))
                await sessao.execute(delete(Receitas).where(Receitas.id == receita_id))
            except NoResultFound:
                return {"message": "Receita não encontrada."}

    return {"message": "Receita excluída com sucesso."}
