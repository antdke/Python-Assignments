## Anthony Dike - Due: Nov. 14, 2017
## CSCI-UA.0002-012
## Assignment 7: Part 1b

"""
This program contains the following:

-- USERNAME VALIDATOR --

1) prompts user to input a username (string)
2) checks username:
    - is between 8 - 15 characters long
    - posseses any special chars. (anything not alphanumeric)
    - checks if the first char is a number
    - must possess one uppercase char
    - must possess one lowercase char
    - must possess one numeric char
3) keeps prompting user to input a username until it is valid

-- PASSWORD VALIDATOR --

1) prompts user to input a password (string)
2) checks password:
    - is at least 8 characters
    - cannot contain the user's username
    - must possess one uppercase char
    - must possess one lowercase char
    - must possess one numeric char
    - must contain one of select 'special' chars (#, $, %, and &)
3) keeps prompting user to input a password until it is valid
    
"""

#PROGRAM START

"""
----------- USERNAME VALIDATOR -----------------

"""

# key to unlocking while loop
proceed = False

# indicates that there is is an error present
errorPresent = False

# loop to keep asking user for valid response
while proceed == False:

    errorPresent = False

    # ask user for a username
    user = input("Please enter a username: ")

    # check if username is 8 - 15 characters long
    if len(user) < 8 or len(user) > 15:

        # indicates that there is is an error present
        errorPresent = True

        # error message
        print("Username must be between 8 and 15 characters.")
        print()

        # start 'while loop' over
        continue
    

    # checks if username only possess alphanumeric characters
    elif user.isalnum() == False:

        # indicates that there is is an error present
        errorPresent = True

        # error message
        print("Username must contain only alphanumeric characters.")
        print()

        # start 'while loop' over
        continue
    

    # checks if the first char is a number
    elif user[0].isnumeric() == True: #THIS WORKS

        # indicates that there is is an error present
        errorPresent = True

        # error message
        print("The first character in your username cannot be a digit")
        print()

        # start 'while loop' over
        continue
    
    
    # counters
    notNum = 0
    notUpper = 0
    notLower = 0
    

    # checks if username possesses one uppercase char, one lowercase char
    # and one number
    for n in user:

         # keeps count of how many times a letter isnt a digit
        if n.isnumeric() == False:

            notNum += 1
        
        # keeps count of how many times a letter isnt an uppercase character
        if n.isupper() == False:

            notUpper += 1

        # keeps count of how many times a letter isnt a lowercase character
        if n.islower() == False:

            notLower += 1

        

        
        if notNum == len(user):

            # indicates that there is is an error present
            errorPresent = True
            
            # error message
            print("Your username must contain at least one digit")
            print()

            # start 'while loop' over
            continue

        elif notUpper == len(user):

            # indicates that there is is an error present
            errorPresent = True
            
            # error message
            print("Your username must contain at least one uppercase character")
            print()

            # start 'while loop' over
            continue
        
        
        elif notLower == len(user):

            # indicates that there is is an error present
            errorPresent = True
            
            # error message
            print("Your username must contain at least one lowercase character")
            print()

            # start 'while loop' over
            continue

    
    # this condition activates when no error
    if errorPresent == False:

        # celebratory message
        print("Your username is valid!")
        print()
        
        # stops while loop & ends program
        proceed = True


"""
----------- PASSWORD VALIDATOR -----------------

1) prompts user to input a password (string)
2) checks password:
    - is at least 8 characters
    - cannot contain the user's username
    - must possess one uppercase char
    - must possess one lowercase char
    - must possess one numeric char
    - must contain one of select 'special' chars (#, $, %, and &)
3) keeps prompting user to input a password until it is valid

"""

# key to unlocking while loop
proceed2 = False

# indicates that there is is an error present
errorPresent2 = False

# loop to keep asking user for valid response
while proceed2 == False:

    # ask user for a password
    password = input("Please enter a password: ")


    # check if password is at least 8 characters
    if len(password) < 8:

        # indicates that there is is an error present
        errorPresent2 = True

        # error message
        print("password must be at least 8 characters.")
        print()

        # start 'while loop' over
        continue


    # checks if password contains the username
    if user in password:

        # indicates that there is is an error present
        errorPresent2 = True

        # error message
        print("Username cannot be used in the password.")
        print()

        # start 'while loop' over
        continue
        
    
    # counters
    notNum = 0
    notUpper = 0
    notLower = 0
    notSpecial = 0
    

    # checks if password possesses one uppercase char, one lowercase char
    # and one number
    for n in password:

         # keeps count of how many times a char isnt a digit
        if n.isnumeric() == False:

            notNum += 1
        
        # keeps count of how many times a char isnt an uppercase character
        if n.isupper() == False:

            notUpper += 1

        # keeps count of how many times a char isnt a lowercase character
        if n.islower() == False:

            notLower += 1

        # keeps count of how many times a char isnt a special character
        if (n == "#") or (n == "$") or (n == "%") or (n == "&"):

            notSpecial += 0
        else:
            notSpecial += 1
        

    
    if notNum == len(password):

        # indicates that there is is an error present
        errorPresent2 = True
        
        # error message
        print("Your password must contain at least one digit")
        print()

    elif notUpper == len(password):

        # indicates that there is is an error present
        errorPresent2 = True
        
        # error message
        print("Your password must contain at least one uppercase character")
        print()
    
    
    elif notLower == len(password):

        # indicates that there is is an error present
        errorPresent2 = True
        
        # error message
        print("Your password must contain at least one lowercase character")
        print()

    elif notSpecial == len(password):

        # indicates that there is is an error present
        errorPresent2 = True
        
        # error message
        print("Your password must contain at least one special character")
        print()

    
# this condition activates when no error
if errorPresent2 == False:

    # celebratory message
    print("Your password is valid!")
    print()
    
    # stops while loop & ends program
    proceed2 = True
        
