##################################################################################
##Name: Broady Rivet                                                            ##
##Date:12/4/18                                                                  ##
##Description: Program finds how many zeros are present in a user given number. ##
##################################################################################
##import needed libraries##
from time import time

##Define your function##
def Zeros():
    number = input("Please enter an interger.")
    counter = 0

    #start the timer#
    starter = time()

    #actaul calculation#
    for i in range (1, number + 1):
        number = number + 1
        while i > 0:
            if i % 10 == 0:
                counter = counter + 1
            i = i / 10

    #Print the results#
    print "The number of zeros written from 1 to {} is {}.".format(number/2,counter)

    #stop timer#
    stopper = time()

    #calcuate elapsed time#
    elapsedtime = stopper - starter

    #display elapsed time#
    print "This took {} seconds.".format(elapsedtime)
    
################################
##           MAIN             ##
##          PROGRAM           ##
################################
Zeros()
