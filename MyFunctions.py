## Anthony Dike - Due: Oct. 31, 2017
## CSCI-UA.0002-012
## myfunctions file

# LINE FUNCTIONS #

# horizontal line function

def horizontal_line(w):
    width = w 
    print("*"*(width))

# vertical line function

def vertical_line(w):
    width = w
    #shift = s #not needed(?)
    #height = 5 # assume always 5
    print(format("*",">"+str(width)))

# Two vertical lines function

def two_vertical_lines(w):
    #height = 5
    width = w
    #subtract 2 from width because the 2 asterisks count as part of wisth
    print(format("*"+(" "*(width-2))+"*")) 

# ------------------------------------------



# NUMBER FUNCTIONS #

# Number 0
def number_0(w):
    print()
    horizontal_line(w)
    for n in range(1,3+1):
        two_vertical_lines(w)
    horizontal_line(w)
    print()

# Number 1
def number_1(w):
    print()
    for n in range(1,5+1):
        vertical_line(w)
    print()


# Number 2
def number_2(w):
    print()
    horizontal_line(w)
    vertical_line(w)
    horizontal_line(w)
    vertical_line(w-w)
    horizontal_line(w)
    print()

# Number 3
def number_3(w):
    print()
    horizontal_line(w)
    vertical_line(w)
    horizontal_line(w)
    vertical_line(w)
    horizontal_line(w)
    print()

# Number 4
def number_4(w):
    print()
    two_vertical_lines(w)
    two_vertical_lines(w)
    horizontal_line(w)
    vertical_line(w)
    vertical_line(w)
    print()

# Number 5
def number_5(w):
    print()
    horizontal_line(w)
    vertical_line(w-w)
    horizontal_line(w)
    vertical_line(w)
    horizontal_line(w)
    print()
    
# Number 6
def number_6(w):
    print()
    horizontal_line(w)
    vertical_line(w-w)
    horizontal_line(w)
    two_vertical_lines(w)
    horizontal_line(w)
    print()

# Number 7
def number_7(w):
    print()
    horizontal_line(w)
    for n in range(1,4+1):
        vertical_line(w)
    print()

# Number 8
def number_8(w):
    print()
    horizontal_line(w)
    two_vertical_lines(w)
    horizontal_line(w)
    two_vertical_lines(w)
    horizontal_line(w)
    print()

# Number 9
def number_9(w):
    print()
    horizontal_line(w)
    two_vertical_lines(w)
    horizontal_line(w)
    vertical_line(w)
    vertical_line(w)
    print()

#--------------------------------------------------

# OPERATION FUNCTIONS #

# addition function

def plus(w):
    for n in range(1,5):
        if n == 3:
            horizontal_line(w)
        print(format("*",">"+str(3)))

# subtraction function

def minus(w):
    horizontal_line(w)

#---------------------------------------------------

# Check Answer function

def check_answer(number1, number2, answer, operator):
    if operator == "+":
        if number1 + number2 == answer:
            return True
        else:
            return False
    else:
        if number1 - number2 == answer:
            return True
        else:
            return False
