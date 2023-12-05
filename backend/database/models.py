from typing import List, Optional
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    UniqueConstraint,
    Enum
)

import enum

from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship, backref, DeclarativeBase
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class Receitas(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    instrucoes = Column(Text, nullable=False)



class Ingrediente(Base):
    __tablename__ = "ingrediente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_receitas = Column(Integer, ForeignKey("receitas.id"), nullable=False)

    receita = relationship(
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
    id_receita = Column(Integer, ForeignKey("receitas.id"), nullable=False)

    receita = relationship(
        "Receitas", backref=backref("fotos", cascade="all, delete-orphan")
    )

    foto = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "foto", "id_receita", name="u_foto_receitas"
        ),
    )
    


class CategoriasEnum(enum.Enum):
    CAFE_DA_MANHA = "Café da manhã"
    JANTAR = "Jantar"
    ALMOCO = "Almoço"
    DOCES = "Doces e Sobremesas"
    LANCHE = "Lanche"

class Categorias(Base):
    __tablename__= "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(Enum(CategoriasEnum), nullable=False)


class CategoriaEReceita(Base):
    __tablename__ = "categoriasereceitas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_receita= Column(Integer, ForeignKey("receitas.id"), nullable=False)
    id_categoria = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    receita = relationship(
        "Receitas", backref=backref("categoria_assoc", cascade="all, delete-orphan")
    )
    categoria = relationship(
        "Categorias", backref=backref("receita_assoc", cascade="all, delete-orphan")
    )

    __table_args__ = (
        UniqueConstraint(
            "id_receita", "id_categoria", name="u_receita_categoria"
        ),
    )


