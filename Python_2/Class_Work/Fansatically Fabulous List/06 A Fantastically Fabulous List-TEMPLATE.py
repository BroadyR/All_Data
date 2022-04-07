###############################################################################################################################################################
# Name: Broady Rivet
# Date: 11/1/18
# Description: Ask user amount of numbers on the list and ask them to enter a number that amount of times and returns the list regularly, sorted, and reversed.
################################################################################################################################################################

# function that:
# (1) prompts the user for a list size
def listsize():
    grades = []
    listsize = input("How many intergers would you like to add to the list?")
# (2) prompts the user for the integers to store in the list (corresponding to the list size)
    while (len(grades)< listsize):
        numbers = input("Enter a number:")
# (3) creates the list
        grades.append(numbers)
# (4) returns the list
    return grades


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
numbers = listsize()

# display information about the list using the list functions discussed in class
# there is no need to write/call your own functions here
print ("The original list:{}".format(numbers))
print ("The length of the list is {}.".format(len(numbers)))
print ("The minimum value in the list is {}.".format(min(numbers)))
print ("The maximum value in the list is {}.".format(max(numbers)))
numbers.reverse()
print ("The reversed list: {}".format(numbers))
numbers.sort()
print ("The sorted list: {}".format(numbers))
