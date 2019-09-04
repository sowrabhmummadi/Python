import random


class Player:

    def __init__(self, bankroll, is_dealer=False):
        self.bankroll = bankroll
        self.cards = []
        self.is_dealer = is_dealer

    def add_card(self, card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

    def is_dealer(self):
        return self.is_dealer;


class Card:
    def __init__(self, ctype, value, name=""):
        self.ctype = ctype
        self.value = value
        self.name = name

    def print_card(self):
        print(f'{self.ctype} : {self.value} : {self.name}')


class Deck:
    cards = []

    def __init__(self):
        self.fill_cards()
        self.shuffle_deck()

    def fill_cards(self):
        for card_type in ['Heart', 'Diamond', 'Spade', 'Club']:
            for card_value in range(2, 11):
                self.cards.append(Card(card_type, card_value))
            for card_name in ['Jack', 'Queens', 'King']:
                self.cards.append(Card(card_type, 10, card_name))
                self.cards.append(Card(card_type, 1, 'Ace'))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def print_deck(self):
        for card in self.cards:
            card.print_card()

    def get_card(self):
        return self.cards.pop()

    def get_length(self):
        return len(self.cards)


class BlackJack:

    def __init__(self):
        self.player = Player(100)
        self.dealer = Player(100, True)
        self.deck = Deck()

    def start(self):
        is_game_ended = False
        self.player.add_card(self.deck.get_card())
        self.dealer.add_card(self.deck.get_card())
        self.player.add_card(self.deck.get_card())
        self.dealer.add_card(self.deck.get_card())
        while not is_game_ended:
            self.print_cards()
            break

    def deal_initial_cards(self):
        Player.addCaself.deck.get_card()

    def print_cards(self):
        for p in [self.player, self.dealer]:
            if p.is_dealer
                print('Dealers cards: ', "")
            else:
                print('players cards: ', "")
            for card in p.get_cards():
                print(f'{card.print_card()} |', "")
            print('')


BlackJack().start()
