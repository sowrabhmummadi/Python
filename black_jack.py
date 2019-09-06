import random

blackjack_limit = 21


class Player:

    def __init__(self, bankroll, is_dealer=False):
        self.bankroll = bankroll
        self.cards = []
        self.is_dealer = is_dealer

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        if self.is_dealer:
            return "Dealer"
        else:
            return "Player"

    def get_hand_value(self):
        non_ace_cards = list(filter(lambda card: card.get_name() != 'Ace', self.cards))
        no_of_non_ace_cards = len(self.cards) - len(non_ace_cards)
        sum_of_cards = sum(map(lambda x: x.get_value(), non_ace_cards))
        while no_of_non_ace_cards > 0:
            if sum_of_cards + 10 < 21:
                sum_of_cards += 10
            else:
                sum_of_cards += 1
            no_of_non_ace_cards -= 1
        return sum_of_cards

    def print_cards(self):
        if self.is_dealer:
            first_card = self.cards[0]
            print(f'{self} cards(sum: {first_card.get_value()}+): ', end="")
            first_card.print_card()
            for _ in self.cards[1::]:
                print('-------', end=", ")
        else:
            print(f'{self} cards(sum: {self.get_hand_value()}): ', end="")
            for card in self.cards:
                card.print_card()
        print('')

    def print_full_cards(self):
        print(f'{self} cards(sum: {self.get_hand_value()}): ', end="")
        for card in self.cards:
            card.print_card()
        print('')


class Card:
    def __init__(self, ctype, value, name=""):
        self.ctype = ctype
        self.value = value
        self.name = name

    def print_card(self):
        if self.name == "":
            return print(f'{self.value} of {self.ctype}', end=", ")
        else:
            return print(f'{self.name} of {self.ctype}', end=", ")

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name


class Deck:
    cards = []

    def __init__(self):
        self.fill_cards()
        self.shuffle_deck()

    def fill_cards(self):
        for card_type in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
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

    def deal_card(self):
        return self.cards.pop()

    def get_length(self):
        return len(self.cards)


class BlackJack:

    def __init__(self):
        self.player = Player(100)
        self.dealer = Player(100, True)
        self.deck = Deck()

    def start_game(self):
        # bet = input(f"please specify your bet(Balance:{self.player.get_bank_roll()}):")
        self.deal_initial_cards()

        self.player.print_cards()
        self.dealer.print_cards()
        # players turn
        is_game_over, player_hand_sum = self.players_turn()
        if not is_game_over:
            is_game_over, dealer_hand_sum = self.dealers_turn(player_hand_sum)
        if not is_game_over:
            self.provide_verdict(dealer_hand_sum, player_hand_sum)

    def provide_verdict(self, dealer_hand_sum, player_hand_sum):
        self.print_full_cards()
        if player_hand_sum > dealer_hand_sum:
            print("~$$$$ player won $$$$~")
        elif dealer_hand_sum > player_hand_sum:
            print("~$$$$ players loose $$$$~")
        else:
            print("~$$$$ Tied $$$$~")

    def dealers_turn(self, player_hand_sum):
        is_game_over = False
        print("Dealers turn")
        while True:
            dealer_hand_sum = self.dealer.get_hand_value()
            if dealer_hand_sum > player_hand_sum or dealer_hand_sum > 17:
                break
            self.hit(self.dealer)
        if dealer_hand_sum > blackjack_limit:
            self.print_full_cards()
            print("~$$$$ dealer bust ~$$$$")
            is_game_over = True
        return is_game_over, self.dealer.get_hand_value()

    def players_turn(self):
        is_game_over = False
        while True:
            print("1.Hit 2.Stand")
            option = input("Choose your option: ")
            if option == '1':
                self.hit(self.player)
                player_hand_sum = self.player.get_hand_value()
                if player_hand_sum > blackjack_limit:
                    self.print_full_cards()
                    print("~$$$$ player bust $$$$~")
                    is_game_over = True
                    break
                else:
                    self.player.print_cards()
                    self.dealer.print_cards()

            elif option == '2':
                print("player stands...")
                break
            else:
                print("please choose a valid option..")
        return is_game_over, self.player.get_hand_value()

    def deal_initial_cards(self):
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def hit(self, player):
        print(f"{player} choose to Hit")
        player.add_card(self.deck.deal_card())

    def print_full_cards(self):
        self.player.print_full_cards()
        self.dealer.print_full_cards()

    def stand(self, player):
        print(f"{player} choose to Stand")


def start_game():
    print("welcome to simplified Black jack")
    while True:
        BlackJack().start_game()
        user_input = input("\n Do you want to play another game (y)")
        if user_input.lower() == 'y':
            BlackJack().start_game()
        else:
            print("Thank you for your time")
            break


start_game()
