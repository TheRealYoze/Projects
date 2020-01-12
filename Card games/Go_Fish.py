from random import shuffle

# Creates a shuffled deck #
def create_draw_pile():
    suits = ['\u2660', '\u2665', '\u2666', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    draw_pile = []
    for i in ranks:
        for z in suits:
            draw_pile.append(i+z)
    shuffle(draw_pile)

    return draw_pile

# Creates the decks for the players #
def create_family_decks():
    family_decks = []
    for i in range(nb_of_players):
        family_decks.append([])
    return family_decks

# Splits the deck between players #
def split_deck(nb_of_players):

    # Determines the number of cards to give #
    nb_of_cards_to_give = 5*nb_of_players

    if nb_of_cards_to_give > len(draw_pile):
        draw_pile.extend(create_draw_pile())
        
    # Splits the deck between the players #
    decks = [draw_pile[i:i + 5] for i in range(0, nb_of_cards_to_give, 5)]

    # Removes the cards of the decks from the draw pile #
    for i in range(nb_of_cards_to_give):
        draw_pile.remove(draw_pile[0])

    return decks

def remove_four():

    # Removes all the quads from the decks #
    i, j, k = 0, 0 ,0
    while i < (len(decks)):
        while j < (len(decks[i])):
            to_remove = []
            while k < (len(decks[i])):
                card_1 = decks[i][j]
                card_2 = decks[i][k]
                if card_1[:-1] == card_2[:-1]:
                    to_remove.append(decks[i][k])
                if len(to_remove) == 4:
                    k, j = 0, 0
                    for card in range(4):
                        decks[i].remove(to_remove[0])
                        family_decks[i].append(to_remove[0])
                        to_remove.remove(to_remove[0])
                else:
                    k += 1
            j += 1
            k = 0
        i += 1
        j, k = 0, 0
    
    return decks


def turn():

    # Makes every player play #
    i = 0
    while i < len(decks):

        # If the player has no cards, it skips his turn #
        if decks[i] != []:
            print("\nPlayer ", i + 1, ", it is your turn.", sep="")
            input("Press enter to begin.")

            # Takes the input from the user #
            card_request = ""
            while card_request == "":
                print("\nHere is your deck:\n", decks[i], sep="")
                card_request = input(str("\nWhich card do you want to ask?\nType it here: ")).upper()

            same_card = False
            for check in range(len(decks[i])):
                if card_request == decks[i][check][:-1]:
                    same_card = True
                    break
            
            while not same_card:
                
                if type(card_request) == int:
                    if (2 > card_request or card_request > 10):
                        print("\nIf you want to type a number, make sure it is between 2 and 10.")
                        print("\nHere is your deck:\n", decks[i], sep="")
                        card_request = input(str("\nWhich card do you want to ask?\nType it here: ")).upper()
                        
                elif card_request.isdigit():
                    card_request = int(card_request)
                    if (2 > card_request or card_request > 10):
                        print("\nIf you want to type a number, make sure it is between 2 and 10.")
                        print("\nHere is your deck:\n", decks[i], sep="")
                        card_request = input(str("\nWhich card do you want to ask?\nType it here: ")).upper()
                    else:
                        print("\nYou have to have that card number if you want to ask it.")
                        print("\nHere is your deck:\n", decks[i], sep="")
                        card_request = input(str("\nWhich card do you want to ask?\nType it here: ")).upper()                      

                elif ('J' != card_request and 'Q' != card_request and 'K' != card_request and 'A' != card_request):
                    print("\nIf you want to type a letter, make sure you type either 'j', 'q', 'k' or 'a'.")
                    print("\nHere is your deck:\n", decks[i], sep="")
                    card_request = input(str("\nWhich card do you want to ask?\nType it here: ")).upper()

                else:
                    print("\nYou have to have that card letter if you want to ask it.")
                    print("\nHere is your deck:\n", decks[i], sep="")
                    card_request = input(str("\nWhich card do you want to ask?\nType it here: ")).upper()
                     
                for check in range(len(decks[i])):
                    if card_request == decks[i][check][:-1]:
                        same_card = True
                        break

            # Shows the number of cards each player has #
            print()
            for players in range(len(decks)):
                print("Player", players + 1, "has", len(decks[players]), "cards.")
            
            # Asks the user to who he wants to ask his card #
            print("\nWho do you want to ask for the card '", card_request, "'?", sep="")
            player_input = int(input("Player number: "))
            player_nb = player_input - 1

            # Determines if the targeted player has the wanted card #
            stolen_cards = []
            for wanted_card in decks[player_nb]:
                if card_request == wanted_card[:-1]:

                    # Appends the wanted cards to a list #
                    stolen_cards.append(wanted_card)

            # Removes the stolen cards from the player's hand #
            if len(stolen_cards) != 0:
                for j in range(len(stolen_cards)):
                    decks[player_nb].remove(stolen_cards[j])
            
            # Makes the user draw a card #
            if len(stolen_cards) == 0:
                print("\nSorry, this player doesn't not have any '", card_request, "'. Go Fish!", sep="")
                if draw_pile != []:
                    input("Press enter to draw a new card.\n")
                    print("You drew a'", draw_pile[0], "'.", sep="")

                    # Appends the new card to the player's deck#
                    decks[i].append(draw_pile[0])
                    
                    # Removes the stolen card from the draw pile #
                    draw_pile.remove(draw_pile[0])

                    # Calculates if the newly aquired card makes a family #
                    maybe_family = []
                    for card in decks[i]:
                        if decks[i][-1][:-1] == card[:-1]:
                            maybe_family.append(card)
                        if len(maybe_family) == 4:
                            print("Congratulations! You made a new family!")
                            for o in range(4):
                                print(maybe_family[o], end=" ")
                            
                            # Finds the specific cards and appends them to the family decks and removes them from the player's hand #
                            for family in maybe_family:
                                family_decks[i].append(family)
                                decks[i].remove(family)
                    
                    print("\n\nYour deck is now:\n", decks[i], sep="")

                    see_families = input("\nDo you want to see how many families each player has? (y/n): ")
                    if see_families == "y":
          
                        # Prints the number of families each player has #
                        print()
                        for t in range(len(family_decks)):
                            if len(family_decks[t]) != 0:
                                if len(family_decks[t])/4 == 1:
                                    print("Player", t+1, "has 1 family.")
                                else:
                                    print("Player", t+1, "has", len(family_decks[t])//4, "families.")
                            else:
                                print("Player", t+1, "has no families.")
                                
                # If there are no more cards in the draw pile #            
                else:
                    print("Sorry, there is no more cards in the draw pile.")
                    
                    see_families = input("\nDo you want to see how many families each player has? (y/n): ")
                    if see_families == "y":
          
                        # Prints the number of families each player has #
                        print()
                        for t in range(len(family_decks)):
                            if len(family_decks[t]) != 0:
                                if len(family_decks[t])/4 == 1:
                                    print("Player", t+1, "has 1 family.")
                                else:
                                    print("Player", t+1, "has", len(family_decks[t])//4, "families.")
                            else:
                                print("Player", t+1, "has no families.")
                    
            # Shows the aquired cards and deletes them from the player's hand #
            elif len(stolen_cards) == 1:
                print("\nThis player had a '", stolen_cards[0], "'!", sep="")

                # Adds the stolen cards to the deck #
                decks[i].extend(stolen_cards)
                
                # Calculates if the newly aquired card makes a family #
                maybe_family = []
                for card in decks[i]:
                    if decks[i][-1][:-1] == card[:-1]:
                        maybe_family.append(card)
                    if len(maybe_family) == 4:
                        print("\nCongratulations! You made a new family!")
                        for o in range(4):
                            print(maybe_family[o], end=" ")
                        
                        # Finds the specific cards and appends them to the family decks and removes them from the player's hand #
                        for family in maybe_family:
                            family_decks[i].append(family)
                            decks[i].remove(family)
                    
                print("\n\nYour deck is now:\n", decks[i], sep="")
                
                see_families = input("\nDo you want to see how many families each player has? (y/n): ")
                if see_families == "y":
      
                    # Prints the number of families each player has #
                    print()
                    for t in range(len(family_decks)):
                        if len(family_decks[t]) != 0:
                            if len(family_decks[t])/4 == 1:
                                print("Player", t+1, "has 1 family.")
                            else:
                                print("Player", t+1, "has", len(family_decks[t])//4, "families.")
                        else:
                            print("Player", t+1, "has no families.")

            # If the player had more than 1 card that was asked #    
            else:
                print("\nLucky you! This player had the folowing cards:")
                for j in stolen_cards:
                    print("'", j, "'", sep="", end=" ")
                print()
                # Adds the stolen cards to the deck #
                decks[i].extend(stolen_cards)
                
               # Calculates if the newly aquired card makes a family #
                maybe_family = []
                for card in decks[i]:
                    if decks[i][-1][:-1] == card[:-1]:
                        maybe_family.append(card)
                    if len(maybe_family) == 4:
                        print("\nCongratulations! You made a new family!")
                        for o in range(4):
                            print(maybe_family[o], end=" ")
                        
                        # Finds the specific cards and appends them to the family decks and removes them from the player's hand #
                        for family in maybe_family:
                            family_decks[i].append(family)
                            decks[i].remove(family)
                                
                print("\n\nYour deck is now:\n", decks[i], sep="")

                see_families = input("\nDo you want to see how many families each player has? (y/n): ")
                if see_families == "y":
      
                    # Prints the number of families each player has #
                    print()
                    for t in range(len(family_decks)):
                        if len(family_decks[t]) != 0:
                            if len(family_decks[t])/4 == 1:
                                print("Player", t+1, "has 1 family.")
                            else:
                                print("Player", t+1, "has", len(family_decks[t])//4, "families.")
                        else:
                            print("Player", t+1, "has no families.")
                
            # 'Clears' the console #
            input("\nPress enter to clear the console.\n")
            for l in range(18):
                print("\n")
            
            i += 1

        # If the player has no cards, it skips his turn #
        else:
            print("Sorry player ", i + 1, ", you don't have any cards left.")
            input("Press enter to continue\n")
            i += 1

    return decks


run = True
print("\nWelcome to the game of Go Fish!")
while run:
    rules = input("\nDo you want to have an explanation of the rules? (y/n): ")
    while run:
        if rules == "y":
            run = False

            # Explanation of the rules #
            input("\nWhen you are finished reading one rule, press enter to read the next one.\n")
            input("The goal of the game is to be the first player to finish with the most families.\n")
            input("Every player starts with with 5 cards.\nEvery family (4 cards of the same value) that one player has gets discated.\n")
            input("Don't panic! The game will keep track of your discarted families.\n")
            input("At the begining of his turn, the player decides which card he wants to ask.\nYou can only ask for a card value you already have!\n")
            input("The player then decides to which player he wants to ask that card.\n")
            input("If that second player has one or more cards of that value, he is forced to give all of his cards to the first player.\n")
            input("If the second player doesn't have any card that he was asked for, the first player has to draw a card from the draw pile.\n")
            input("If there are no more cards in the draw pile, the player doesn't do anyting.\n")
            input("If one player doesn't have any cards in his hand, he cannot play anymore.\n")
            input("As said in the begining, the player who finishes with the most families wins!\n")
            input("Are you ready to start?\n")
            draw_pile = create_draw_pile()
            nb_of_players = int(input("Please enter a number of players: "))
            decks = split_deck(nb_of_players)
            family_decks = create_family_decks()
            decks = remove_four()
            while decks != []:
                decks = turn()
        elif rules == "n":
            draw_pile = create_draw_pile()
            nb_of_players = int(input("\nPlease enter a number of players: "))
            decks = split_deck(nb_of_players)
            family_decks = create_family_decks()
            decks = remove_four()
            while decks != []:
                decks = turn()
        else:
            rules = input("Please make a selection between yes (y) and no (n): ")
