import argparse
from match import *

def parse():
    parser = argparse.ArgumentParser(description="""
        Simulate a game of "Snap!" between 2 computer players using N decks of playing cards.
        Choose a matching condition:
        1. Value of the cards.
        2. Suit of the cards.
        3. Both the value and suit of the cards.""")
    parser.add_argument('-n', required=True, type=int)
    choices_arr = ['value', 'suit']
    parser.add_argument('--choice', nargs='+', required=True, choices=choices_arr, default=all)

    args = parser.parse_args()
    if args.choice == choices_arr:
        match_condition = match_by_suit_or_value
    elif args.choice[0] == choices_arr[0]:
        match_condition = match_by_value
    elif args.choice[0] == choices_arr[1]:
        match_condition = match_by_suit

    print("Game starts with {} deck and matching by {}\n".format(args.n, " and ".join(args.choice)))

    return args.n, match_condition