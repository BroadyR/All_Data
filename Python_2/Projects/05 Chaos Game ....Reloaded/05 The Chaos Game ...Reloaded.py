######################################################################################################
# Name: Broady Rivet
# Date: 5/10/19
# Description: makes the fractal shapes
#####################################################################################################
from Tkinter import *
from random import randint
from Fractals import *

#############################################################################################

class ChaosGame(Canvas):
    radius = 0
    def __init__(self, master):
        # constructs the class and creates the radius and color as class properties
        Canvas.__init__(self, master, bg = "white")
        self.pack(fill = BOTH, expand = 1)
        self.vertexRadius = 2
        self.vertexColor = "red"
        self.pointRadius = 0
        self.pointColor = "blue"
        self.dimensions = {"min_x" : 5, "max_x" : 595, "min_y" : 5, "max_y" : 520, \
                "mid_x" : 600 / 2, "mid_y" : 525 / 2}
    # Chooses a fractal
    def make(self, fractalName):
        if (fractalName == "SierpinskiTriangle"):
            fractal = SierpinskiTriangle(self.dimensions)
            for vertex in fractal.vertices:
                self.plot(vertex, self.vertexColor, self.vertexRadius)
            currentPoint = fractal.vertices[0].interpt(fractal.vertices[1], fractal.r)
            for n in range(fractal.numPoints):
                val = randint(0,2)
                if (val == 0):
                    currentPoint = currentPoint.interpt(fractal.vertices[0], fractal.r)
                elif (val == 1):
                    currentPoint = currentPoint.interpt(fractal.vertices[1], fractal.r)
                elif (val == 2):
                    currentPoint = currentPoint.interpt(fractal.vertices[2], fractal.r)
                self.plot(currentPoint, self.pointColor, self.pointRadius)
        elif (fractalName == "SierpinskiCarpet"):
            if (fractalName == "SierpinskiCarpet"):
                fractal = SierpinskiCarpet(self.dimensions)
            for vertex in fractal.vertices:
                self.plot(vertex, self.vertexColor, self.vertexRadius)
            currentPoint = fractal.vertices[0].interpt(fractal.vertices[1], fractal.r)
            for n in range(fractal.numPoints):
                val = randint(0,7)
                if (val == 0):
                    currentPoint = currentPoint.interpt(fractal.vertices[0], fractal.r)
                if (val == 1):
                    currentPoint = currentPoint.interpt(fractal.vertices[1], fractal.r)
                if (val == 2):
                    currentPoint = currentPoint.interpt(fractal.vertices[2], fractal.r)
                if (val == 3):
                    currentPoint = currentPoint.interpt(fractal.vertices[3], fractal.r)
                if (val == 4):
                    currentPoint = currentPoint.interpt(fractal.vertices[4], fractal.r)
                if (val == 5):
                    currentPoint = currentPoint.interpt(fractal.vertices[5], fractal.r)
                if (val == 6):
                    currentPoint = currentPoint.interpt(fractal.vertices[6], fractal.r)
                if (val == 7):
                    currentPoint = currentPoint.interpt(fractal.vertices[7], fractal.r)
                self.plot(currentPoint, self.pointColor, self.pointRadius)
        elif (fractalName == "Hexagon"):
            fractal = Hexagon(self.dimensions)
            for vertex in fractal.vertices:
                self.plot(vertex, self.vertexColor, self.vertexRadius)
            currentPoint = fractal.vertices[0].interpt(fractal.vertices[1], fractal.r)
            for n in range(fractal.numPoints):
                val = randint(0,5)
                if (val == 0):
                    currentPoint = currentPoint.interpt(fractal.vertices[0], fractal.r)
                if (val == 1):
                    currentPoint = currentPoint.interpt(fractal.vertices[1], fractal.r)
                if (val == 2):
                    currentPoint = currentPoint.interpt(fractal.vertices[2], fractal.r)
                if (val == 3):
                    currentPoint = currentPoint.interpt(fractal.vertices[3], fractal.r)
                if (val == 4):
                    currentPoint = currentPoint.interpt(fractal.vertices[4], fractal.r)
                if (val == 5):
                    currentPoint = currentPoint.interpt(fractal.vertices[5], fractal.r)
                self.plot(currentPoint, self.pointColor, self.pointRadius)

    # Plots the points and chooses a color            
    def plot(self, num, color, radius):
        x = num.x
        y = num.y
        self.create_oval(x - radius ** 2, y - radius ** 2, x + radius ** 2, y + radius ** 2, fill = color, \
                outline = color)
##########################################################
################# MAIN ###################################

# the default size of the canvas is 600x525
WIDTH = 600
HEIGHT = 525
# Creates the fractal type as a list
shapes = [ "SierpinskiTriangle", "SierpinskiCarpet", "Hexagon"]

# Creates a window for each fractal shape given
for i in shapes:
    window = Tk()
    window.geometry("{}x{}".format(WIDTH, HEIGHT))
    window.title("The Chaos Game...Reloaded")
    s = ChaosGame(window)
    s.make(i)
    window.mainloop()

