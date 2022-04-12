from hand import Hand


def gameplay(i, deck, player_hands, dealer_hand, bust_count, split_hands):
    LABELS = ["zero", "first", "second", "third", "fourth", "fifth"]

    for player in player_hands:
        label = 0
        if len(split_hands) == 0:
            i += 1
        else:
            label += 1
        playing = True
        while playing:
            try:
                if len(split_hands) != 0:
                    print("Player " + str(i) + "'s " + LABELS[label] + " hand:")
                    player.get_hand()
                    print("Type \"dealer\" to see the dealer's hand ")
                    decision = input("Hit (h), Stand (s), Double (d), Split (sp)? ")

                    print(" ")
                else:
                    print("Player " + str(i) + "'s hand:")
                    player.get_hand()
                    print("Type \"dealer\" to see the dealer's hand ")
                    decision = input("Hit (h), Stand (s), Double (d), Split (sp)? ")

                    print(" ")

                if decision == "h":
                    deck.hit(player)
                    if player.value > 21:
                        print("BUST")
                        playing = False
                        bust_count += 1
                elif decision == "s":
                    playing = False
                elif decision == "d":
                    if player.can_double():
                        deck.hit(player)
                        playing = False
                        player.set_double(True)
                        if player.value > 21:
                            print("BUST")
                            bust_count += 1
                    else:
                        raise ValueError("Illegal choice")
                elif decision == "sp":
                    if player.can_split():
                        second_hand = Hand(False)
                        player.split(second_hand)
                        split_hands.append(second_hand)
                        deck.hit(player)
                        deck.hit(second_hand)
                        temp_hand = [player, second_hand]
                        gameplay(i, deck, temp_hand, dealer_hand, bust_count, split_hands)
                        playing = False
                    else:
                        raise ValueError("Illegal choice")
                elif decision == "dealer":
                    print("Dealer shows")
                    dealer_hand.get_dealer_hand()
                else:
                    raise ValueError("Illegal choice")

                if decision != "sp":
                    print("Player " + str(i) + "'s hand:")
                    player.get_hand()
                    print(" ")

            except:
                print("Please choose a legal move")
                print(" ")
