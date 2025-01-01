from unittest.mock import patch

import pytest

from src.smartphone_prod import Smartphone

def test_init_smartphone_products(smartphone_samsung: Smartphone) -> None:
    assert smartphone_samsung.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_samsung.price == 180000
    assert smartphone_samsung.quantity == 5
    assert smartphone_samsung.efficiency == 95.5
    assert smartphone_samsung.model == "S23 Ultra"
    assert smartphone_samsung.memory == 256
    assert smartphone_samsung.color == "Серый"

def test_invalid_smartphone_type() -> None:
    with pytest.raises(TypeError):
        Smartphone("Not a product")  # type: ignore
