from abc import ABC, abstractmethod

class BaseItem(ABC):
    """Абстрактный класс для общих свойств Category и Order"""
    name: str
    description: str

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass