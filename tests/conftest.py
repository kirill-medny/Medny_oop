import pytest

from src.products import Category, Product


@pytest.fixture()
def products_samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def category_phone() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        # ["product1", "product2", "product3"],
    )


@pytest.fixture()
def category_iphone() -> Category:
    return Category(
        "Айфоны",
        "Айфоны получения дополнительных функций для удобства жизни",
        # ["product5", "product4"]
    )


@pytest.fixture()
def category_phone_none_prod() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        # [],
    )


@pytest.fixture()
def category_ip() -> Category:
    return Category(
        "Айфоны",
        "Айфоны получения дополнительных функций для удобства жизни",
        # ["product5", "product4"]
    )


@pytest.fixture()
def products_none_price() -> Product:
    return Product(
        "Samsung",
        "256GB",
    )


@pytest.fixture()
def products_none() -> Product:
    return Product("", "")


@pytest.fixture()
def products_error() -> Product:
    return Product(123, "Description", 10.99, 5)  # type: ignore


@pytest.fixture
def products_apple() -> Product:
    """Фикстура для создания продукта Apple."""
    return Product("Apple Iphone 14", "256GB, Черный цвет, 12MP камера", 100000, 10)


@pytest.fixture
def category_electronics() -> Category:
    """Фикстура для создания категории Электроника."""
    return Category("Электроника", "Товары электроники")
