############################################################################################
# Name:Broady Rivet
# Date: 10/24/18
# Description: Subtracts 1 beer then displays the amount and repeats until all beer is gone.
############################################################################################

# the algorithm implemented recursively
def passSomeBeers(bottles):
        if (bottles > 1):
                print "{} bottles of beer on the wall.".format(bottles)
                print "{} bottles of beer.".format(bottles)
                print "Take one down, pass it around."
        bottles = bottles - 1
        print "{} bottles of beer on the wall.".format(bottles)
        print
                
        if(bottles == 1):
                print "{} bottle of beer on the wall.".format(bottles)
                print "{} bottle of beer.".format(bottles)
                print "Take one down, pass it around."
                
        if (bottles > 0):
                passSomeBeers(bottles)
        
        if(bottles == 0):
                print 


###############################################
# MAIN PART OF THE PROGRAM
###############################################
passSomeBeers(99)

