from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
move = ('n', 's', 'e', 'w')
player = Player('', room['outside'])

def start_game():
    print("Welcome to Lost Settler's Cave!")
    print("What is your name adventurer?")
    player_name = input("Enter your name:")
    player.name = player_name
    print(f"{player.name} you said? Ah what a great name for a great explorer!")
    print("I bet you're here to search for the pioneers lost treasure from when they crash landed on this here planet.")
    print("To move around the cave use cardinal directions: n, s, e, w.")
    print("Type x to use your escape rope and escape from the cave quickly")
    print("Type q to quit the game")

def deadend():
    print('You walk in that direction, but realize it is a dead end.\n')

def move_player(action):
    # move north
    if action == 'n':
        if hasattr(player.room, 'n_to'):
            player.room = player.room.n_to
        else:
            deadend()
    # move south
    elif action == 's':
        if hasattr(player.room, 's_to'):
            player.room = player.room.s_to
        else:
            deadend()
    # move east
    elif action == 'e':
        if hasattr(player.room, 'e_to'):
            player.room = player.room.e_to
        else:
            deadend()
    # move west
    elif action == 'w':
        if hasattr(player.room, 'w_to'):
            player.room = player.room.w_to
        else:
            deadend()

def end_game():
    print(f"Thank you {player.name} for playing an adventure in Lost Settler's Cave!")
    print(f'Credits\n Developed by Cody Brewer\n')
    print(f"Follow me on github to see what else I build! Github: @CodyBrewer")
    

start_game()

while True:
    print(f"Welcome to the : {player.room.name}")
    print(f'{player.room.description}\n')
    print(f"What's your move, {player.name}?")
    player_move = input("Enter your move:")
    # sanitize move
    player_move = player_move.lower().split(" ", 1)

    action = player_move[0]
    if action == 'q':
        end_game()
        break
    if action == 'x':
        player.room = room['outside']
    if action in move:
        move_player(action)
    