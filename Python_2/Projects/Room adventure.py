##############################################################################
## Name: Broady Rivet                                                       ##
## Date: 1/7/19                                                             ##
## Description:                                                             ##
##############################################################################

#blueproint for room
class Room(object):
    #constructor
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exitLocation = []
        self.items = []
        self.itemDescriptions = []
        self.grabbable = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocation(self):
        return self._exitLocation

    @exitLocation.setter
    def exitLocation(self, value):
        self._exitLocation = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbable(self):
        return self._grabbable

    @grabbable.setter
    def grabbable(self, value):
        self._grabbable = value

    #################################
    #adds and exit to the room
    def addExit(self, exit, room):
        self._exits.append(exit)
        self._exitLocation.append(room)

    #adds an item to the room
    def addItem(self, items, desc):
        self._items.append(items)
        self._itemDescriptions.append(desc)

    #makes items grabbable
    def addGrabbable(self, items):
        self._grabbable.append(items)

    #removes item from inventory
    def delGrabbable(self, items):
        self._grabbable.remove(items)

    def __str__(self):
        s = "You are in {}. \n".format(self.name)
        s += "You see:"
        for item in self.items:
            s += item + " "
        s += "\n"
        s += "Exits:"
        for exit in self._exits:
            s += exit + " "
        return s
def createRooms():
    global currentRoom

    #create rooms
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    #add the exits to room 1
    r1.addExit("east", r2)
    r1.addExit("south", r3)

    #add grabbables to room 1
    r1.addGrabbable("key")

    #add item to room 1
    r1.addItem("chair", "Its a vacant chair, good job")
    r1.addItem("table", "Its a table. A golden key rest on top.")

    #########
    #add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)

    # add items to room 2
    r2.addItem("rug", "Its a nice rug with a dead mouse under it.")
    r2.addItem("fireplace", "It is a log fire place that seems to be lit \(.__.)/")

    #add gabbables ro room 2
    r2.addGrabbable("dead mouse")
    ##########
    #add exits to room 3
    r3.addExit("north",r1)
    r3.addExit("east",r4)

    #add grabables to room 3
    r3.addGrabbable("book")

    # add items to room 3

    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "There is nothing special about this statue.")
    r3.addItem("desk", "The statue is resting on it. So is the book.")

    ##########
    # add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None) # DEATH!

    # add grabbables to room 4
    r4.addGrabbable("6-pack")

    # add items to room 4

    r4.addItem("brew_rig", "Gourd is brewing some sort of beverage on the breq rig. A 6-pack is resting beside it.")

    #set room 1 as the starting room
    currentRoom = r1

#death function
def death():
	print(" " * 17 + "u" * 7)
	print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
	print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
	print(" " * 9 + "u" + "$" * 21 + "u")
	print(" " * 8 + "u" + "$" * 23 + "u")
	print(" " * 7 + "u" + "$" * 25 + "u")
	print(" " * 7 + "u" + "$" * 25 + "u")
	print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
	print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
	print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
	print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
	print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
	print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
	print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
	print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
	print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
	print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
	print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
	print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
	print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
	print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
	print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
	print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
	print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
	print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
	print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")


###############################################
#START THE GAME!
inventory = []
createRooms()

#play
while (True):
    status = "{}\nYou are carrying:{}\n".format(currentRoom, inventory)
    if (currentRoom == None):
        death()
        break
    print ("=======================================================")
    print (status)

    #prompt for player input
    action = input("What to do?")
    #set inputs to lowercase
    action = action.lower()
    #game's exit
    if (action == "quit" or action == "exit" or action == "bye"):
        break

    #set default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
    words = action.split()
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]
        if (verb == "go"):
            response = "Invalid exit"
            for i in range (len(currentRoom.exits)):
                if (noun == currentRoom.exits[i]):
                    currentRoom = currentRoom.exitLocation[i]
                    response = "Room changed"
                    break
        elif (verb == "look"):
            response = "I don't see that item."
            for i in range(len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = currentRoom.itemDescriptions[i]
                    break
        elif (verb == "take"):
            response = "I don't see that item."
            for grabbable in currentRoom.grabbable:
                if (noun == grabbable):
                    inventory.append(grabbable)
                    currentRoom.delGrabbable(grabbable)
                    response = "Item grabbed."
                    break
            if (noun == "6-pack"):
                response = "You took and drank the 6-pack....\nYou became drunk, fell, hit your head, and died."
                death()
                break
            if (noun == "dead mouse"):
               repsonse = "The mouses body popped and splattered on you... that's discusting."
            for i in range(len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = "This item is too heavy to take because you are a weakling."
                    break


    #display response
    print ("\n{}".format(response))
