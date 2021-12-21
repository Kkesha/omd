import click
from pizza import Pizza


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Выводит меню"""
    pizzas = [Pizza('Margherita'), Pizza('Pepperoni'), Pizza('Hawaiian')]
    for pizza in pizzas:
        print(f'- {pizza.dict()}')
    print('Размер пиццы: L или XL')


@cli.command()
@click.argument('pizza')
@click.argument('size', default='L')
@click.option('--delivery', is_flag=True, default=False)
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza_for_order = Pizza(pizza, size)
    print(pizza_for_order.__str__() + ':')
    if pizza_for_order.size == 'L':
        print('     🍳 Приготовили за 20 минут')
    else:
        print('     🍳 Приготовили за 25 минут')
    if delivery:
        print('     🚚 Доставили за 15 минут')


if __name__ == '__main__':
    cli()
