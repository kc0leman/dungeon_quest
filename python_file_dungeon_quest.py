import random

player_name = input("Enter your character name: ")
player_health = 10
inventory = []
game_over = False

treasure = {
    "gold coin": 1,
    "broadsword": 16,
    "katana": 10,
    "brass knuckles": 6,
    "staff": 12,
    "mace": 5,
    "morning star": 20,
    "ruby": 100,
    "emerald": 150,
    "diamond": 200,
    "silver ring": 50,
    "gold ring": 125,
    "brass helmet": 13,
    "steel helmet": 30,
    "plate armor": 75,
    "chain mail legs": 85,
    "leather boots": 25,
    "boots of haste": 300
}

def get_item_phrase(item):
    pair_items = ["brass knuckles", "leather gloves", "iron gloves", "chain mail legs", 
                  "leather legs", "leather boots", "boots of haste"]
    if item in pair_items:
        return f"a pair of {item}"
    elif item[0].lower() in "aeiou":
        return f"an {item}"
    else:
        return f"a {item}"

def interpret_choice(choice):
    choice = choice.lower().strip()
    if choice in ("1", "search for treasure", "search treasure", "search", "option 1", "choose 1"):
        return "1"
    elif choice in ("2", "move to next room", "move next room", "move", "option 2", "choose 2"):
        return "2"
    elif choice in ("3", "check health and inventory", "check health", "health", "inventory", "option 3", "choose 3"):
        return "3"
    elif choice in ("4", "quit the game", "quit", "exit", "option 4", "choose 4"):
        return "4"
    else:
        return None

def show_summary():
    total_value = 0
    print("\n🎉 Game Summary 🎉")
    print(f"Player: {player_name}")
    print(f"Final Health: {player_health}")
    print("Final Inventory:")
    if inventory:
        for item in inventory:
            print(f"- {item} (value: {treasure.get(item, 0)})")
            total_value += treasure.get(item, 0)
    else:
        print("- Empty")
    print(f"\n💰 Total treasure value: {total_value} gold coins")
    print("Thank you for playing!")

def main():
    global player_health, game_over
    room = 1
    
    while True:
        if game_over:
            break
        
        print(f"\n🕋 You are in Room {room}.")
        print("""
Choose either the phrase or number for your choice:
1. Search for treasure
2. Move to next room
3. Check health and inventory
4. Quit the game
""")
        raw_choice = input("What would you like to do? ")
        choice = interpret_choice(raw_choice)

        if choice == "1":
            print("\n🪙 You begin to search the room for treasure...")
            outcome = random.choice(["treasure", "trap"])
            if outcome == "treasure":
                found = random.choice(list(treasure.keys()))
                inventory.append(found)
                print(f"You found {get_item_phrase(found)}. It has been added to your inventory.")
            else:
                print("💥 It's a trap! You lose 2 health points.")
                player_health -= 2
                print(f"❤️ Current Health: {player_health}")
                if player_health <= 0:
                    print("☠️ You have died. Game Over.")
                    game_over = True

        elif choice == "2":
            if room == 5:
                print("\n🚪 You have reached the last room and cannot move further.")
                print("🎉 Ending the game and showing summary...")
                game_over = True
            else:
                room += 1
                print("\n🚪 You move to the next room...")

        elif choice == "3":
            print(f"\n❤️ Health: {player_health}")
            print("🎒 Inventory:")
            if inventory:
                for item in inventory:
                    print(f"- {item}")
            else:
                print("- Empty")

        elif choice == "4":
            print(f"\n👋 Goodbye, {player_name}. Thanks for playing!")
            game_over = True

        else:
            print("\n❌ Invalid choice. Please choose 1–4 or a matching phrase.")

if __name__ == "__main__":
    main()
    show_summary()
    input("\nGame over. Press Enter to exit...")

