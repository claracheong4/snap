import unittest

from snap import Snap
from match import *
from player import Player

class TestSnap(unittest.TestCase):
    def setUp(self):
        self.players = [Player('Player A'), Player('Player B')]

    def test_single_deck_value(self):
        snap = Snap(1, match_by_value, self.players)
        snap.simulate()

        self.assertEqual(snap.winners[0].cards, 26)

    def test_two_decks_suit(self):
        snap = Snap(2, match_by_suit, self.players)
        snap.simulate()

        self.assertEqual(snap.winners[0].cards, 72)

    def test_two_decks_suit_value(self):
        snap = Snap(2, match_by_suit_or_value, self.players)
        snap.simulate()

        self.assertEqual(snap.winners[0].cards, 56)

    def test_zero_decks_negative(self):
        with self.assertRaises(ValueError) as context:
            Snap(0, match_by_suit, self.players)
        self.assertEqual('Number of decks must be more than 1', str(context.exception))

    def test_zero_players_negative(self):
        with self.assertRaises(ValueError) as context:
            Snap(1, match_by_suit, [])
        self.assertEqual('Number of players must be more than 1', str(context.exception))

if __name__ == '__main__':
    unittest.main()