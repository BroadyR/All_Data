from Tkinter import *

class App(Frame):
    def __init__(self, master):                                     #calls on superclass in tkinter class
        Frame.__init__(self, master)
        self.button1 = Button(master, text="BYE!",\
                              fg="red", command=self.quit)          #fg = color code, command line is what happens when button is pressed
        self.button1.pack(side=LEFT)                                #side = allignment
        self.button2 = Button(master, text="Say something",\
                              command=self.say)                     #say command calls say function
        self.button2.pack(side=LEFT)

    def say(self):
        print "Fruit Loops!"

window = Tk()       #makes window

app = App(window)   #maps window

window.mainloop()   #displays window

