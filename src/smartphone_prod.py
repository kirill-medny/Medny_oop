from src.products import Product

class Smartphone(Product):
    """Класс смартфоны в категории продукты"""
    def __init__(self, name: str, description: str, price: float,
                 quantity: int , efficiency: float, model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency=efficiency
        self.model=model
        self.memory=memory
        self.color=color

    def __add__(self, other) -> float:  # type: ignore
        """Магический метод для сложения продуктов категории смартфоны и возврата полной стоимости."""
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)  # type: ignore
        raise TypeError



