## Anthony Dike - Due: Oct. 31, 2017
## CSCI-UA.0002-012
## Assignment 6: Part 6

import myfunctions
import random

#Testing '.myfunctions'
##x = myfunctions.check_answer(1,1,2,"+")
##
##print(x)

"""
This program does the following:

1) asks the user for the amount of problems wanted (only pos nums)
2) asks the user for a size of the numbers
3) generates a series of random addition and subtraction problems
4) prompts the user for an answer and check the answer
5) keeps track of correct question answered

"""

#PROGRAM START#

# boolean to pass while loop
proceed = False

# while loop to keep user until valid input
while proceed == False:
    # user input for number of problems
    problems = int(input("How many problems would you like to attempt? "))
    if problems <= 0:
        print("Invalid number, try again")
        print() #spacer
    else:
        proceed = True #breaks loop


# boolean to pass while loop
proceed2 = False

# while loop to keep user until valid input
while proceed2 == False:
    w = int(input("How wide do you want your digits to be? 5-10: "))
    if w < 5 or w > 20:
        print("Invalid width, try again")
        print() #spacer
    else:
        proceed2 = True #breaks loop

print("Here we go!")
print() #spacer

#keeps track of correct answers
correct = 0

#keeps track of problems generated
counter = problems

# once 'counter' reaches 0, program ends
while counter != 0:
    
    # decreases by 1 with each iteration
    counter -= 1
    
    # initializing variables
    firstNum = 0
    secondNum = 0
    operation  = ""

    print()
    print("What is...")
    print()

    # range allows for 
    for i in range(2):

        # generates random objects
        randNum = random.randint(0,9)
        randOp = random.randint(1,2)

        # occurs if the random number selected is 0
        if randNum == 0:
            if i == 0:
                firstNum += randNum
                myfunctions.number_0(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                 secondNum += randNum
                 myfunctions.number_0(w)

        # occurs if the random number selected is 1
        if randNum == 1:
            if i == 0:
                firstNum += randNum
                myfunctions.number_1(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_1(w)

        # occurs if the random number selected is 2
        if randNum == 2:
            if i == 0:
                firstNum += randNum
                myfunctions.number_2(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_2(w)

        # occurs if the random number selected is 3
        if randNum == 3:
            if i == 0:
                firstNum += randNum
                myfunctions.number_3(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_3(w)

        # occurs if the random number selected is 4
        if randNum == 4:
            if i == 0:
                firstNum += randNum
                myfunctions.number_4(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_4(w)

        # occurs if the random number selected is 5
        if randNum == 5:
            if i == 0:
                firstNum += randNum
                myfunctions.number_5(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_5(w)

        # occurs if the random number selected is 6
        if randNum == 6:
            if i == 0:
                firstNum += randNum
                myfunctions.number_6(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_6(w)

        # occurs if the random number selected is 7
        if randNum == 7:
            if i == 0:
                firstNum += randNum
                myfunctions.number_7(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_7(w)

        # occurs if the random number selected is 8
        if randNum == 8:
            if i == 0:
                firstNum += randNum
                myfunctions.number_8(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_8(w)


        # occurs if the random number selected is 9
        if randNum == 9:
            if i == 0:
                firstNum += randNum
                myfunctions.number_9(w)

                if randOp == 1:
                    print()
                    operation = "+"
                    myfunctions.plus(w)
                    print()
                else:
                    print()
                    print()
                    operation = "-"
                    myfunctions.minus(w)
                    print()
                    print()
                    
            elif i == 1:
                secondNum += randNum
                myfunctions.number_9(w)

    # user enters their answer
    answer = int(input("= "))

    # calls function from external module to validate user answer
    ans = myfunctions.check_answer(firstNum,secondNum,answer,operation)

    if ans == True:
        print("Correct!")
        correct += 1
    else:
        print("Sorry, that's not correct.")


print()

# tells user how many questions they got right
print("You got",correct,"out of",problems,"correct!")
