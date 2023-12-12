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
    titulo = Column(String(150), nullable=False)
    instrucoes = Column(Text, nullable=False)



class Ingrediente(Base):
    __tablename__ = "ingrediente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_receitas = Column(Integer, ForeignKey("receitas.id"), nullable=False)

    receita = relationship(
        "Receitas", backref=backref("ingredientes", cascade="all, delete-orphan", lazy="selectin")
    )

    ingrediente = Column(String(500), nullable=False)

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
        "Receitas", backref=backref("fotos", cascade="all, delete-orphan", lazy="selectin")
    )

    foto = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "foto", "id_receita", name="u_foto_receitas"
        ),
    )
    


class CategoriasEnum(enum.Enum):
    ENTRADA = "ENTRADA"
    PRATOPRINCIPAL = "PRATOPRINCIPAL"
    SOBREMESA = "SOBREMESA"
    EVENTOSFESTIVOS = "EVENTOSFESTIVOS"
    CAFE_DA_MANHA = "CAFE_DA_MANHA"
    BOLOS = "BOLOS"
    LANCHE = "LANCHE"



class TagsEnum(enum.Enum):
    LEITE = "LEITE"
    TRIGO = "TRIGO"
    FRANGO = "FRANGO"
    PEIXE = "PEIXE"
    QUEIJOS = "QUEIJOS"
    COGUMELOS = "COGUMELOS"
    OLEAGINOSAS = "OLEAGINOSAS"
    PORCO = "PORCO"
    CARNE = "CARNE"

class Tags(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(Enum(TagsEnum), nullable=False)

class TagsEReceita(Base):
    __tablename__ = "tagsereceitas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_receita = Column(Integer, ForeignKey("receitas.id"), nullable=True)
    id_tag = Column(Integer, ForeignKey("tag.id"), nullable=False)

    receita = relationship(
        "Receitas", backref=backref("tags_assoc", cascade="all, delete-orphan", lazy="selectin")
    )
    tags = relationship(
        "Tags", backref=backref("receita_assoc", cascade="all, delete-orphan", lazy="selectin")
    )

    __table_args__ = (
        UniqueConstraint(
            "id_receita", "id_tag", name="u_receita_tag"
        ),
    )



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
        "Receitas", backref=backref("categoria_assoc", cascade="all, delete-orphan", lazy="selectin")
    )
    categoria = relationship(
        "Categorias", backref=backref("receita_assoc", cascade="all, delete-orphan", lazy="selectin")
    )

    __table_args__ = (
        UniqueConstraint(
            "id_receita", "id_categoria", name="u_receita_categoria"
        ),
    )


