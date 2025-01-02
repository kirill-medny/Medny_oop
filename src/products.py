from typing import Any, Dict, List, Optional, Type

from src.base_item import BaseItem
from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс продукты"""

    name: str  # Название
    description: str  # Описание
    __price: float  # Цена
    quantity: int  # Количество в наличии

    def __init__(self, name: str, description: str, price: float = 0, quantity: int = 0) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        """
        Геттер для приватного атрибута цены.
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для приватного атрибута цены.

        Реализует проверку:
          в случае если цена равна или ниже нуля, выводите сообщение в консоль
          “Цена не должна быть нулевая или отрицательная”, при этом новую цену устанавливать не нужно.
          В случае если цена товара понижается, добавить логику подтверждения пользователем вручную через ввод
          y (значит yes) или n (значит no) для согласия понизить цену или для отмены действия соответственно.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            confirmation = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if confirmation.lower() == "y":
                self.__price = new_price
                print(f"Цена успешно понижена до {new_price}")
            else:
                print("Понижение цены отменено.")
        else:
            self.__price = new_price

    @classmethod
    def new_product(
        cls: Type["Product"], product_data: Dict[str, Any], existing_products: Optional[List["Product"]] = None
    ) -> "Product":
        """
        Создает объект Product из словаря, обрабатывая дубликаты и выбирая более высокую цену.

        :param product_data: Словарь с данными о продукте (name, description, price, quantity)
        :param existing_products: Список существующих продуктов, в котором нужно искать дубликаты
        :return: Созданный или обновленный объект Product
        """
        name = product_data.get("name") or ""
        description = product_data.get("description") or ""
        price = product_data.get("price", 0.0)
        quantity = product_data.get("quantity", 0)

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    # Товар с таким именем уже существует, обновляем его
                    product.quantity += quantity
                    product.price = max(product.price, price)  # type: ignore
                    return product
        # Товар не существует, создаем новый
        return cls(name, description, price, quantity)

    def __add__(self, other) -> float:  # type: ignore
        """Магический метод для сложения продуктов и возврата полной стоимости."""
        return (self.price * self.quantity) + (other.price * other.quantity)  # type: ignore


class Category(BaseItem):
    """Категории продуктов"""

    # name: str  # Название
    # description: str  # Описание
    __products: list  # Список товаров категории

    _category_count = 0

    def __init__(self, name: str, description: str, __products: list) -> None:

        # self.name = name
        # self.description = description
        super().__init__(name, description)
        self.__products = __products

        Category._category_count += 1

    @property
    def products(self) -> list:
        """
        Возвращает список товаров в виде строк в формате:
        "Название продукта, 80 руб. Остаток: 15 шт."
        """
        formatted_list = []
        for product in self.__products:
            formatted_list.append(f"{str(product)}")
        return formatted_list

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """
         Добавляет продукт в категорию
        :param product: объект продукта
        """
        if isinstance(product, Product):
            return self.__products.append(product)
        raise TypeError

    def get_product_count(self) -> int:
        """
        Возвращает количество продуктов в категории
        """
        return len(self.__products)
