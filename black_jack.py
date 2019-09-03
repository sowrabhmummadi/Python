import random


class Deck:
    cards = []

    def __init__(self):
        self.fill_cards()
        self.shuffel_deck()

    def fill_cards(self):
        [[self.cards.append(f"{card_type} : {card_value}") for card_value in range(1, 13)] for
         card_type in ['Heart', 'Diamond', 'Spade', 'Club']]

    def shuffel_deck(self):
        random.shuffle(self.cards)

    def print_deck(self):
        print(self.cards)

    class Card:

        def __init__(self, name, value):
            self.name = name
            self.value = value


Deck().print_deck()
