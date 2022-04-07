################################################
##Name: Broady Rivet
##Date: 02/04/19
##Description: Flip a coin as many times as asked by user and display probabilities
################################################
from random import randint

def Game():
    games = input("How many games?")
    toss = input("How many coin tosses per game?")
    for x in range(0, 1):
        groupa = 0
        groupb = 0
        p = 0
        wins = 0
        for i in range (0, games):
            heads = 0
            tails = 0
            count = 0
            both = 0
            if (count < toss):
                for j in range(0, toss):
                    coin1 = randint(1, 2)
                    coin2 = randint(1, 2)
                    if (coin1 != coin2):        #Prof
                        both += 1
                        count += 1

                    elif (coin1 and coin2 == 1):    #group A
                        heads += 1
                        count += 1

                    elif (coin1 and coin2 == 2):  #group B
                        tails += 1
                        count += 1


                if (tails > both and  tails > heads):               
                    groupb += 1
                    wins += 1

                elif (both > tails and both > heads):
                    p += 1
                    wins += 1
                        
                elif (heads > tails and heads > both):
                    groupa += 1
                    wins += 1
                        
            a = (float (heads) / float (count) * 100)
            b = (float (tails) / float (count) * 100)
            prof = (float (both) / float (count) * 100)

                


            print "Game {}:\n Group A: {} ({}%); Group B: {} ({}%); Prof: {} ({}%);".format(i, heads, a, tails, b, both, prof)

            wina = round((float (groupa) / float (wins)) * 100,2)
            winb = round((float (groupb) / float (wins)) * 100,2)
            winp = round((float (p) / float (wins)) * 100,2)

        print "Wins: Group A = {} ({}%); Group B = {} ({}%); Prof = {} ({}%)".format(groupa, wina, groupb, winb, p, winp)

##############
##main Program
##############

Game()

