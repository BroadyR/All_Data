#############################################################################
##Name: Broady Rivet                                                       ##
##Date: 1/14/19                                                            ##
##Description: Super class is used to recall information about a larger    ##
##                group to make a more specified class.                    ##
#############################################################################
# the vehicle class
class Vehicle(object):
    def __init__(self, year, make , model):
        self.year = year
        self.make = make
        self.model = model
    # a vehicle is instantiated with a make and model
    @property
    def year(self):
        return self._year
    #mutator
    @year.setter
    def year(self, value):
        self._year = 2000
        if (value > 2000 and value < 2018):
            self._year = value
    #make mutator
    @property
    def make(self):
        return self._make

    #make getter
    @make.setter
    def make(self, make):
        self._make = make
        
    #model mutator
    @property
    def model(self):
        return self._model
    
    #model getter
    @model.setter
    def model(self, model):
        self._model = model

    def __str__(self):
        return '{} {} {}'.format(self.year, self.make, self.model)
    
##the truck class
class Truck(Vehicle):
##a truck is a vehicle
##a truck is instantiated with a make and model
    #make mutator
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    @property
    def make(self):
        return self._make

    #make getter
    @make.setter
    def make(self, make):
        self._make = make
        
    #model mutator
    @property
    def model(self):
        return self._model
    
    #model getter
    @model.setter
    def model(self, model):
        self._model = model

    #call the vehicle superclass
    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model, year)

    
##the car class
class Car(Vehicle):
##a car is a vehicle
##a car is instantiated with a make and model
    #make mutator
    def __init__(self, make, model):
        self.make = make
        self.model = model
                         
    @property
    def make(self):
        return self._make

    #make getter
    @make.setter
    def make(self, make):
        self._make = make
        
    #model mutator
    @property
    def model(self):
        return self._model
    
    #model getter
    @model.setter
    def model(self, model):
        self._model = model

    #call the vehicle superclass
    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model, year)


##the Dodge Ram class
class DodgeRam(Truck):
    make = "Dodge"
    model = "Ram"

    #call the vehicle subclass
    def __init__(self, year):
        Truck.__init__(self, year, DodgeRam.make, DodgeRam.model)
##a Doodge Ram is a truck
##a Dodge Ram is instantiated with a year
##all Dodge Rams have the same make and model

##the Honda Civic class
class HondaCivic(Car):
    make = "Honda"
    model = "Civic"

    #call the vehicle subclass
    def __init__(self, year):
        Car.__init__(self, year, HondaCivic.make, HondaCivic.model)
##a Honda Civic is a car
##a Honda Civic is instantiated with a year
##all Honda Civics have the same make and model

############################################################
############################################################
## MAIN PROGRAM##

ram = DodgeRam(2016)
print ram

civic1 = HondaCivic(2007)
print civic1

civic2 = HondaCivic(1999)
print civic2
