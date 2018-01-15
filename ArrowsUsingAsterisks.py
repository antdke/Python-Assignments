## Anthony Dike - Due: Oct. 5, 2017
## CSCI-UA.0002-012
## Assignment 4: Program #3: Arrows

"""
Assignment #4, Part 3
Anthony Dike (worked with Selin Gureralp)
"""

"""
This program does the following:
1) prompts the user to enter a positive number
2) program takes the number and produces arrows made of asterisks
"""

proceed = False

# while loop can be used for data validation (negative numbers)
while proceed == False:
    columns = int(input("How many columns? "))
    if columns < 0:
        print("Invalid entry, try again!")
    else:
        proceed = True

# counter used to determine the spaces that are printed with each asterisk
counter = 1

#first half of arrow

# asterisks are printed up until counter equates to the number inputted for columns
while counter != columns:
    
    print(format("*",">"+str(counter))) # format used for spaces
    counter += 1

#second half of arrow

# asterisks are printed until counter equates to 0
while counter > 0:
    
    print(format("*",">"+str(counter))) #format used for spaces
    counter -= 1


#IT WORKS!
