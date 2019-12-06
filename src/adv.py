from room import Room
from player import Player
from item import Item

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
chamber! Fortunately, you're the first person to come upon this treasure and take all 
the loot! The only exit is to the south."""),
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

# adds itemsNrf = room['foyer']
rf = room['foyer']
rf.addItem(Item("wand", "I'm a wand", 3))
rf.addItem(Item("sword", "I'm a sword", 4))

rOut = room['outside']
rOut.addItem(Item("bottlecap", "I'm a bottlecap", -1))
rOut.addItem(Item("healthkit", "I'm a healthkit", 5))

rOver = room['overlook']
rOver.addItem(Item("spyglass", "I'm a spyglass", 3))
rOver.addItem(Item("rock", "I'm a rock", -1))

rN = room['narrow']
rN.addItem(Item("painting", "I'm a painting", 9))
rN.addItem(Item("candy", "I'm candy", 4))

rT = room['treasure']
rT.addItem(Item("diamonds", "I'm some diamonds", 50))
rT.addItem(Item("magic", "I'm magic", 50))


player = Player("Mage Laura", room['outside'])


while True: 
    print(f"{player}")
    print(f"You are standing in the {player.current_room.name}")
    print(f"{player.current_room.desc}")
    print(f"{player.current_room}")
    userInput = input("enter a direction or command : ")
    wordList=userInput.split(" ",userInput.count(" "))
    if len(wordList) == 1:
        if userInput == 'n':
            if player.current_room.n_to is None:
                print("You can't go that direction from here.")
            else:
                player.current_room = player.current_room.n_to
                print((f'You are now in {player.current_room.name}'))
        elif userInput == 's':
            if player.current_room.s_to is None:
                print("You can't go that direction from here.")
            else:
                player.current_room = player.current_room.s_to
                print((f'You are now in {player.current_room.name}'))
        elif userInput == 'e':
            if player.current_room.e_to is None:
                print("You can't go that direction from here.")
            else:
                player.current_room = player.current_room.e_to
                print((f'You are now in {player.current_room.name}'))
        elif userInput == 'w':
            if player.current_room.w_to is None:
                print("You can't go that direction from here.")
            else:
                player.current_room = player.current_room.w_to
                print((f'You are now in {player.current_room.name}'))
        elif userInput == 'i' or userInput == 'inventory':
            if player.items:
                for item in player.items:
                    print(f"You have a {item.name}")
            else:
                print("player has no items")
        else:
            print("I don't recognize that command!")
    elif len(wordList) == 2:
        verbChoice = wordList[0]
        itemChoice = wordList[1]
        if verbChoice == 'get' or verbChoice == 'take':
            for item in player.current_room.items:
                if item.name == itemChoice:
                    player.addItem(item)
                    item.onTake(itemChoice)
                    player.addPoints(item.points)
                    player.current_room.removeItem(item)
                
        elif verbChoice == 'drop':
            for item in player.items:
                if item.name == itemChoice:
                    player.removeItem(item)
                    item.onDrop(item.name)
                    player.removePoints(item.points)
                    player.current_room.addItem(item)
        else:
            print("I don't recognize that command!")


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
