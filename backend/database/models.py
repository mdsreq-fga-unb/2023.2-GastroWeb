from typing import List, Optional
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)

from sqlalchemy.orm import Mapped, declarative_base, DeclarativeBase, mapped_column

Base = declarative_base()

class Receitas(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, autoincrement=True)

    titulo = Column(String(100), nullable=False)
    ingredientes = Column(Text, nullable=False)
    instrucoes = Column(Text, nullable=False)

class Fotos(Base):
    __tablename__ = "fotos"

    id = Column(Integer, primary_key=True, autoincrement=True)

    path = Column(String, nullable=False)
