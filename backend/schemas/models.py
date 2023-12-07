from pydantic import BaseModel
from typing import List, Optional
from fastapi import UploadFile, File
from enum import Enum

class StandartOutput(BaseModel):
    message: str


class Ingredientes(BaseModel):
    ingrediente: str

class Fotos(BaseModel):
    fotos: str

class ReceitaBasica(BaseModel):
    titulo: str
    instrucoes: str
    ingredientes: List[Ingredientes]

class BuscaTitulo(BaseModel):
    titulo: str

""" 
class CategoriasEnum(str, Enum):
    CAFE_DA_MANHA = "CAFE_DA_MANHA"
    JANTAR = "JANTAR"
    ALMOCO = "ALMOCO"
    DOCES = "DOCES"
    LANCHE = "LANCHE"



class TagsEnum(str, Enum):
    LACTOSE = "LACTOSE"
    OLEAGINOSAS = "OLEAGINOSAS"
    PORCO = "PORCO"
    CARNE = "CARNE"
    GLUTEN = "GLUTEN"
    FRUTOSDOMAR = "FRUTOSDOMAR"


class ReceitaPorJSON(BaseModel):
    titulo: str
    instrucoes: str
    Ingredientes: List[str]
    categorias: List[str]
    tags: List[str]
 """