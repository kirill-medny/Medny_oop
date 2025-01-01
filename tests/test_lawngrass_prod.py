from unittest.mock import patch

import pytest

from src.lawn_grass_prod import LawnGrass

def test_init_lawngrass_grass(lawngrass_grass: LawnGrass) -> None:
    assert lawngrass_grass.name == "Газонная трава"
    assert lawngrass_grass.description == "Элитная трава для газона"
    assert lawngrass_grass.price == 500.0
    assert lawngrass_grass.quantity == 20
    assert lawngrass_grass.country == "Россия"
    assert lawngrass_grass.germination_period == "7 дней"
    assert lawngrass_grass.color == "Зеленый"

