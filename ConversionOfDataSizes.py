## Anthony Dike - Due: Sept. 21, 2017
## CSCI-UA.0002-012
## Assignment 2: Program #3: Data Size Converter

"""
This program asks the user to input a file size in Kilobytes (KB)
then converts the supplied input into bits, bytes, megabytes, and gigabytes.
"""

#user inputs data
kilo = float(input("Enter a file size, in kilobytes (KB): "))

#spacer
print()

#display KB
print(str(kilo) + " KB ...")

#spacer
print()

#format into numbers with commas and two decimal places
kbToBits = '{0:,.2f}'.format(kilo*1024*8)
# TEST print(kbToBits)
kbToBytes = '{0:,.2f}'.format(kilo*1024)
# TEST print(kbToBytes)
kbToMB = '{0:,.2f}'.format(kilo/1024)
#TEST print(kbToMB)
kbToGB = '{0:,.2f}'.format(kilo / 1024 / 1024)
# TEST print(kbToGB)

#display conversions

print("... in bits", format((kbToBits), ">23")  + " bits") # from KB to bits
print("... in bytes", format((kbToBytes), ">21") + " bytes") # from KB to bytes
print("... in megabytes", format((kbToMB), ">20") + " MB") # from KB to megabytes
print("... in gigabytes", format((kbToGB), ">21")  + "GB") # from KB to gigabytes
