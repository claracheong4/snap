import operator

from randomizer import randomizer
from parse import parse
from deck import *
from player import Player

class Snap(object):
    def __init__(self, n, match_condition, players):
        if n < 1:
            raise ValueError("Number of decks must be more than 1")
        if len(players) < 1:
            raise ValueError("Number of players must be more than 1")

        self.deck = Deck(n)
        self.match_condition = match_condition
        self.players = players
        self.prev_card = None
        self.pile = 0
        self.winners = None

    def __draw(self):
        card = self.deck.draw()
        self.pile += 1
        print(str(card) + " is drawn and added to pile")

        has_match = self.match_condition(card, self.prev_card)
        if has_match:
            print("Card matches!")
            player = randomizer.choice(self.players)
            print("{} shouted SNAP!".format(player))
            player.add_cards(self.pile)
            self.pile = 0

        self.prev_card = card

    def __end(self):
        print("\n--------------End of Game--------------")
        is_draw = all(p.cards == self.players[0].cards for p in self.players)
        if is_draw:
            print("The game ends with a draw!")
            self.winners = self.players
            pass

        winner = max(self.players, key=operator.attrgetter('cards'))
        print("The games end with {} as winner".format(winner))

        self.winners = [winner]

    def simulate(self):
        self.deck.shuffle()
        while self.deck:
            print("--------------Start of Turn--------------")
            print(self)
            self.__draw()
            print("--------------End of Turn--------------\n")

        self.__end()

    def __str__(self):
        return "Pile: {}\nDeck: {}\nPlayers: {}".format(self.pile, len(self.deck), ', '.join(str(p) for p in self.players))

if __name__ == '__main__':
    n, match_condition = parse()
    players = [Player('Player A'), Player('Player B')]
    snap = Snap(n, match_condition, players)
    snap.simulate()
