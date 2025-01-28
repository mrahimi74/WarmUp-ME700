#This file contains some basic functions used in the main code


#This function calculates the average of two numbers
def Avg(x, y):
    return (x + y) / 2

#This function gets any number and returns its sign
def sign(x):
    if x > 0:
        return 1
    else:
        return -1

#This function calculates the absolute value of a number
def abs(x):
    if x >= 0:
        return x
    else:
        return -x
