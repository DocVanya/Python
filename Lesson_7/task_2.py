from abc import ABC, abstractmethod


class Clothes:

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Suit(Clothes):

    @property
    def consumption(self):
        return 2 * self.param + 0.3


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


coat = Coat(50)
suit = Suit(185)
print(coat + suit)
