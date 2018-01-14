## Anthony Dike - Due: Sept. 14, 2017
## CSCI-UA.0002-012
## Assignment 1: Program #3: Math Expressions

"""
This program does the following:
1. Converts the speed of light from Kilometers per second (Km/s) to Miles per second (Mps)
2. Displays the value of half the speed of light in Mps
3. Displays the value of a quarter the speed of light in Mps
4. Converts the speed of the Earth's revolution around the Sun from Miles per hour (Mph) to Kms
5. Expresses the speed of the Earth's revolution as a percentage of the speed of light

"""

#WARNING: Don't use commas so that the system doesn't confuse the numbers for tuples
lightSpeed = 299792.458 #speed of light in kps
conversionKmToM = 0.621 #conversion rate of Km to Mi (1 Km = 0.621 Mi)
earthSpeed = 66600 #speed of Earth's revolution around the Sun in mph 

print("Speed of light (Kilometers / sec):",str(lightSpeed) + " kps",sep="    ") #displays the speed of light
print("Speed of light (Miles / sec):",str(lightSpeed*conversionKmToM) + " mps",sep="         ") #displays the speed of light in Mps
print("Half speed of light (Miles / sec):",str(lightSpeed*conversionKmToM/2) + " mps",sep="    ") #displays half the speed of light in Mps
print("Quarter speed of light (Miles / sec):",str(lightSpeed*conversionKmToM/4) + " mps",sep=" ") #displays a quarter of the speed of light in Mps
print() #space
print("The earth moves 66,600 miles / hour around the sun") #speed of the earth's revolution in Mph
print("66,600 miles per hour is equal to:",str(earthSpeed/3600.00/conversionKmToM) + " kps",sep="    ") #displays the conversion of the speed of earth's revoltion from mph to kps
print("66,600 miles per hour is equal to:",str((earthSpeed/3600.00/conversionKmToM)/lightSpeed) + " % of the speed of light",sep="    ") #displays the speed of the Earth's revolution as a percentage of the speed of light


