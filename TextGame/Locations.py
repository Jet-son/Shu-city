class Castle(object):
    name = "Castle"
    description = "This is a castle."

    def __str__(self):
        return self.name

    def upon_inspect(self):
        print("You are currently standing in a castle.")
        print("There seems to be a gate ahead.")
        print("Maybe you can open it?")

    def upon_use(self):
        print(f"You can not use {self.name}")


class Castle_Gate(object):
    name = "Castle Gate"
    description = "You come upon a large wooden gate for the castle"

    def __str__(self):
        return self.name

    def upon_inspect(self):
        print("This is a castle gate. I wonder how I open it?")

    def upon_use(self):
        print(f"You can not use {self.name}")

class Castle_Grounds(object):
    name = "Castle Grounds"
    description = "You arrive at the castle grounds"

    def __str__(self):
        return self.name

    def upon_inspect(self):
        print("Sure is a nice castle innit?")

    def upon_use(self):
        print(f"You can not use {self.name}")

class Graveyard(object):
    name = "Graveyard"
    description = "You arrive at the Graveyard"

    def __str__(self):
        return self.name

    def upon_inspect(self):
        print("Oh wow, a spooky graveyard")
        print("I hope I don't see a G-G-G-Ghost...")

    def upon_use(self):
        print(f"You can not use {self.name}")

class Castle_Entrance(object):
    name = "Castle Entrance"
    description = "You arrive at the Castle Entrance"

    def __str__(self):
        return self.name

    def upon_inspect(self):
        print("You have entered the castle, sure is a big place")

    def upon_use(self):
        print(f"You can not use {self.name}")

map = {
    "Castle": {"North": Castle_Gate(), "South": None, "East": Castle_Grounds, "West": Graveyard()},
    "Castle Gate": {"North": Castle_Entrance(), "South": Castle(), "East": None, "West": None},
    "Graveyard": {"North": None, "South": None, "East": None, "West": None},
    "Castle Entrance": {"North": None, "South": None, "East": None, "West": None},
    "Castle Grounds": {"North": None, "South": None, "East": None, "West": None},

}