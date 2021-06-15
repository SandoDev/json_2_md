from os import name
from pydantic import BaseModel


class TestModel(BaseModel):
    marca: str
    modelo: str
    anio: int
    km: int
    otros: dict
    nueva: list
