##########################################################################################
# Name: Broady Rivet
# Date: 10/29/18
# Description: This program creates and sorts data inputted into a table
##########################################################################################

#import the math library to use needed functions
import math

# a function that displays the table
def table(x, y, z, B):
    if(x == B):
        print "n\tSeq\tBin\tPref"
        print "-"*32
    if(x == 0):
        print "0\t0\t0\t0"
    else:
        print "{}\t{}\t{}\t{}".format(x, Seq(x), Bin(x), int(round(Seq(x)/Bin(x))))
    if(x < y):
        x += z
        if (x <= y):
            table(x, y, z, B)

#function that asks for a minimum number and gives an error if is less than 0
def miny():
    number1 = input("Minimum number of list items (>=0)?")
    if (number1 < 0):
        print "ERROR: Minimum must be >=0!"
        number1 = miny()
    return number1

#function that asks for a maximum number and gives an error if is less than minimum
def maxy(x):
    number2 = input("Maximum number of list items (>= min ({}))?".format(x))
    if (number2 < x):
        print "ERROR: Maximum must be >= minimum ({})!".format(x)
        number2 = maxy(x)
    return number2


#a function that asks for the interval and gives an error if the number is less than 1
def interval():
    interval1 = input("The interval between each row of the table (>= 1)?")
    if (interval1 < 1):
        print "ERROR: Interval must be >= 1!"
        interval1 = interval()
    return interval1
                

# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def Seq(x):
              return (x/2)
              

# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def Bin(x):
              return int((math.ceil(math.log(x+1, 2))))
              
###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
miny1 = miny()


# get user input for the maximum (make sure that is is >= minimum)
maxy1 = maxy(miny1)


# get user input for the interval (make sure that it is >= 1)
interval1 = interval()

# generate the table
table(miny1, maxy1, interval1, miny1)
