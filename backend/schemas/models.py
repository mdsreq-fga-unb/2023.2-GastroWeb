from pydantic import BaseModel

class StandartOutput(BaseModel):
    message: str

class ReceitaBasica(BaseModel):
    titulo: str
    instrucoes: str
    ingredientes: str

class BuscaTitulo(BaseModel):
    titulo: str