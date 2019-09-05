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

    def is_dealers(self):
        return self.is_dealer

    def get_bank_roll(self):
        return self.bankroll

    def get_name(self):
        if self.is_dealer:
            return "Dealer"
        else:
            return "Player"

    def get_hand_value(self):
        return sum(map(lambda x: x.get_value(), self.cards))


class Card:
    def __init__(self, ctype, value, name=""):
        self.ctype = ctype
        self.value = value
        self.name = name

    def print_card(self):
        return f'{self.value} : {self.ctype} : {self.name}'

    def get_value(self):
        return self.value


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
            # self.cards.append(Card(card_type, 1, 'Ace'))

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
        # bet = input(f"please specify your bet(Balance:{self.player.get_bank_roll()}):")
        self.player.add_card(self.deck.get_card())
        self.dealer.add_card(self.deck.get_card())
        self.player.add_card(self.deck.get_card())
        self.dealer.add_card(self.deck.get_card())
        is_game_over = False

        # players turn
        while True:
            player_hand_sum = self.player.get_hand_value()
            if player_hand_sum > 21:
                self.print_cards()
                print("~$$$$ player bust $$$$~")
                is_game_over = True
                break
            self.print_cards()
            print("1.Hit 2.Stand")
            option = input("Choose your option: ")
            if option == '1':
                self.hit(self.player)
            else:
                print("player stands...")
                break

        if not is_game_over:
            print("Dealers turn")
            while True:
                dealer_hand_sum = self.dealer.get_hand_value()
                if dealer_hand_sum > player_hand_sum or dealer_hand_sum > 17:
                    break
                self.hit(self.dealer)
            self.print_cards()
            if dealer_hand_sum > 21:
                print("~$$$$ dealer bust ~$$$$")
            elif player_hand_sum > dealer_hand_sum:
                print("~$$$$ player won ~$$$$")
            elif dealer_hand_sum > player_hand_sum:
                print("~$$$$ players loose ~$$$$")
            else:
                print("~$$$$ Tied ~$$$$")

    def print_cards(self):
        for p in [self.player, self.dealer]:
            if p.is_dealers():
                print(f'Dealers cards(sum: {p.get_hand_value()}): ', end="")
            else:
                print(f'players cards(sum: {p.get_hand_value()}): ', end="")
            for card in p.get_cards():
                print(f'{card.print_card()} |', end="")
            print('')

    def hit(self, player):
        print(f"{player.get_name()} choose to Hit")
        player.add_card(self.deck.get_card())

    def stand(self, player):
        print(f"{player.get_name()} choose to Stand")


BlackJack().start()
