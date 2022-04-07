###################################################################
## Name: Broady Rivet                                             ##  
## Date: 12/13/18                                                 ##
## Description: program makes a class of cars and shows the name, ##
##              model, and year of the car.                       ##
###################################################################

# the vehicle class
class Vehicle(object):
    def __init__(self, make, model):
        self.year = 0
        self.model = model
        self.make = make
# a vehicle has a year, make, and model
    #make mutator
    @property
    def make(self):
        return self._make

    #make getter
    @make.setter
    def make(self, make):
        self._make = make

    #year mutator
    @property
    def year(self):
        return self._year

    #year getter
    @year.setter
    def year(self, year):
        #if year isnt in correct parameters the year
        #is set to the last one used
        if(year > 2000 and year < 2018):
            self._year = year

    #model mutator
    @property
    def model(self):
        return self._model
    
    #model getter
    @model.setter
    def model(self, model):
        self._model = model



# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
########################
##   the main part    ##
##   of the program   ##
########################

v1 = Vehicle("Dodge", "Ram")
v2 = Vehicle("Honda", "Odyssey")
print "v1={} {}".format(v1.make, v1.model)
print "v2={} {}".format(v2.make, v2.model)
print

v1.year = 2016
v2.year = 2016
print "v1={} {} {}".format(v1.year, v1.make, v1.model)
print "v2={} {} {}".format(v2.year, v2.make, v2.model)
print

v1.year = 1999
v2.model = "Civic"
v2.year = 2007
print "v1={} {} {}".format(v1.year, v1.make, v1.model)
print "v2={} {} {}".format(v2.year, v2.make, v2.model)

