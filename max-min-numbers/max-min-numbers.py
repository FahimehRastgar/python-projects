
import random

def getMinimum(ml):

    minimum = ml[0]
    for y in ml:
        if y > minimum :
            continue
        else:
            minimum = y
    return minimum

def getMaximum(ml):
    maximum = ml[0]
    for m in ml:
        if m < maximum :
            continue
        else:
            maximum = m
    return maximum

def maxMin ():

    numbers = int(input(" \n How many numbers should be in the list (10-50) "))
    
    myList = []
    
    for i in range(numbers):
        x = random.randint(1,100)
        myList.append(x)
           
    print(myList)

    print(f"Minimum:", getMinimum(myList))
    print(f"Maximum:", getMaximum(myList))


maxMin()