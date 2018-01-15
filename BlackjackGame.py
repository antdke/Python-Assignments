# Anthony Dike - Due: Nov. 28, 2017
## CSCI-UA.0002-012
## Assignment 8: Part 2

#The program allows the user to play BlackJack against the computer.

import random

cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts',
          '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts',
          'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds',
          '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds',
          '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds',
          'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs',
          '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs',
          'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades',
          '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades',
          '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10,
          10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

# PLAYER and COMPUTER starts with no cards
player = []
computer = []

"""
Important realization: I have to extract the card value from it
BEFORE i remove the card from the deck.
"""

# PLAYER is dealt two cards
player.append(random.choice(cards))
player.append(random.choice(cards))


# PLAYER is dealt two cards
computer.append(random.choice(cards))
computer.append(random.choice(cards))



# PLAYER and COMPUTER also obtain values of those random cards in a diff list
location = ""
player_values = []
computer_values = []

location = cards.index(player[0])
player_values.append(values[location])
print(player_values) #test

location = cards.index(player[1])
player_values.append(values[location])
print(player_values) #test

location = cards.index(computer[0])
computer_values.append(values[location])
print(computer_values) #test

location = cards.index(computer[1])
computer_values.append(values[location])
print(computer_values) #test

# the two player cards have to be removed
cards.remove(player[0])
if player[0] in cards:
    print("IT's STILL HERE!")
else:
    print("YOU GOT RID OF IT")
cards.remove(player[1])
print(player) #test

# the two computer cards have to be removed
cards.remove(computer[0])
cards.remove(computer[1])
print(computer) #test

# start gane

# calc of player values 
player_total = 0
for num in player_values:
    player_total += num

# calc of computer values 
computer_total = 0
for num in computer_values:
    computer_total += num


# boolean keys
no_winner = True
computer_turn = False
    # This has to repeat so should all be in a while loop

while no_winner == True:
    print("Player hand:",player,"is worth",str(player_total))

    # hit or stand
    hitOrStand = input("(h)it or (s)tand? ")

    # if player decides to 'hit', its player's turn
    if hitOrStand == "h":
        # player gets a random card appended to deck
        player.append(random.choice(cards))
        # the card value has to be appended also
        player_total += values[cards.index(player[-1])]
        # the random card is printed
        print("You drew",player[-1]) # index at [-1] will always be the last item
        # remove picked card from the deck
        cards.remove(player[-1])
        continue # restart loop

    # if player decides to 'stand', its computer/dealer's turn
    elif hitOrStand == "s":
        computer_turn = True

        while computer_turn == True:
            print("Computer hand:",computer,"is worth",str(computer_total))
            
            # Computer gets a random card appended to deck
            computer.append(random.choice(cards))
            # the card value has to be appended also
            computer_total += values[cards.index(computer[-1])]
            # the random card is printed
            print("Computer drew",computer[-1]) # index at [-1] will always be the last item
            # remove picked card from the deck
            cards.remove(computer[-1])
            continue # restart loop
