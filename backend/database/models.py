from typing import List, Optional
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    UniqueConstraint
)

from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship, backref, DeclarativeBase
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class Receitas(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    instrucoes = Column(Text, nullable=False)

    fotos = relationship("Fotos", back_populates="receita")


class Ingrediente(Base):
    __tablename__ = "ingrediente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_receitas = Column(Integer, ForeignKey("receitas.id"), nullable=False)

    receitas = relationship(
        "Receitas", backref=backref("ingredientes", cascade="all, delete-orphan")
    )

    ingrediente = Column(String(50), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "ingrediente", "id_receitas", name="u_ingrediente_receitas"
        ),
    )


class Fotos(Base):
    __tablename__ = "foto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    foto = Column(String, nullable=False)

    id_receita = Column(Integer, ForeignKey("receitas.id"))
    receita = relationship("Receitas", back_populates="fotos")



    