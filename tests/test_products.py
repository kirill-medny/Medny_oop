import pytest

from src.products import Category, Product


def test_init_products(products_samsung: Product) -> None:
    assert products_samsung.name == "Samsung Galaxy S23 Ultra"
    assert products_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert products_samsung.price == 180000
    assert products_samsung.quantity == 5


Category._category_count = 0  # Обнуляем счетчики для каждого теста
Category._product_count = 0


def test_init_category(category_phone: Category) -> None:

    assert category_phone.name == "Смартфоны"
    assert (
        category_phone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_phone.products == ["product1", "product2", "product3"]
    assert Category._category_count == 1
    assert Category._product_count == 3


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


def test_invalid_name_type() -> None:
    with pytest.raises(TypeError):
        Product(123, "Description", 10.99, 5) # type: ignore
        Category(123, "Description") # type: ignore


def test_invalid_description_type() -> None:
    with pytest.raises(TypeError):
        Product("Name", 123, 10.99, 5) # type: ignore
        Category("Name", 123) # type: ignore


def test_invalid_price_type() -> None:
    with pytest.raises(TypeError):
        Product("Name", "Description", "10", 5) # type: ignore


def test_invalid_quantity_products_type() -> None:
    with pytest.raises(TypeError):
        Product("Name", "Description", 10, "5") # type: ignore
        Category("Name", "Description", 123) # type: ignore


def test_negative_price() -> None:
    with pytest.raises(ValueError):
        Product("Name", "Description", -10.99, 5)


def test_negative_quantity() -> None:
    with pytest.raises(ValueError):
        Product("Name", "Description", 10.99, -5)
