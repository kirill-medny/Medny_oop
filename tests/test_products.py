from unittest.mock import patch

import pytest

from src.products import Category, Product
from tests.conftest import products_samsung


def test_init_products(products_samsung: Product) -> None:
    assert products_samsung.name == "Samsung Galaxy S23 Ultra"
    assert products_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert products_samsung.price == 180000
    assert products_samsung.quantity == 5


def test_set_negative_price(products_samsung: Product) -> None:
    products_samsung.price = -100.0
    assert products_samsung.price == 180000


def test_set_zero_price(products_samsung: Product) -> None:
    products_samsung.price = 0
    assert products_samsung.price == 180000


def test_init_category(category_phone: Category) -> None:

    assert category_phone.name == "Смартфоны"
    assert (
        category_phone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category._category_count == 1


def test_category_creation_with_no_products(category_phone_none_prod: Category) -> None:
    assert category_phone_none_prod.name == "Смартфоны"
    assert (
        category_phone_none_prod.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_phone_none_prod.products == []


def test_init_products_none_price(products_none_price: Product) -> None:
    assert products_none_price.price == 0
    assert products_none_price.quantity == 0


def test_create_product_negative_price() -> None:
    with pytest.raises(ValueError):
        Product("Test Product", "Description", -100.0, 5)


def test_create_product_negative_quantity() -> None:
    with pytest.raises(ValueError):
        Product("Test Product", "Description", 100.0, -5)


def test_invalid_price_type() -> None:
    with pytest.raises(TypeError):
        Product("Name", "Description", "10", 5)  # type: ignore


def test_invalid_quantity_products_type() -> None:
    with pytest.raises(TypeError):
        Product("Name", "Description", 10, "5")  # type: ignore
        Category("Name", "Description", 123)  # type: ignore


def test_negative_price() -> None:
    with pytest.raises(ValueError):
        Product("Name", "Description", -10.99, 5)


def test_negative_quantity() -> None:
    with pytest.raises(ValueError):
        Product("Name", "Description", 10.99, -5)


def test_set_lower_price_with_confirm(products_samsung: Product) -> None:
    with patch("builtins.input", return_value="y"):
        products_samsung.price = 150000
        assert products_samsung.price == 150000


def test_set_lower_price_without_confirm(products_samsung: Product) -> None:
    with patch("builtins.input", return_value="n"):
        products_samsung.price = 150000
        assert products_samsung.price == 180000


def test_new_product_creation() -> None:
    product_data = {"name": "Test Product", "description": "Description", "price": 100.0, "quantity": 5}
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 5


def test_new_product_duplicate_update() -> None:
    product1 = Product("Test Product", "Description", 100.0, 5)
    product_data = {"name": "Test Product", "description": "New Description", "price": 120.0, "quantity": 10}
    product2 = Product.new_product(product_data, [product1])
    assert product2.price == 120.0
    assert product2.quantity == 15
    assert product1 is product2


def test_sum_full_cost(products_apple:Product, products_samsung:Product) -> None:
    assert products_apple + products_samsung == 1900000

def test_str_product(products_apple:Product) -> None:
    assert str(products_apple) == "Apple Iphone 14, 100000 руб. Остаток: 10 шт."

def test_str_category(category_iphone:Category) ->None:
    assert str(category_iphone) == "Айфоны, количество продуктов: 2 шт."

