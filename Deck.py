import random

colors = ['heart', 'diamonds', 'spades', 'clubs']


class Card:
    def __init__(self, value, color):
        self._val = value
        self._color = color

    def print_card(self):
        print(str(self._val) + ", " + str(self._color))


class Deck:
    def __init__(self):
        self._deck = [Card(value, color) for value in range(1, 14) for color in colors]
        self.shuffle()

    def __getitem__(self, key):
        return self._deck[key]

    def shuffle(self):
        random.shuffle(self._deck)



