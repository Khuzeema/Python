import random

def modify_health(health, amount):
    health += amount
    if health > 100:
        health = 100
    if health < 0:
        health = 0
    return health

def combat(health):
    print("\nYou encounter a monster!")
    action = input("Do you fight or run? (fight/run): ").strip().lower()
    if action == "fight":
        if random.randint(0, 1):  
            print("You defeated the monster!")
        else:
            print("The monster hurt you!")
            health = modify_health(health, -random.randint(10, 30))
    elif action == "run":
        print("You ran back to the starting room.")
    else:
        print("Invalid action! The monster attacked you.")
        health = modify_health(health, -random.randint(10, 20))
    return health

def trap(health):
    print("\nYou triggered a trap! Spikes shoot out from the walls.")
    health = modify_health(health, -random.randint(10, 25))
    return health

def puzzle(health):
    print("\nYou find a puzzle on the wall. Solve it to proceed.")
    puzzle_answer = 10  # Simplified static answer for clarity
    try:
        guess = int(input("What is 3 + 7? Answer: "))
        if guess == puzzle_answer:
            print("Correct! You bypassed the puzzle safely.")
        else:
            print("Wrong answer! The puzzle zaps you with electricity.")
            health = modify_health(health, -random.randint(10, 20))
    except ValueError:
        print("Invalid input! The puzzle zaps you with electricity.")
        health = modify_health(health, -random.randint(10, 20))
    return health

def random_event(health, inventory):
    event = random.choice(["health potion", "key", "bats"])
    if event == "health potion":
        print("\nYou check your surroundings and find a health potion.")
        print("You drink it and recover some health.")
        health = modify_health(health, random.randint(10, 20))
    elif event == "key":
        if "Key" not in inventory:
            print("\nYou find a shiny key on the ground. It might be useful later.")
            inventory.append("Key")
        else:
            print("\nYou see a key, but you already have one.")
    elif event == "bats":
        print("\nA swarm of bats flies at you, scratching and biting.")
        health = modify_health(health, -random.randint(5, 15))
    return health

def dungeon_adventure():
    print("Welcome to the Enhanced Dungeon Adventure!")
    print("Your goal is to find the treasure and escape the dungeon.")
    print("Type your choices to proceed.\n")

    # Starting variables
    health = 100
    treasure_found = False
    inventory = []  # New inventory system

    while health > 0:
        print(f"\nYour health: {health}")
        print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")
        print("You are in a mysterious room with three options:")
        print("1. Open the left door")
        print("2. Open the right door")
        print("3. Check your surroundings")
        choice = input("What do you want to do? (1/2/3): ").strip()

        if choice == "1":
            event = random.choice(["monster", "trap", "puzzle"])
            if event == "monster":
                health = combat(health)
            elif event == "trap":
                health = trap(health)
            elif event == "puzzle":
                health = puzzle(health)

        elif choice == "2":
            print("\nYou open the right door and find a treasure chest!")
            if not treasure_found:
                print("You found the treasure! Now, find a way to escape!")
                treasure_found = True
                inventory.append("Treasure")
            else:
                print("The chest is empty; you've already taken the treasure.")

        elif choice == "3":
            health = random_event(health, inventory)

        else:
            print("Invalid choice! You wasted time and got attacked by bats!")
            health = modify_health(health, -random.randint(5, 10))

        # Check if player has the treasure and exits
        if treasure_found and "Key" in inventory and random.randint(1, 5) == 5:  
            print("\nYou found the exit, used the key, and escaped the dungeon with the treasure!")
            print("Congratulations, you win!")
            return

    print("\nYou ran out of health and succumbed to the dangers of the dungeon. Game over.")

# Start the game
dungeon_adventure()