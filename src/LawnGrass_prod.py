from src.products import Product

class LawnGrass(Product):
    """Класс трава газанная в каткргории продукты"""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country:str, germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
