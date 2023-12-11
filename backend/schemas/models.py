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

class User(BaseModel):
    username: str
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str