## Anthony Dike - Due: Nov. 28, 2017
## CSCI-UA.0002-012
## Assignment 8: Part 1

#This program converts the zeros with index values that are prime in the range of 1-1001 to ones.

"""
# KEY
# 1 == NON PRIME
# 0 = PRIME

CHANGE TOTAL VALUE TO 1000 at end
"""

# Create a list of 1,000 values ... all of which are set to zero
myList = [0] * 1000

# set first two values to 1
myList[0] = 1
myList[1] = 1

"""
Ruling Out Non-Primes
"""
# make all values in the indices that are multiples of 2 non-prime (0)
# excluding 2

for num in range(4, len(myList)):
    if num % 2 == 0:
        myList[num] = 1

#print(myList) # Test

# make all values in the indices that are multiples of 3 non-prime (0)
# excluding 3

for num in range(6, len(myList)):
    if num % 3 == 0:
        myList[num] = 1

#print(myList) # Test

# make all values in the indices that are multiples of 5 non-prime (0)
# excluding 5

for num in range(10, len(myList)):
    if num % 5 == 0:
        myList[num] = 1

#print(myList) # Test

"""
Printing the Primes Indices
"""
print()
print()
print()

##for n in range(len(myList)):
##    if myList[n] == 0:
##        #print("True") #Test1: PASSED
##        print(myList.index(myList[n]))

rowCounter = 0

for n in range(0, len(myList)):
    if myList[n] == 0:
        #for x in range (0,10):
        print(format(myList.index(myList[n]),">3"), end=" ")# the issue is having indices finder
        #count for more than the first occurence
        rowCounter += 1
        if rowCounter % 10 == 0:
            print("\n")

        # change the number completely from a 0 to a diff num after
        # it is read.
        myList[myList.index(myList[n])] = 2
        #print(myList) #test
