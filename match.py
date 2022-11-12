def match_by_value(card1, card2):
    return card1 is not None and card2 is not None and card1.value == card2.value

def match_by_suit(card1, card2):
    return card1 is not None and card2 is not None and card1.suit == card2.suit

def match_by_suit_or_value(card1, card2):
    return match_by_suit(card1, card2) or match_by_value(card1, card2)
