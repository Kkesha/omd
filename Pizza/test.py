import pytest
from pizza import Pizza


def test_name():
    with pytest.raises(ValueError):
        assert Pizza('Other_pizza')


def test_recipe():
    assert Pizza('Margherita').dict() == 'Margherita 🧀: tomato sauce, mozzarella, tomatoes'


def test_eq():
    pizza1 = Pizza('Margherita')
    pizza2 = Pizza('Margherita')
    assert (pizza1 == pizza2) == True
