from pydantic import BaseModel
from typing import List

class StandartOutput(BaseModel):
    message: str


class Ingredientes(BaseModel):
    ingrediente: str

class ReceitaBasica(BaseModel):
    titulo: str
    instrucoes: str
    ingredientes: List[Ingredientes]

class BuscaTitulo(BaseModel):
    titulo: str
