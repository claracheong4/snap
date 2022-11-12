from randomizer import randomizer
from collections import namedtuple

class Card(namedtuple('Card', 'suit value')):
    suits = ['Spade', 'Heart', 'Diamond', 'Club']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __str__(self):
        return '({card.suit} {card.value})'.format(card=self)

class Deck(object):
    def __init__(self, n):
        self.cards = [Card(value, suit) for value in Card.values for suit in Card.suits for _ in range(n)]

    def __add__(self, other):
        return self.__class__(self.cards + other.cards)

    def shuffle(self):
        randomizer.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def __nonzero__(self):
        return bool(self.cards)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)