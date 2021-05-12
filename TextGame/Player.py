class Player:
    name = ''
    charclass = ''
    skills = []
    inventory = {}
    equipment = []
    stats = {'health': 0, 'magic': 0, 'attack': 0, 'defense': 0, 'dexterity': 0}

    def __init__(self, name, charclass, loc, map):
        self.name = name
        self.charclass = charclass
        self.stats['health'] = 25
        self.map = map
        self.linkedlocs = map[loc.name]
        self.location = loc

    def add_health(self, hval):
        self.stats['health'] += hval

    def remove_health(self, hval):
        self.stats['health'] -= hval

    def kill(self):
        self.stats['health'] = 0

    def move(self, loc):
        self.location = loc

    def add_inventory(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def upon_move(self, newloc):
        self.location = newloc
        self.linkedlocs = self.map[newloc.name]

    def upon_where(self):
        cnt = 0
        for i in self.linkedlocs:
            if self.linkedlocs[i]:
                cnt += 1
                print(f"{i}: {self.linkedlocs[i].name}")
        if cnt == 0:
            print("It appears as if you are at a dead end.\n")

