from fastapi import APIRouter
from sqlalchemy.future import select
from database.connection import async_session
from database.models import Receitas, Fotos, Ingrediente, CategoriaEReceita, TagsEReceita

delete_recipes = APIRouter(tags=["Delete"])

@delete_recipes.delete("/delete_receita_por_id/{receita_id}")
async def delete_receita_por_id(
    receita_id: int
):
    async with async_session() as sessao:
        
        receita = (
            await sessao.execute(
                select(Receitas).where(Receitas.id == receita_id)
            )
        ).scalar()

        if not receita:
            return {"message": "Receita não encontrada ou sem categoria."}

        await sessao.execute(
            CategoriaEReceita.delete().where(CategoriaEReceita.id_receita == receita_id)
        )
        await sessao.execute(
            TagsEReceita.delete().where(TagsEReceita.id_receita == receita_id)
        )
        await sessao.execute(
            Ingrediente.delete().where(Ingrediente.id_receitas == receita_id)
        )
        await sessao.execute(
            Fotos.delete().where(Fotos.id_receita == receita_id)
        )

        await sessao.execute(
            Receitas.delete().where(Receitas.id == receita_id)
        )

        await sessao.commit()

        return {"message": "Receita excluída com sucesso."}
