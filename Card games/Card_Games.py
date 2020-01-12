yes = True
while yes:

    # Prints the list of games the users can play #
    print("\nHello! Here is a list of the games you can play!")
    print("1: Go Fish     2: Fake Go Fish     3: Oui")        
    play = input("\nInput the number of the game you want to play: ")
    
    if play == "1":
        from Go_Fish.py import*

    elif play == "2":
        from Fake_Go_Fish.py import *
        
    else:
        play = input("Please select a choose a number from the list")
