##################################################################################################
# Name: Broady Rivet
# Date: 10/1/18
# Description: This code asks for your name and age and displays both and multiplys your age by 2.
##################################################################################################

# function that prompts the user for a name and returns it
def name1():
    return raw_input("Please enter your name. ")

# function that receives the user's name as a parameter, and prompts the user for an age and returns it
def age1(name):
    return input("How old are you, {}?".format(name))

# function that receives the user's name and age as parameters and displays the final output
def finalfunc(name, age):
    print "Hi, {}. You are {} years old. Twice your age is {}".format(name, age, age*2)


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get the user's name
name = name1()

# get the user's age
age = age1(name)

# display the final output
finalfunc(name, age)
