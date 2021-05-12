from Actions import *

actionlist = ["inspect", "move", "help", "where", "use", "stats", "exit"]

def parser(p_input):
    return p_input.split()

def check_action(action):
    return (action in actionlist)

def get_player_action():
    pinput = input(">?").lower()
    pinput = parser(pinput)

    if len(pinput) >= 2:
        act = pinput[0]
        item = pinput[1]
    elif len(pinput) == 1:
        act = pinput[0]
        item = ''
    else:
        print("You did not enter any commands. Type help for list of commands\n")

    if check_action(act):
        return act, item
    else:
        print("Not a valid action. Type help for list of commands\n")

def do_player_action(act, item, player):

    if act == 'move':
        move(player, player.map)
    elif act == 'inspect':
        inspect(player)
    elif act == 'help':
        help()
    elif act == 'exit':
        player.kill()
    elif act == 'where':
        where(player)
    elif act == 'stats':
        stats(player)
    elif act == 'use':
        use(player)