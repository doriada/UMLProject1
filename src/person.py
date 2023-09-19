from abc import ABC
from typing import List

class person(ABC):

    def __init__(self, nombre: str, cedula: int) -> None:
        self._nombre = nombre
        self._cedula = cedula

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._cedula}, {self._nombre!r})'
    

class Autor(person):
    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__libros: List["Libro"] = []

class Gerente(person):
    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__editorial: "Editorial" = None

class Narrador(person):
    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__libros: List["Audiolibro"] = []
