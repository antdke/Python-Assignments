## Anthony Dike - Due: Oct. 24, 2017
## CSCI-UA.0002-012
## Assignment 5: Part 2a: Prime Number Finder

"""
This program does the following:

1) get user to input a pos. int. (make user retry if input 0 or neg. int.)
2) check if user int. is a prime number.

NOTES:
- 1 is NOT a prime num
- after an iteration evenly divides test num, num CANT be prime
- IMPORTANT: only report if a num is prime after all iterations, NOT w/in loop

"""

## PROGRAM START

# user inputs pos. int.
# keep user until user inputs pos. num. (NO zero or neg. num.)

proceed = False #bool value

while proceed == False:
    
    #user input
    testNum = int(input("Enter a positive number to test: "))
    
    #test number cant be a zero or neg num
    if testNum <= 0:
        print("Only numbers greater than 0! Please, Try Again.")
        continue
    
    else:
        #breaks loop
        proceed = True

# spacer
print()

# indicates if testNum is prime or not
# determines final print statement
notPrime = False

if testNum == 1:
    notPrime = True
else:
    # for loop to validate if prime number
    for num in range(2,testNum):
    
        #if statement to check if testNum divides evenly
        if testNum % num == 0:
            
            #prints if testNum is NOT prime
            print(num,"is a divisor of",testNum,"... stopping")
            notPrime = True
            break #stops loop bcuz testNum is NOT prime
        
        else:
            #prints with each iteration of not dividing evenly
            print(num,"is NOT a divisor of",testNum,"... continuing")

#spacer
print()

# either prints whether testNum is prime or not
if notPrime == True:
    print(testNum,"is not a prime number.")
else:
    print(testNum,"is a prime number!")
