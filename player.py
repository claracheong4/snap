class Player(object):
    def __init__(self, name, cards=0):
        self.cards = cards
        self.name = name

    def add_cards(self, n):
        self.cards += n

    def __str__(self):
        return '({p.name}: {p.cards} cards)'.format(p=self)
