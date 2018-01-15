## Anthony Dike - Due: Oct. 24, 2017
## CSCI-UA.0002-012
## Assignment 5: Part 2b: Find all Prime Numbers between 1 and 1000

"""
This program does the following:

1) finds all prime number from 1 - 1000
"""

# PROGRAM START

#set range from 2 - 1000 bcuz 1 is NOT a prime number
for num in range(2,1001):
    #resets boolean prime checker
    prime = True
    #range of 2 current num in first for loop iteration
    for i in range(2,num):
        if num % i == 0:
            #sets prime to false if num is divisible by anything other than 1
            prime = False
    #if prime stays true then num is prime
    if prime == True:
        print(num,"is a prime number!")
