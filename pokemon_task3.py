from abc import ABC, abstractmethod
from random import choice


class AnimeMon(ABC):
    @property
    @abstractmethod
    def exp(self):
        pass

    @exp.setter
    @abstractmethod
    def exp(self, val):
        pass

    @classmethod
    @abstractmethod
    def inc_exp(self):
        pass


class Pokemon(AnimeMon):
    def __init__(self, name: str, poketype: str, exp: int = 50):
        self.name = name
        self.poketype = poketype
        self._exp = exp

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, val):
        self._exp = val

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

    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass', exp=60)
    train(bulbasaur)
    print(bulbasaur.exp)

    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)
