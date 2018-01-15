## Anthony Dike - Due: Oct. 24, 2017
## CSCI-UA.0002-012
## Assignment 5: Part: EXTRA CREDIT

"""
This program does the following:
1) asks user for 2 inputs: start and end numbers
2) make sure user inputs valid inputs
3) checks for prime numbers from start to end number
4) organizes printed primes into a table with 10 numbers in each row

"""
proceed = False

while proceed == False:
    #start number
    start = int(input("Start number: "))

    #end number
    end = int(input("End number: "))
    
    # start and end can't be negative
    if start < 0 or end < 0:
        print("Start and end must be positive")
        print()
        continue

    # start can't be greater than end
    elif start > end:
        print("End number must be greater than start number")
        print()
        continue

    else:
        # while loop ends when inputs are valid
        proceed = True
        break


# counter for row
rowCount = 0

#set range from start and end 
for num in range(start,end+1):
    
    #resets boolean prime checker
    prime = True
    
    # 1 is Not a prime number 
    if num == 1:
        prime = False
        
    else:
        #range of 2 current num in first for loop iteration
        for i in range(2,num):
            
            if num % i == 0:
                
                #sets prime to false if num is divisible by anything other than 1
                prime = False
                
    #if prime stays true then num is prime
    if prime == True:
        
        #progresses num printed on row
        rowCount += 1
        
        #prints numbers in table-like format
        print(format(num, ">4d"), end="")
        
    #once row prints 10 num, start over on new line
    if rowCount == 10:
        print("", end="\n")
        rowCount = 0
