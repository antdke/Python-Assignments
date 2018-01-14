## Anthony Dike - Due: Sept. 28, 2017
## CSCI-UA.0002-012
## Assignment 3: Program #1: Valid Triangle Tester

"""
This program does the following:

1) This program asks the user for coordinates of the points of a triangle. 
2) The program computes the distance between each point. 
3) The program determines then tells the user whether the triangle is valid.
"""

print("Valid Triangle Tester")

# prompts user to input x and y values of the points on the triangle
p1x = float(input("Enter point #1 - x position: "))
p1y = float(input("Enter point #1 - y position: "))
p2x = float(input("Enter point #2 - x position: "))
p2y = float(input("Enter point #2 - y position: "))
p3x = float(input("Enter point #3 - x position: "))
p3y = float(input("Enter point #3 - y position: "))

# spacer
print()

#Calculation & assignment of side lengths
side1 = format((( (p1x-p2x)**2 + (p1y-p2y)**2 )**0.5), ".2f")
side2 = format((( (p2x-p3x)**2 + (p2y-p3y)**2 )**0.5), ".2f")
side3 = format((( (p3x-p1x)**2 + (p3y-p1y)**2 )**0.5), ".2f")

#Display side lengths
print("The length of each side of your test shape is: ")
print("Side 1: " + str(side1))
print("Side 2: " + str(side2))
print("Side 3: " + str(side3))


"""
In order for a triangle to be valid,
it must meet these three standard:

(a) Side 1 + Side 2 must be longer than Side 3
(b) Side 2 + Side 3 must be longer than Side 1
(c) Side 3 + Side 1 must be longer than Side 2
"""
# Triangle Validator

# This validates whether the points entered by the user creates a valid triangle.
if float(side1) + float(side2) > float(side3):
    if float(side3) + float(side2) > float(side1):
        if float(side3) + float(side1) > float(side2):
            print("\nThis is a valid triangle!")
        else:
            print("\nThis is not a valid triangle.")
    else:
        print("\nThis is not a valid triangle.")
else:
    print("\nThis is not a valid triangle.")
