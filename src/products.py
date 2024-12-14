class Product:
    """Класс продукты"""

    name: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # Количество в наличии

    def __init__(self, name: str, description: str, price: float=0, quantity: int=0) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Категории продуктов"""

    name: str  # Название
    description: str  # Описание
    products: list  # Список товаров категории

    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:

        self.name = name
        self.description = description
        self.products = products if products else []

        Category._category_count += 1
        Category._product_count += len(self.products)

