# blackjack

def play_blackjack():
    import time
    import random
    from art import logo, you_win

    # ----- variabelen -----
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # J, Q, K worden voorgesteld als 10

    def show_cards(d_hand, p_hand):
        if sum(d_hand) > 21 and 11 in d_hand:
            d_hand.remove(11)
            d_hand.append(1)
        if sum(p_hand) > 21 and 11 in p_hand:
            p_hand.remove(11)
            p_hand.append(1)
        # bij "n" beslissing bij speler en "n" bij dealer: toon kaarten en beslis wie winnaar is (of gelijkspel)
        print(f"dealer had {' en '.join(str(card) for card in d_hand)}, met een totaal van {sum(d_hand)}")           
        print(f"you had {' en '.join(str(card) for card in p_hand)}, met een totaal van {sum(p_hand)}")
        if sum(d_hand) == 21 and sum(p_hand) < 21:
            print("dealer wint")
        elif sum(d_hand) < 21 and sum(d_hand) > sum(p_hand):
            print("dealer wint")
        elif sum(p_hand) > 21 and sum(d_hand) > 21:
            print("BUST! niemand wint")
        elif sum(p_hand) > 21 and sum(d_hand) < 21:
            print("dealer wint!")
        elif sum(p_hand) == sum(d_hand):
            print("gelijkspel!")
        else:
            print(you_win)

    game_over = False
    # ----- begin scherm -----
    print(logo)

    while game_over == False:
        players_hand = []
        dealers_hand = []
        # begin deck computer (1 kaart zichtbaar ; andere kaart onzichtbaar)
        up_card = random.choice(cards)
        hole_card = random.choice(cards)
        dealers_hand.append(up_card)
        dealers_hand.append(hole_card)
        print(f"dealer heeft een {up_card} en een hole-card")
        # begin deck speler (beide zichtbaar)
        player_card_1 = random.choice(cards)
        player_card_2 = random.choice(cards)
        players_hand.append(player_card_1)
        players_hand.append(player_card_2)
        print(f"jij hebt een {player_card_1} en een {player_card_2}")
        # indien geen 21 bij speler: nog een kaart voor speler? y/n -> tot "n"
        while sum(players_hand) < 21:
            player_plays = input("nog een kaart? ")
            if player_plays == "y":
                players_hand.append(random.choice(cards))
                print(f"je trok een {players_hand[-1]}")
            else: 
                break
        # indien geen 21 bij dealer en indien stand dealer <17 : nog een kaart voor computer. Indien >=17 maar <21 neemt de computer een random y/n beslissing. Bij 21 voor dealer: "n" en volgende stap
        while sum(dealers_hand) < 17:
            dealers_hand.append(random.choice(cards))
        while sum(dealers_hand) > 17 and sum(dealers_hand) < 21:
            dealers_choices = ["continue", "stop"]
            dealers_choice = random.choice(dealers_choices)
            if dealers_choice == "continue":
                dealers_hand.append(random.choice(cards))
            else:
                break
                
        show_cards(dealers_hand, players_hand)

        game_over = True

while input("Blackjack spelen? (y/n) ") == "y":
    play_blackjack()