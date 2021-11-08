from random import choice


class Pokemon:
    def __init__(self, name: str, poketype: str, exp: int = 50):
        self.name = name
        self.poketype = poketype
        self.exp = exp

    def inc_exp(self, inc_size: int):
        self.exp += inc_size


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


class Digimon(Pokemon):
    def __init__(self, name: str, exp: int = 100):
        self.name = name
        self.exp = exp

    def inc_exp(self, value: int):
        self.exp += value * 8


if __name__ == '__main__':
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)
