######################################################################################################################
# Name: Broady Rivet
# Date: 12/22/18
# Description: a class takes given numbers makes them into a fraction, then divides said
#               numbers and gives the answer. The program can also add, subtract, multiply, or divide
#               fractions before giving an answer.
######################################################################################################################

# the fraction class
class Fraction(object):
    
# by default, a fraction is 0/1
    def __init__(self, num=0, den=1):
        self.num = num
# make sure not to set the denominator to 0 if specified
        if (den == 0):
            den = 1
        self.den = den
        
        self.reduce()
# getter for the numerator
    @property
    def num(self):
        return self._num
    
# setter for the numerator
    @num.setter
    def num(self, value):
        self._num = value
        
# getter for the denominator
    @property
    def den(self):
        return self._den
    
# setter for the denominator
    @den.setter
    def den(self, value):
# ignore if the specified denominator is 0
        if (value != 0):
            self._den = value
            
#reduces a fraction
    def reduce(self):
        gcd = 1
        minimum = min(abs(self.num), abs(self.den))
        for i in range(2, minimum + 1):
            if (self.num % i == 0 and self.den % i == 0 ):
                gcd = i
        self.num /= gcd
        self.den /= gcd
        if (self.num == 0):
            self.den = 1
            
# calculates and returns the sum of two fractions
    def __add__(self, other):
        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den
        sum = Fraction(num, den)
        self.reduce()
        return sum
    
# calculates and returns the difference of two fractions
    def __sub__(self, other):
        num = (self.num * other.den) - (other.num * self.den)
        den = self.num * other.den
        dif = Fraction(num, den)
        self.reduce()
        return dif
    
# calculates and returns the product of two fractions
    def __mul__(self, other):
        num = (self.num * other.num)
        den = (self.den * other.den)
        pro = Fraction(num, den)
        self.reduce()
        return pro
    
# calculates and returns the division of two fractions
    def __div__(self, other):
        num = (self.num * other.den)
        den = (self.den * other.num)
        div = Fraction(num, den)
        self.reduce()
        return div
    
# returns a fraction's numeric representation
    def getReal(self):
        return float(self.num) / self.den
    def __str__(self):
        return "{}/{} ({})".format(self.num, self.den, self.getReal()) 

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

