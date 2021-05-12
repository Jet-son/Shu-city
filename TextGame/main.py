import Player as p
import Locations as l
import Traps as t
from Gamefunc import *

# Global vars
WIN = False

# Print game title
print("\n-----------------------------------")
print("Welcome to INSERT GAME TITLE HERE")
print("---------------------------------\n")

# Get player information
name = input("What should we call you? ")
charclass = input("Wat class do you want to be? ")

# Initialize player information and location
loc = l.Castle()
player = p.Player(name, charclass, loc, l.map)

# Greeting
ans = ("Do you wish to begin your Quest (Y/N)? ")
if ans == 'N':
    player.kill()
else: pass

# Start main game loop
while player.stats['health'] > 0:
    act, item = get_player_action()
    do_player_action(act, item, player)

# Game end
if WIN:
    print(f"Congrats {player.name}, you have completed the quest")
    print("THE END?")
else:
    print("Lame bro. Try again ")
    print("GAME OVER")