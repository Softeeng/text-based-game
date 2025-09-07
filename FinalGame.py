# The Phantom Curse Text Adventure Game
# Description:
# Explore the mansion to collect seven cursed artifacts
# Avoid the phantom in the attic until you have all items
# Use commands to move, collect items, and to check inventory.

# Room Layout
rooms = {
  'Foyer': {'North': 'Library', 'South': 'Basement'},
  'Library': {'South': 'Foyer', 'East': 'Ballroom'},
  'Dining Room': {'West': 'Ballroom', 'South': 'Kitchen'},
  'Kitchen': {'North': 'Dining Room'},
  'Ballroom': {'West': 'Library', 'East': 'Dining Room', 'North': 'Study'},
  'Study': {'South': 'Ballroom', 'East': 'Master Bedroom'},
  'Basement': {'North': 'Foyer'},
  'Master Bedroom': {'West': 'Study', 'North': 'Attic'},
  'Attic':{'South': 'Master Bedroom'}
}

# Items Located in Rooms
items = {
  'Library': 'Dusty Tome',
  'Dining Room': 'Silver Goblet',
  'Kitchen': 'Ancient Knife',
  'Ballroom': 'Broken Violin',
  'Study': 'Pocket Watch',
  'Master Bedroom': 'Velvet Ring Box',
  'Basement': 'Cursed Mirror'
}

def print_intro():
  print("Welcome to The Phantom Curse")
  print("\nLegend speaks of an old mansion hidden in the shadowy forest..long abandoned...")
  print("They say it holds seven cursed artifacts - each one key to confronting the ghostly Phantom in the attic.")
  print("Many have entered and tested their fate...but none have returned")
  print("Tonight, armed with courage and a flashlight, it's your turn to take the test.")
  print("Collect all seven items to break the curse - but beware...")
  print("If you face the Phantom before you're ready...IT'S OVER.")
  print("\nType 'help' at any time for commands.\n")

def show_room(room,inventory):
  print(f"\nYou are in the {room}")
  print(f"Inventory: {', '.join(inventory)}")
  directions = rooms[room].keys()
  print("You can go:" + ",".join(directions))
  if room in items and items [room] not in inventory:
    print(f"You see a {items[room]} here.")

def get_command():
  return input("\nEnter a command:").strip().lower()

def handle_command(command, current_room, inventory):
  if command.startswith("go "):
    direction = command[3:].strip().capitalize()
    if direction in rooms[current_room]:
      return rooms[current_room][direction], inventory
    else:
      print("You can't go that way")
      return current_room, inventory
  elif command == "get item":
    if current_room in items:
      item = items[current_room]
      if item in inventory:
        print(f"You already picked up the {item}.")
      else:
        inventory.append(item)
        print(f"You picked up the {item}.")
    else:
      print("There's no item to pick up here.")
    return current_room, inventory
  elif command == "inventory": 
    if inventory:
      print("Your inventory:", ",".join(inventory))
    else:
      print("Your inventory is empty.")
    return current_room, inventory
  elif command == "help":
    print("\nCommands:")
    print(" go North, South, East, West - Move between rooms")
    print(" get item - Collect the item in the room")
    print(" inventory - Show collected items")
    print(" quit - Exit the game\n")
    return current_room, inventory
  elif command == "quit":
    print("Thanks for playing! Goodbye.")
    exit()
  else:
    print("Invalid command. Type 'help' for options.")
    return current_room, inventory

def check_attic (current_room, inventory):
  if current_room == "Attic":
    print("\nYou enter the Attic...")
    if len(inventory) == 7:
      print("Armed with all 7 artifacts, you face the Phantom and break the curse. You win!")
    else:
      print("You are not prepared...the Phantom steals your soul...You lose.")
    return True # End game if in attic
  return False # Continue game if not in attic

def main():
  current_room = 'Foyer'
  inventory = []
  print_intro()
  while True:
    show_room(current_room, inventory)
    command = get_command()
    current_room, inventory = handle_command(command, current_room, inventory)
    if check_attic(current_room, inventory):
      break

if __name__ == "__main__":
  main()
