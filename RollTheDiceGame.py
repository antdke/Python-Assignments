## Anthony Dike - Due: Oct. 5, 2017
## CSCI-UA.0002-012
## Assignment 4: Program #1: Roll the Dice

"""
Assignment #4, Part 1
Anthony Dike (worked with Selin Gureralp)
"""

"""
This program does the following:

1) Prompts the user to input a number that is greater
than or equal to 3.
2) The program takes the number and creates two dice with
as many sides.
3) The program then rolls the dice until both roll the number
one: "snake eyes."
4) The program then displays the amount of tries it took to roll
"snake eyes,"the amount of times doubles has been rolled, and the
average roll for each die."

"""

# Program Start

import random

#use a while loop


# this remains false until the user inputs a valid input
proceed = False

# prompts the user to input the number of sides on the dice
while proceed == False:
    # user input
    sides = int(input("How many sides on your dice? "))
    # input can't be less than 3
    if (sides < 3): 
        print("Sorry, that's not a valid size value. Please choose a number that is more than or equal to 3")
    # input has to be a positive number
    elif (sides < 0):
        print("Sorry, that's not a valid size value. Please choose a positive number.")
    else:
        proceed = True
        
#spacer
print()

# initialize die variables
die1 = random.randint(1,sides)
die2 = random.randint(1,sides)
counter = 1

"""
#TEST:I wanna see if die1 and die2 become numbers
print(die1)
print(die2)
print(die1)
print(die2)
"""
print("Thanks! Here we go...")

#spacer
print()

# use a while loop to keep dice rolling until
# snake eyes (die1 and die2 equate to 1) are rolled

# initialize variables to be used in snakeEyes while loop
snakeEyes = False
doubles = 0
die1AvgCounter = 0
die2AvgCounter = 0

while snakeEyes == False:

    # this adds up the number in each die's roll
    # to be later divided by the counter to find
    # each die's average
    die1AvgCounter += die1
    die2AvgCounter += die2

    # this counts the number of times both dice rolled the same numbers
    if die1 == die2:
        doubles += 1

    # prints each roll of the dice        
    print(str(counter) + ". die number 1 is " + str(die1) + " and die number 2 is " + str(die2) + ".")

    #condition of snake eyes
    if die1 == 1 and die2 == 1:
        snakeEyes = True
        break
    
    else:
        # re-randomized the values of both dice
        die1 = random.randint(1,sides) 
        die2 = random.randint(1,sides) 
        counter += 1 #This works
        
#spacer
print()

# these print once "snake eyes" is achieved

# prints counter
print("You got snakes eyes! Finally! On try number " + str(counter) + "!")

# prints doubles amount
print("Along the way you rolled doubles " + str(doubles) + " times")

# prints the average amount of each die's roll
print("The average roll for die #1 was " + format(float(die1AvgCounter / counter), ".2f"))
print("The average roll for die #2 was " + format(float(die2AvgCounter / counter), ".2f"))


#DONE @ 6pm exactly 10/2 !!
