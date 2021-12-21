from random import randint
from typing import Callable


class Pizza:
    def __init__(self, name: str, size: str = 'L'):
        """Проверяем имя пиццы, размер по умолчанию L"""
        name = name.capitalize()
        if name not in ['Margherita', 'Pepperoni', 'Hawaiian']:
            raise ValueError(f'We have no pizza with name {name}')

        self.name = name
        self.size = size

        if name == 'Margherita':
            self.name += ' 🧀'
            self.recipe = dict.fromkeys([self.name], ['tomato sauce', 'mozzarella', 'tomatoes'])

        if name == 'Pepperoni':
            self.name += ' 🍕'
            self.recipe = dict.fromkeys([self.name], ['tomato sauce', 'mozzarella', 'pepperoni'])

        if name == 'Hawaiian':
            self.name += ' 🍍'
            self.recipe = dict.fromkeys([self.name], ['tomato sauce', 'mozzarella', 'chicken', 'pineapples'])

    def dict(self):
        """Возвращает рецепт в виде строки"""
        recipe = ''
        for name, ingredients in self.recipe.items():
            recipe = f'{name}: ' + ', '.join(ingredient for ingredient in ingredients)
        return recipe

    def __str__(self):
        return f'{self.name} ({self.size})'

    def __eq__(self, other):
        return self.name == other.name and self.size == other.size


def menu():
    """Выводит меню"""
    pizzas = [Pizza('Margherita'), Pizza('Pepperoni'), Pizza('Hawaiian')]
    for pizza in pizzas:
        print(f'- {pizza.dict()}')
    print('Размер пиццы: L или XL')


def order(pizza: str, size: str = 'L', delivery: bool = False):
    """Готовит и доставляет пиццу"""
    pizza_for_order = Pizza(pizza, size)
    print(pizza_for_order.__str__() + ':')
    if pizza_for_order.size == 'L':
        print('     🍳 Приготовили за 20 минут')
    else:
        print('     🍳 Приготовили за 25 минут')
    if delivery:
        print('     🚚 Доставили за 15 минут')


def log(text: str) -> Callable:
    """Функция-декоратор, которая выводит время ее выполнения"""
    def wrapper(func: Callable) -> Callable:
        def decorator(*args, **kwargs):
            for pizza in args:
                print(pizza, end=' ')
            print(text.format(randint(5, 30)))
            func(*args, **kwargs)
        return decorator
    return wrapper


@log(': 🍳 приготовили за {} мин!')
def bake(pizza: Pizza):
    """Готовит пиццу"""


@log(': 🛵 доставили за {} мин!')
def delivery(pizza: Pizza):
    """Доставляет пиццу"""


@log(': 🏠 забрали за {} мин!')
def pickup(pizza: Pizza):
    """Самовывоз"""


if __name__ == '__main__':
    pizza1 = Pizza('Margherita')
    pizza2 = Pizza('Pepperoni')
    pizza3 = Pizza('Margherita', 'XL')
    print(pizza1)
    print(pizza1.dict())
    print(pizza1 == pizza3)
    menu()
    order('Margherita')
    order('Hawaiian', 'XL', delivery=True)
    delivery(pizza1)
    bake(pizza2)
    pickup(pizza3)
