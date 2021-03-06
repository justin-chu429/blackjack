from deck import Deck
from hand import Hand
from gameplay import gameplay

# lavabear

print("Welcome! How many decks would you like to play with?")
#requested_decks = input("Number of decks: ")
#requested_players = input("Number of players: ")

try:
    # change to requested_decks
    deck = Deck(int(2))
    print("Shuffling the deck")
    print(" ")
    deck.create_deck()
    deck.shuffle_deck()

    player_hand_1 = Hand(False)
    #player_hand_2 = Hand(False)
    player_hands = [player_hand_1]
    dealer_hand = Hand(True)

    deck.init_deal(player_hands, dealer_hand)

    print("Player 1's Hand")
    player_hand_1.get_hand()
    print(" ")

    #print("Player 2's Hand")
    #player_hand_2.get_hand()
    #print(" ")

    print("Dealer shows")
    dealer_hand.get_dealer_hand()

    print(" ")
    print(" ")

    i = 0
    bust_count = 0
    split_hands = []
    #print(len(split_hands))
    gameplay(i, deck, player_hands, dealer_hand, bust_count, split_hands)

    print("Dealer's Hand")
    dealer_hand.get_hand()
    if bust_count != len(player_hands):
        while dealer_hand.get_value() < 17:
            deck.hit(dealer_hand)
            if dealer_hand.get_value() > 21:
                print("BUST")
            print("Dealer's Hand")
            dealer_hand.get_hand()


except:
    print("Please enter a number next time. Goodbye")