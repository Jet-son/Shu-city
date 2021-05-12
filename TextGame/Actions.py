def inspect(pobj):
    pobj.location.upon_inspect()

def where(pobj):
    print(f"You are currently in {pobj.location.name}")

def move(pobj, locarray):
    # List possible location choices
    pobj.upon_where()

    # Gets direction from user (North, South, East, West)
    direction = input("Please enter the direction you wish to travel")

    while(direction not in pobj.linkedlocs or pobj.linkedlocs[direction] == None):
        if direction == 'back':
            break
        else:
            pobj.location.upon_where()
            direction = input("Please try entering a direction again")

    # Stores location object associated with direction into newloc
    if direction != 'back':
        newloc = pobj.linkedlocs[direction]
    else:
        newloc = pobj.location

    # Uses player object's upon_move function to change players location
    pobj.upon_move(newloc)

    # Print description of new location
    print(pobj.location.description)

def help():
    print("\nAvailable Actions")
    print("-------------------")
    print("move - moves character to available location")
    print("use - use an item")
    print("inspect - inspect surroundings")
    print("where - lists available locations to move to")
    print("stats - lists player stats")
    print("help - prints out help options\n")

def use(pobj):
    pobj.location.upon_use()

def stats(pobj):
    print(f"Name - {pobj.name}")
    print(f"Class - {pobj.charclass}")
    for i in pobj.stats:
        print(f"{i} - {pobj.stats[i]}")
