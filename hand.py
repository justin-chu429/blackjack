class Hand:
    def __init__(self, dealer):
        self.hand = []
        self.value = 0
        self.card_count = 0
        self.aces_count = 0
        self.dealer = dealer
        self.double = False

    def add_card(self, card):
        self.hand.append(card)

    def calc_hand(self):
        self.reset_counts()

        for card in self.hand:
            try:
                value = int(card.get_value())
                self.value += value
                self.card_count += 1
            except:
                value = card.get_value()

                if (value == "J") | (value == "Q") | (value == "K"):
                    actual_value = 10
                    self.value += actual_value
                    self.card_count += 1

                if value == "A":
                    actual_value = 11
                    self.value += actual_value
                    self.aces_count += 1
                    self.card_count += 1

        if self.aces_count != 0:
            if self.value > 21:
                for ace in range(self.aces_count):
                    self.value -= 10
                    self.aces_count -= 1
                    if self.value < 21:
                        break

    def get_hand(self):
        i = 0
        for card in self.hand:
            if i != len(self.hand) - 1:
                print(card.get_value() + " " + card.get_suit(), end =" ")
                i += 1
            else:
                print(card.get_value() + " " + card.get_suit())

    def get_dealer_hand(self):
        print(self.hand[1].get_value() + " " + self.hand[1].get_suit())

    def reset_counts(self):
        self.value = 0
        self.card_count = 0
        self.aces_count = 0

    def get_value(self):
        return self.value

    def can_split(self):
        return (self.card_count == 2) & (self.hand[0].get_value() == self.hand[1].get_value())

    def can_double(self):
        return self.card_count == 2

    def set_double(self, action):
        self.double = action

    def split(self, second_hand):
        split_card = self.hand[1]
        second_hand.add_card(split_card)
        self.hand.remove(split_card)
