from random import shuffle

# Creates a shuffled deck #
def create_deck():
    suits = ['\u2660', '\u2665', '\u2666', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    deck = []
    for i in ranks:
        for z in suits:
            deck.append(i+z)
    shuffle(deck)

    return deck

# Splits the deck between players #
def split_deck(nb_of_players):

    # Finds out the number of cards to remove #
    nb_of_cards_to_remove = len(deck) % nb_of_players
    
    # Remove the 'excess' number of cards #
    if nb_of_cards_to_remove != 0:
        for i in range(nb_of_cards_to_remove):
            del deck[i]
        
    nb_of_cards_per_person = len(deck)/nb_of_players
    nb_of_cards_per_person = int(nb_of_cards_per_person)


    # Splits the deck between the players #
    decks = [deck[i:i + nb_of_cards_per_person] for i in range(0, len(deck), nb_of_cards_per_person)]

    return decks

def remove_pairs():

    # Removes all the pairs from the decks #
    i, j, k = 0, 0 ,0
    while i < (len(decks)):
        while j < (len(decks[i])):
            copies = 0
            while k < (len(decks[i])):
                card_1 = decks[i][j]
                card_2 = decks[i][k]
                if card_1[:-1] == card_2[:-1]:
                    copies += 1
                if copies == 2:
                    decks[i].remove(decks[i][j])
                    decks[i].remove(decks[i][k-1])
                    k, j, copies = 0, 0, 0
                else:
                    k += 1
            j += 1
            k = 0
        i += 1
        j, k = 0, 0
    return decks

def turn_go_fish():
    
    # Makes every player play #
    i = 0
    while i < len(decks):
        print("\nPlayer ", i + 1, ", it is your turn.", sep="")
        ready = input("Press enter to begin.\n")
        if ready == "":

            # Takes the numbers of the player and his card #
            print("Here is your deck:\n", decks[i], sep="")
            player_input = int(input("\nFrom which player do you want to steal?\nPlayer number: "))
            player_nb = player_input - 1
            print("\nThis player has ", len(decks[player_nb]), " cards.\nWhich one do you want to steal?", sep="")
            steal_input = int(input("Card number: "))
            steal_nb = steal_input - 1
            print("\nYou stole a '", decks[player_nb][steal_nb], "' from player ", player_input, ".", sep="")

            # Appends the stolen card to the current player's deck and deletes it from the other player's deck #
            decks[i].append(decks[player_nb][steal_nb])
            decks[player_nb].remove(decks[player_nb][steal_nb])

            # Verifies if the stolen card makes a pair and deletes the pair if it does #
            for j in range(len(decks[i])-1):
                if decks[i][j][:-1] == decks[i][-1][:-1]:
                    print("\nCongratulations! You have a new pair: '", decks[i][j], "'", " and ", decks[i][-1], "'.", sep="")
                    decks[i].remove(decks[i][j])
                    decks[i].remove(decks[i][-1])
                    break
            print("Your deck is now:\n", decks[i], sep="")

            # 'Clears' the console #
            input("\nPress enter to clear the console.\n")
            for l in range(18):
                print("\n")
            
            # Deletes the deck if it is empty #
            if decks[i] == []:
                del decks[i]
                print("Le joueur ", i+1, " a perdu. T'es laid!", sep="")
                

            i += 1

    return decks

def turn():
    
    # Makes every player play #
    i = 0
    while i < len(decks):
        print("\nPlayer ", i + 1, ", it is your turn.", sep="")
        ready = input("Press enter to begin.\n")
        if ready == "":

            # Takes the numbers of the player and his card #
            print("Here is your deck:\n", decks[i], sep="")
            player_input = int(input("\nFrom which player do you want to steal?\nPlayer number: "))
            player_nb = player_input - 1
            print("\nThis player has ", len(decks[player_nb]), " cards.\nWhich one do you want to steal?", sep="")
            steal_input = int(input("Card number: "))
            steal_nb = steal_input - 1
            print("\nYou stole a '", decks[player_nb][steal_nb], "' from player ", player_input, ".", sep="")

            # Appends the stolen card to the current player's deck and deletes it from the other player's deck #
            decks[i].append(decks[player_nb][steal_nb])
            decks[player_nb].remove(decks[player_nb][steal_nb])

            # Verifies if the stolen card makes a pair and deletes the pair if it does #
            for j in range(len(decks[i])-1):
                if decks[i][j][:-1] == decks[i][-1][:-1]:
                    print("\nCongratulations! You have a new pair: '", decks[i][j], "'", " and ", decks[i][-1], "'.", sep="")
                    decks[i].remove(decks[i][j])
                    decks[i].remove(decks[i][-1])
                    break
            print("Your deck is now:\n", decks[i], sep="")

            # 'Clears' the console #
            input("\nPress enter to clear the console.\n")
            for l in range(18):
                print("\n")
            
            # Deletes the deck if it is empty #
            if decks[i] == []:
                del decks[i]
                print("Le joueur ", i+1, " a perdu. T'es laid!", sep="")
                

            i += 1

    return decks


deck = create_deck()


run = True
print("\n\nWelcome to the fake game of Go Fish!")
while run:
    rules = input("Do you want to have an explanation of the rules? (y/n): ")
    while run:
        if rules == "y":
            run = False

            # Explanation of the rules #
            print("\nThe goal of the game is to be the first player to finish his deck.")
            print("Every player starts with the same number of cards.\nEvery pairs that one player has gets discated.")
            print("\nAt the begining of his turn, the player decides from which other player he wants to steal.")
            print("He then decides which card he takes (whitout being able to see it, of course).")
            print("\nIf the new card the player stole forms a pair with one of the cards he had before, the pair gets removed.")
            input("\nPress enter when you are ready to start.\n")
            create_deck()
            nb_of_players = int(input("\n\n\nPlease enter a number of players: "))
            decks = split_deck(nb_of_players)
            decks = remove_pairs()
            while decks != []:
                turn()
        elif rules == "n":
            run = False
            create_deck()
            nb_of_players = int(input("Please enter a number of players: "))
            decks = split_deck(nb_of_players)
            decks = remove_pairs()
            while decks != []:
                turn()
        else:
            rules = input("Please make a selection between yes (y) and no (n): ")
