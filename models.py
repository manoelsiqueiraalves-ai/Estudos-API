from pydantic import BaseModel, validator
from typing import Optional


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def titulo_validator(cls, value):
        palavras = value.split()

        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras')

        if value != value.upper():
            raise ValueError('O título deve estar em letras maiúsculas')

        return value
