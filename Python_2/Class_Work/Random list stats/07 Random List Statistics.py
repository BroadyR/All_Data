###########################################################################################
# Name: Broady Rivet
# Date: 11/6/17
# Description: code uses given parameters and generates random numbers within said
#               parameters and displays the radndom list and the mean, median, and range.
###########################################################################################
from random import randint
# function that prompts the user for a list size, minimum and maximum values, creates the list, and returns it
# you must use the list functions discussed in class to add integers to the list
# (1) prompts the user for a list size
def listsize():
    grades = []
    listsize1 = int(input("How many random intergers would you like to add to the list?"))
    miny = input("What would you like the minimum value to be?")
    maxy = input("What would you like the maximum value to be?")
# (2) prompts the user for the integers to store in the list (corresponding to the list size)
    while (len(grades)< listsize1):
        numbers = randint(miny,maxy)
# (3) creates the list
        grades.append(numbers)
# (4) returns the list
    return grades

#get minimum
def getmin(grades):
#assume valuse in first is smallest
    smallest = grades[0]
#cycle through whole list
#update if you find smaller
    i = 1
    while(i < len(grades)):
        if (grades[i] < smallest):
            smallest = grades[i]
        i += 1
    return smallest

#getmax
def getmax(grades):
#assume valuse in first is biggest
    biggest = grades[0]
#cycle through whole list
#update if you find biggest
    i = 1
    for i in range (0, len(grades)):
        if (grades[i]>biggest):
            biggest = grades[i]
        i += 1
    return biggest

# create the list
nums = listsize()

# display the list
# there is no need to write/call your own function for this part
print ("The list: {}".format(nums))

# function that receives the list as a parameter, and calculates and returns the mean
def mean(grades):
    global x
    x = 0
    i = 0
    for i in range (len(grades)):
        x += grades[i]
    avg = float(x) / len(grades)
    return avg

# function that receives the list as a parameter, and calculates and returns the median
def median(grades):
    list.sort(grades)
    if (len(grades)%2 == 0):
        median1 = float(((grades[(len(grades)/2)-1])) + float(grades[len(grades)/2])) / 2
    else:
        median1 = grades[(len(grades)/2)]
    return median1

# function that receives the list as a parameter, and calculates and returns the range
def ranger(grades):
    range1 = (getmax(grades)) - (getmin(grades))
    return range1


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################

mean2 = mean(nums)
median2 = median(nums)
range2 = ranger(nums)


# calculate and display the mean
print ("The mean of the list is {}.".format(mean2))

# calculate and display the median
print ("The median of the list is {}.".format(float(median2)))

# calculate and display the range
print ("The range of the list is {}.".format(range2))
