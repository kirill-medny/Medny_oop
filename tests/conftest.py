import pytest

from src.lawn_grass_prod import LawnGrass
from src.products import Category, Product
from src.smartphone_prod import Smartphone


@pytest.fixture()
def products_samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


@pytest.fixture()
def category_phone() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " 
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture()
def category_iphone() -> Category:
    return Category("Айфоны", "Айфоны получения дополнительных функций для удобства жизни",
                    ["product5", "product4"])


@pytest.fixture()
def category_phone_none_prod() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " 
        "но и получения дополнительных функций для удобства жизни",
        [],
    )


@pytest.fixture()
def category_ip() -> Category:
    return Category("Айфоны", "Айфоны получения дополнительных функций для удобства жизни",
                    ["product5", "product4"])


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
    return Category("Электроника", "Товары электроники")  # type: ignore


@pytest.fixture
def smartphone_samsung() -> Smartphone:
    """Фикстура для проверки категории Smartphone"""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
        95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def lawngrass_grass() -> LawnGrass:
    """Фикстура для проверки категории LawnGrass"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")
