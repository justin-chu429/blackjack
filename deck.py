from card import Card
import random

SUITS = ["spades", "clubs", "hearts", "diamonds"]
VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#VALUES = ["2", "2"]

class Deck:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.all_cards = []

    def create_deck(self):
        for i in range(self.number_of_decks):
            for suit in SUITS:
                for value in VALUES:
                    card = Card(value, suit)
                    self.all_cards.append(card)

    def print_deck(self, max):
        i = 0
        for card in self.all_cards:
            print(card.get_value() + ' ' + card.get_suit())
            i += 1
            if i == max:
                break

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def init_deal(self, player_hands, dealer_hand):
        self.deal_player(player_hands)
        self.deal_dealer(dealer_hand)
        self.deal_player(player_hands)
        self.deal_dealer(dealer_hand)

        for player in player_hands:
            player.calc_hand()
        dealer_hand.calc_hand()

    def deal_player(self, player_hands):
        numb_of_hands = len(player_hands)

        for i in range(numb_of_hands):
            player_hands[i].add_card(self.all_cards[i])

        del self.all_cards[:numb_of_hands]

    def deal_dealer(self, dealer_hand):
        dealer_hand.add_card(self.all_cards[0])
        del self.all_cards[:1]

    def hit(self, hand):
        hand.add_card(self.all_cards[0])
        del self.all_cards[:1]

        hand.calc_hand()
