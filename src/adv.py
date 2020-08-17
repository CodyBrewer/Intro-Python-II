from player import Player
import world

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
move = ('n', 's', 'e', 'w', 'north', 'south', 'east', 'west')
take_item_actions = ('get', 'take', 'pickup')
drop_item_actions = ('drop', 'putdown')

player = Player('', world.room['outside'])

# Intro to game
def start_game():
    print("Welcome to Lost Settler's Cave!")
    print("What is your name adventurer?")
    player_name = input("Enter your name:")
    player.name = player_name
    print(f"{player.name} you said? Ah what a great name for a great explorer!")
    print("I bet you're here to search for the pioneers lost treasure from when they crash landed on this here planet.")
    print("To move around the cave use cardinal directions: n, s, e, w.")
    print("Enter x or escape to use your escape rope and escape from the cave quickly")
    print("Enter q or quit  to quit the game")

# Can't move
def deadend():
    print('You walk in that direction, but realize it is a dead end.\n')

# Move player
def move_player(action):
    # move north
    if action in ['n', 'north']:
        if hasattr(player.room, 'n_to'):
            player.room = player.room.n_to
        else:
            deadend()
    # move south
    elif action in ['s', 'south']:
        if hasattr(player.room, 's_to'):
            player.room = player.room.s_to
        else:
            deadend()
    # move east
    elif action in ['e', 'east']:
        if hasattr(player.room, 'e_to'):
            player.room = player.room.e_to
        else:
            deadend()
    # move west
    elif action in ['w', 'west']:
        if hasattr(player.room, 'w_to'):
            player.room = player.room.w_to
        else:
            deadend()

# Game credits
def end_game():
    print(f"Thank you {player.name} for playing an adventure in Lost Settler's Cave!")
    print(f'Credits\n Developed by Cody Brewer\n')
    print(f"Follow me on github to see what else I build! Github: @CodyBrewer")

# Search room logic
def search():
    output = ''
    count = 1
    if len(player.room.items) > 0:
        for item in player.room.items:
            output += f'{count}. {item.name}\n'
            count += 1
        print(f'You search around and find:\n{output}')
    else:
        print(f'You search around and find nothing of value.')

def check_backpack():
    output = ''
    count = 1
    if len(player.items) > 0:
        for item in player.items:
            output += f'{count}. {item}\n'
            count += 1
            print(f'In your backpack you find: \n{output}')
    else:
        print(f'You find nothing in your backpack')

# take item logic
def take_item(action, target):
    if target in world.item:
        target_item = world.item.get(target)
        target_item.on_take_room(player)
    else:
        print(f'Item not here')

# drop item logic
def drop_item(action, target):
    if target in world.item:
        target_item = world.item.get(target)
        if target_item in player.items:
            target_item.on_drop_room(player)
        else:
            print("You don't have that item to drop")

# Start game
start_game()

while True:
    print(f"Welcome to the : {player.room.name}")
    print(f'{player.room.description}\n')
    print(f"What's your move, {player.name}?")
    player_move = input("Enter your move:")
    # sanitize move
    player_move = player_move.lower().split(" ", 1)
    action = player_move[0]
    if len(player_move) == 1:
        target = ""
    else:
        target = player_move[1]

    if action in ['q', 'quit']:
        end_game()
        break
    elif action in ['x', 'escape']:
        player.room = world.room['outside']
    elif action in ['l', 'look']:
        search()
    elif action in move:
        move_player(action)
    elif action in ['b', 'backpack']:
        check_backpack()
    elif action in take_item_actions:
        take_item(action, target)
    elif action in drop_item_actions:
        drop_item(action, target)