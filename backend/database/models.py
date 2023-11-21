from typing import List, Optional
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    UniqueConstraint,
    DateTime,
)

from sqlalchemy.orm import Mapped, declarative_base, DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class Receitas(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, autoincrement=True)

    titulo = Column(String(100), nullable=False)
    ingredientes = Column(String(100), nullable=False)
    instrucoes = Column(String(100), nullable=False)
