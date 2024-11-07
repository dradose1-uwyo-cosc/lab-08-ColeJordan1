# Cole Jordan
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to: Peter Martinez, Chauncy Hendon
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def decimalChecker(input):
    numString = input
    if '.' in numString:
        numString = numString.replace('.', '', 1)
        if '.' in numString:
            return False
        else:
            return numString
    else:
        return False

def negChecker(input):
    numString = input
    if numString.startswith('-'):
        numString = numString.replace('-', '', 1)
        if '-' in numString:
            return False
        else:
            return numString
    else:
        return False
    
def numChecker(input):
    numString = input
    isFloat = False
    if negChecker(input) != False:
        numString = negChecker(numString)
    if decimalChecker(input) != False:
        numString = decimalChecker(numString)
        isFloat = True

    if numString.isdigit() and isFloat:
        return float(input)
    elif numString.isdigit():
        return int(input)
    else:
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def pointSlope(m,b,lowerX:int,upperX:int):
    yList = []
    if numChecker(m) != False or numChecker(b) != False:
        m = numChecker(m)
        b = numChecker(b)
    elif lowerX > upperX:
        return False
    else:
        return False
    
    for i in range(lowerX,upperX):
        yList.append((m*i) + b)

    return yList


# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

while True:
    entry = input("Enter 'exit' to exit. Enter the function values as m,b,lower bound,upper bound ")
    if entry.lower() == 'exit':
        break
    
    try:
        listInput = entry.split(',')
        if pointSlope(listInput[0],listInput[1],int(listInput[2]),int(listInput[3]) + 1) == False:
            print('Invalid Input A')
            continue
        else:
            print(f"Listed Values: {pointSlope(listInput[0],listInput[1],int(listInput[2]),int(listInput[3]) + 1)}")
    except:
        print('Invalid Input B')
        continue

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def squareRoot(input):
    if input < 0:
        return 
    elif input == 0:
        return 0
    else:
        return input**(1/2)
    


def quadraticFormula(a,b,c):
    result1 = 0
    result2 = 0
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        result1 = (-b + squareRoot((b**2 - 4*a*c))) / (2*a)
        result2 = (-b - squareRoot((b**2 - 4*a*c))) / (2*a)
        return [result1,result2]
    except:
        return False

while True:
    entry = input("Type 'exit' to exit. Enter the quadratic values in the format of a,b,c ")
    if entry.lower == 'exit':
        break
    entry = entry.split(',')
    if quadraticFormula(entry[0], entry[1], entry[2]) == False:
        print('Invalid Input')
        continue
    
    print(f"Result: {quadraticFormula(entry[0], entry[1], entry[2])}")
    
