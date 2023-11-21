from pydantic import BaseModel

class StandartOutput(BaseModel):
    message: str

class ReceitaBasica(BaseModel):
    titulo: str
    instrucoes: str
    ingredientes: list

