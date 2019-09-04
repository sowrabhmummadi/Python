import random


class Card:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def print_card(self):
        print('-----')
        print(f'|{self.name[0]}-{self.value}|')
        print('-----')


class Deck:
    cards = []

    def __init__(self):
        self.fill_cards()
        self.shuffle_deck()

    def fill_cards(self):
        [[self.cards.append(Card(card_type, card_value)) for card_value in range(1, 13)] for
         card_type in ['Heart', 'Diamond', 'Spade', 'Club']]

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def print_deck(self):
        for card in self.cards:
            card.print_card()

    def get_card(self):
        return self.cards.pop()

    def get_length(self):
        return len(self.cards)
