from base_item import BaseItem
from src.products import Product


class Order(BaseItem):
    """Класс Заказ"""

    product: Product
    quantity: int

    def __init__(self, product: Product, quantity: int) -> None:
        super().__init__(product.name, product.description)
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        self.product = product
        self.quantity = quantity

    @property
    def total_cost(self) -> float:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"Заказ: {self.name}, Количество: {self.quantity}, Итого: {self.total_cost} руб."
