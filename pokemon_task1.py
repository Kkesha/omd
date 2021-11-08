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


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass', exp=60)
    train(bulbasaur)
    print(bulbasaur.exp)
