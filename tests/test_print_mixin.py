from pytest import CaptureFixture

from src.lawn_grass_prod import LawnGrass
from src.products import Product
from src.smartphone_prod import Smartphone


def test_print_mixin(capsys: CaptureFixture[str]) -> None:
    Product("Apple Iphone 14", "256GB, Черный цвет, 12MP камера", 100000, 10)
    massage = capsys.readouterr()
    assert massage.out.strip() == "Product(Apple Iphone 14, 256GB, Черный цвет, 12MP камера, 100000, 10)"


def test_lawn_grass_prod(capsys: CaptureFixture[str]) -> None:
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
              "Россия", "7 дней", "Зеленый")
    massage = capsys.readouterr()
    assert massage.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
    # print(massage.out.strip())


def test_smartphone_prod(capsys: CaptureFixture[str]) -> None:
    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
        95.5, "S23 Ultra", 256, "Серый"
    )
    massage = capsys.readouterr()
    assert massage.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
