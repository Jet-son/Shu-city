def pitfall(pobj):
    pobj.remove_health(5)
    if pobj.stats['health'] <= 0:
        print("you fell down a pit and died bruh")
    else:
        print("You fell down a pit and suffered some damage.")
        print(f"Your health is now {pobj.stats['health']}")

def spikes(pobj):
    pobj.remove_health(10)
    if pobj.stats['health'] <= 0:
        print("You were impaled to death homie")
        print("RIP dawg")
    else:
        print("You were impaled but didn't die.")
        print(f"Your health is now {pobj.stats['health']}")