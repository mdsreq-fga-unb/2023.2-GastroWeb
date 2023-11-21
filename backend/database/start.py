from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import *

engine = create_engine("sqlite://", echo=True)

Base.metadata.create_all(engine)

with Session(engine) as s:
    feijoada = Receitas(
        titulo = "Feijoao",
        ingredientes = "Feijao e Alho",
        instrucoes = "Cozinhar o feijão"
    )

    peixe = Receitas(
        titulo = "peixe",
        ingredientes = "Peixe, cebola",
        instrucoes = "Cozinhar o peixe com cebola"
    )



    s.add_all([feijoada, peixe])

    s.commit()


stmt = select(Receitas).where(Receitas.titulo.in_(["Feijoao", "peixe"]))

for receita in s.scalars(stmt):
    print("Titulo:", receita.titulo)
    print("Ingredientes:", receita.ingredientes)
    print("Instrucoes:", receita.instrucoes)
    print("---")