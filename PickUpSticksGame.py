## Anthony Dike - Due: Oct. 5, 2017
## CSCI-UA.0002-012
## Assignment 4: Program #2: Pick Up Sticks

"""
Assignment #4, Part 2
Anthony Dike (worked with Selin Gureralp)
"""

#NOTES
#start with input
#use a while loop to make sure user inputs number between 10 and 100
#begin the program with only Player 1 then add Player 2 after I finish main mechs of the game
#player can only pick up between 1 and 3 sticks, make sure that is so
#keep track of the amount of sticks on table AND make sure "sticksTaken" dont conflict with "sticksLeft"
#when "sticksLeft" == 0, then the Player that took the last stick loses AND the GAME ENDS
#create a variable to keep track of each Player's turn

"""
This program does the following:

1) The user is prompted to enter the number of sticks
on the table (10-100).

2) Then there will be two players that will take
1-3 sticks off of the table until there are none.

3) The player to take the last stick loses and the game ends.

"""

# Program Start

# this remains false until the user inputs a valid input
proceed = False

# user inputs the amount of sticks that will be on the table
while proceed == False:
    sticksLeft = int(input("How many sticks are on the table? (enter a number between 10 and 100): "))

    # makes sure user input is not less than 10 or greater than 100
    if sticksLeft < 10 or sticksLeft > 100:
        print("Invalid # of sticks, please try again.")
    else:
        proceed = True


# start of game

# initialize table empty
tableEmpty = False

# while the table is not eampty, the game will run
while tableEmpty == False:

    # Player 1's Turn
    
    print("There are " + str(sticksLeft) + " sticks on the table.") #prints sticks on table

    # this initializes turn to Player 1
    turn = "Player 1"
    print("Turn: ",turn)

    # Player 1 input of how many sticks he/she wants to take
    sticksTaken = int(input("How many sticks do you want to remove from the table? (1, 2 or 3): "))

    # player can't input a number less than 1 or greater than 3
    if sticksTaken < 1 or sticksTaken > 3:
        print("Invalid number of sticks, try again.")
        continue #restarts loop
    
    # player can't choose to take more sticks off the table then there are left
    elif sticksTaken > sticksLeft:
        print("You can't take that many sticks off of the table. Try again.")
        continue #restarts loop
    
    # this statement breaks the Player 1 loop, so the program can move onto Player 2
    elif sticksTaken <= sticksLeft:

        # keeps count of sticks being taken off the table
        sticksLeft = sticksLeft - sticksTaken

        if sticksLeft == 0: # once this is met, program ends
            print(turn,"loses!")
            break
        else:
            p1turn = False # ends player 1 turn

    
    # Player 2's turn
    
    while p1turn == False:
        
        print("There are " + str(sticksLeft) + " sticks on the table.") #prints sticks on table

        # this initializes turn to Player 2
        turn = "Player 2"
        print("Turn: ",turn)

        
        # Player 2 input of how many sticks he/she wants to take
        sticksTaken = int(input("How many sticks do you want to remove from the table? (1, 2 or 3): "))

        # player can't input a number less than 1 or greater than 3
        if sticksTaken < 1 or sticksTaken > 3:
            print("Invalid number of sticks, try again.")
            continue #restarts loop
    
        # player can't choose to take more sticks off the table then there are left
        elif sticksTaken > sticksLeft:
            print("You can't take that many sticks off of the table. Try again.")
            continue #restarts loop
    
        # this sends program back to Player 1 loop
        elif sticksTaken <= sticksLeft:

            # keeps count of sticks being taken off the table
            sticksLeft = sticksLeft - sticksTaken

            if sticksLeft == 0: # once this is met, program ends
                print(turn,"loses!")
                break
            else:
                p1turn = True # ends player 2 turn
                
    if sticksLeft == 0: #What's this for? Still works. *shrugs*
        break
                
    #IM DONEEEE (10/4 8:47 AM)
