from src.products import Product

class LawnGrass(Product):
    """Класс трава газанная в каткргории продукты"""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country:str, germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other) -> float:  # type: ignore
        """Магический метод для сложения продуктов категории смартфоны и возврата полной стоимости."""
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)  # type: ignore
        raise TypeError