###########################################################################################
# Name: Broady Rivet
# Date: 10/12/18
# Description: This code asks for three intergers and displays all three typed
#               intergers, the minimum, the maximum, the mean, median, mode,
#               and range of all three. 
###########################################################################################

# function that prompts the user to enter an integer and returns it
def number1():
    num1 = input("Please enter an interger.")
    return num1
def number2():
    num2 = input("Please enter an interger.")
    return num2
def number3():
    num3 = input("Please enter an interger.")
    return num3

# function that receives three integers as parameters and returns the minimum of the three
def miny(num1, num2, num3):
    if (num1<=num2) and (num1<=num2):
        return num1
    elif (num1>=num2) and (num2>=num3):
        return num2
    else:
        return num3

# function that receives three integers as parameters and returns the maximum of the three
def maxy(num1, num2, num3):
    if (num1>=num2) and (num1>=num3):
        return num1
    elif (num2>=num1) and (num2>=num3):
        return num2
    else:
        return num3

# function that receives three integers as parameters, and calculates and returns the mean
def mean(num1, num2, num3):
    mean1 = float(num1+num2+num3)/3
    return mean1
# function that receives three integers as parameters, and calculates and returns the median
def med(num1, num2, num3):
    if (num1 < num2):
        if (num2 < num3):
            return num2
        elif (num2 > num3):
            return num3
    elif (num1 > num2):
        if (num1 < num3):
            return num1
        elif (num1 > num3):
            return num3
    else:
        return "there is no median because two or more numbers are equal"
# function that receives three integers as parameters, and calculates and returns the mode
def mode(num1, num2, num3):
    if (num1 ==  num2):
        return num2
    elif (num2 == num3):
        return num2
    elif(num1 == num3):
        return num1
    else:
        return "undefined"

# function that receives three integers as parameters, and calculates and returns the range
def rang(num1, num2, num3):
    range1 = int(maxy(num1, num2, num3)) - int(miny(num1, num2, num3))
    return range1


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get three integers from the user
num1 = number1()
num2 = number2()
num3 = number3()

# determine and display the minimum value
minimum = miny(num1, num2,num3)
print "The minimum value is {}.".format(minimum)

# determine and display the maximum value
maximum = maxy(num1, num2, num3)
print "The maximum value is {}.".format(maximum)

# calculate and display the mean
mean1 = mean(num1, num2, num3)
print "The mean is {}.".format(mean1)

# calculate and display the median
median = med(num1, num2, num3)
print "The median is {}.".format(median)

# calculate and display the mode
mode1 = mode(num1, num2, num3)
print "The mode is {}.".format(mode1)

# calculate and display the range
range1 = rang(num1, num2, num3)
print "The range is {}.".format(range1)
