import db
import random
import print_to_side

# BlackJack
# 1. Welcome message
# 2. shuffle the deck
# 3. deal 2 cards to player and dealer with 1 card of dealer hidden.
# 4. if there is an A, check if player wants to keep it as a 1 or 11 everytime before asking for new card
# 5. player choices:
#     1. hit
#     2. Stay
#     3. Double (double the bet with only 1 card to draw next)
# 6. After the player stays or gets busted. The dealer plays.
# 7. he as to hit till he reaches 17, wins, or gets busted.
game_status = True
while game_status:

    print("Welcome to Blackjack")

    # 6 Decks = Shoe
    shoe = db.suits_mix * 6
    # shuffling the shoe
    random.shuffle(shoe)
    count = 0
    player_hand = []
    dealer_hand = []
    player_total = 0
    dealer_total = 0

    # dealing the hands form the shuffled shoe (6*deck of cards)
    print("Let us deal the card")
    player_hand.append(shoe[count])
    count += 1
    dealer_hand.append(shoe[count])
    count += 1
    player_hand.append(shoe[count])
    count += 1
    dealer_hand.append(shoe[count])
    count += 1

    def print_player_card(hand):
        print("Player Hand - ")
        player_hand_card_art = [db.return_card(c) for c in player_hand]
        print_to_side.side_to_side(player_hand_card_art)
        print()

    def print_dealer_card(hand):
        print("Dealer Hand- ")
        if dealer_total == 0:
            dealer_hand_card_art = [db.HIDDEN_CARD,
                                    db.return_card(dealer_hand[1])]
        else:
            dealer_hand_card_art = [db.return_card(c) for c in dealer_hand]
        print_to_side.side_to_side(dealer_hand_card_art)
        print()

    def calculate_player_total(hand):

        total = 0
        for i in hand:
            num = i[1]
            if num == "A":
                total += int(input("would you like to use it as a '1' or '11': "))
            elif num == "J" or num == "K" or num == "Q":
                total += 10
            else:
                total += int(num)
        return total

    def calculate_dealer_total(hand):
        total = 0
        a = 0
        for i in hand:
            num = i[1]
            if num == "A":
                total += 1
                a += 1
            elif num == "J" or num == "K" or num == "Q":
                total += 10
            else:
                total += int(num)
        for j in range(a):
            if total <= 11 and total >= 7:
                total += 10
        return total

    print_player_card(player_hand)
    print_dealer_card(dealer_hand)
    # calculate totals
    player_total = calculate_player_total(player_hand)
    dealer_total = calculate_dealer_total(dealer_hand)

    # play
    if player_total == 21 and dealer_total == 21:
        print("Can't believe you did not win this!! - it's a draw")
    elif player_total == 21:
        print("YOU GOT A BLACKJACK!!. You win - Hurray!!")
    elif dealer_total == 21:
        print("Dealer has a BLACKJACK!! Dealer Wins!!")
    else:
        # player playing
        while True:
            choice = input("would you want to 'h' - hit or 's' - stay: ")
            if choice == 'h':
                player_hand.append(shoe[count])
                count += 1

                print_player_card(player_hand)

                player_total = calculate_player_total(player_hand)
                # both player and dealer total will be shown later

                if player_total > 21:
                    print("oops, you got busted")
                    break
            else:
                print("you chose to stay your hand")
                break

        # Display dealer hidden hand
        print_dealer_card(dealer_hand)
        # dealer playing
        while True:
            if dealer_total < 17 or dealer_total < player_total:
                print("Dealer hits")

                dealer_hand.append(shoe[count])
                count += 1

                print_dealer_card(dealer_hand)
                dealer_total = calculate_dealer_total(dealer_hand)

            else:
                break

        print(f"Your total is {player_total}")
        print(f"Dealer total is {dealer_total}")
        if dealer_total > 21:
            print("dealer busted")
        elif dealer_total > player_total:
            print("Dealer wins,")
        else:
            print("You win!!")

        game_status = True if "y" == input(
            "would you want to continue with another game. 'y' for yes, 'n' for no: ") else False
