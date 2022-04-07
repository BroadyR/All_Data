######################################################################################################################
# Name: Broady Rivet
# Date: 5/10/19
# Description: creates point class and fractals super and sub class
######################################################################################################################
from Tkinter import *
from random import randint

###############################################################################################

# the 2D point class
class Point(object):

        # Initialized the class and defined 0 as the default answer for each component
        def __init__(self, x=0.0, y=0.0):
                self.x = x
                self.y = y

        # Created the mutators and accessors for the components
        @property
        def x(self):
            return float(self._x)

        @x.setter
        def x(self, point):
            self._x = point

        @property
        def y(self):
            return float(self._y)

        @y.setter
        def y(self, point):
            self._y = point

        # The points of each object is put into its own variable and used to find the distance
        def dist(self, value):  
            x1 = self.x
            y1 = self.y
            x2 = value.x
            y2 = value.y

            return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (.5)

        # The points of each object is put into its own variable and used to find the midpoint and returned as a Point object
        def midpt(self, value):  
            x1 = self.x
            y1 = self.y
            x2 = value.x
            y2 = value.y

            return Point(((x1 + x2) / 2), ((y1 + y2) / 2))

        def interpt(self, other, r):
            rx = r
            if (self.x > other.x):
                rx = 1.0 -r

            ry = r
            if (self.y > other.y):
                ry = 1.0 - r

            x = abs(self.x - other.x) * rx + min(self.x, other.x)
            y = abs(self.y - other.y) * ry + min(self.y, other.y)

            return Point (x, y)
        
        # This magic function was used to change the points into a string
        def __str__(self):  
            return "({},{})".format(self.x, self.y)

# Fractal superclass that inherits from Canvas and the Point superclasses
class Fractal(Canvas,Point):
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.numPoints = 50000
        self.r = 0.5
        self.vertices = []

    def frac_x(self, r):
        return int((self.dimensions["max_x"] - self.dimensions["min_x"]) * r) + self.dimensions["min_x"]

    def frac_y(self, r):
        return int((self.dimensions["max_y"] - self.dimensions["min_y"]) * r) + self.dimensions["min_x"]

#triangle's class
class SierpinskiTriangle(Fractal):

    def __init__(self, dimensions):
        Fractal.__init__(self, dimensions)
        self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["min_y"]))
        self.vertices.append(Point(self.dimensions["min_x"], self.dimensions["max_y"]))
        self.vertices.append(Point(self.dimensions["max_x"], self.dimensions["max_y"]))

#Carpet's class
class SierpinskiCarpet(Fractal):

    def __init__(self, dimensions):
        Fractal.__init__(self, dimensions)
        self.numPoints = 100000
        self.r = 0.66
        self.vertices.append(Point(self.dimensions["min_x"], self.dimensions["min_y"]))
        self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["min_y"]))
        self.vertices.append(Point(self.dimensions["max_x"], self.dimensions["min_y"]))
        self.vertices.append(Point(self.dimensions["min_x"], self.dimensions["mid_y"]))
        self.vertices.append(Point(self.dimensions["max_x"], self.dimensions["mid_y"]))
        self.vertices.append(Point(self.dimensions["min_x"], self.dimensions["max_y"]))
        self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["max_y"]))
        self.vertices.append(Point(self.dimensions["max_x"], self.dimensions["max_y"]))

#Hexagon's class
class Hexagon(Fractal):

    def __init__(self, dimensions):
        Fractal.__init__(self, dimensions)
        self.r = 0.665
        self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["min_y"]))
        self.vertices.append(Point(self.dimensions["max_x"], self.frac_y(0.25)))
        self.vertices.append(Point(self.dimensions["min_x"], self.frac_y(0.25)))
        self.vertices.append(Point(self.dimensions["min_x"], self.frac_y(0.75)))
        self.vertices.append(Point(self.dimensions["max_x"], self.frac_y(0.75)))
        self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["max_y"]))







