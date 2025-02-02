import time
import random

class Crop:
    def __init__(self, name, grow_time, price):
        self.name = name
        self.grow_time = grow_time  # Time it takes to grow the crop
        self.price = price          # Price when the crop is harvested
        self.watered = False        # Whether the crop is watered or not
        self.growth_stage = 0       # Growth stage (0 - not planted, 1 - growing, 2 - ready to harvest)
    
    def water(self):
        self.watered = True
        print(f"You watered your {self.name} crop!")

    def grow(self):
        if self.growth_stage == 0:
            return "Crop not planted."
        if not self.watered:
            return f"Your {self.name} crop is not watered. It won't grow."
        
        self.growth_stage += 1
        self.watered = False  # Reset watered status after growing
        return f"{self.name} is growing. Growth stage: {self.growth_stage}"

    def harvest(self):
        if self.growth_stage == 2:
            print(f"Harvesting your {self.name} crop for {self.price} coins!")
            return self.price
        else:
            return f"{self.name} is not ready to harvest yet."


class Farm:
    def __init__(self):
        self.coins = 100  # Starting coins
        self.crops = []
        self.plant_seeds()

    def plant_seeds(self):
        print("Welcome to your farm!")
        print("You have 100 coins to start.")
        print("You can plant crops here. Each crop has a different cost.")
        
        crops_list = [
            Crop("Tomato", 3, 50),
            Crop("Carrot", 2, 30),
            Crop("Wheat", 4, 70)
        ]
        
        for index, crop in enumerate(crops_list):
            print(f"{index + 1}. {crop.name} (Growth time: {crop.grow_time} turns, Price: {crop.price})")
        
        choice = int(input("Which crop would you like to plant? (1, 2, or 3): ")) - 1
        selected_crop = crops_list[choice]
        
        if self.coins >= selected_crop.price:
            self.coins -= selected_crop.price
            self.crops.append(selected_crop)
            print(f"You planted {selected_crop.name}!")
        else:
            print("You don't have enough coins to plant that crop.")

    def next_turn(self):
        print("\nNext turn... Crops are growing!")
        for crop in self.crops:
            print(crop.grow())
        
    def water_crops(self):
        print("\nWater your crops!")
        for index, crop in enumerate(self.crops):
            print(f"{index + 1}. {crop.name}")
        
        choice = int(input("Which crop would you like to water? (Enter number): ")) - 1
        self.crops[choice].water()

    def harvest_crops(self):
        print("\nHarvest your crops!")
        for crop in self.crops:
            if crop.growth_stage == 2:
                print(crop.harvest())
                self.coins += crop.price
            else:
                print(f"{crop.name} is not ready yet.")
    
    def game_status(self):
        print(f"\nYou have {self.coins} coins.")
        print("Your crops:")
        for crop in self.crops:
            print(f"{crop.name}: Growth stage {crop.growth_stage}, Watered: {crop.watered}")


def main():
    farm = Farm()
    
    while True:
        print("\n--- FARM SIMULATION ---")
        print("1. Water crops")
        print("2. Grow crops")
        print("3. Harvest crops")
        print("4. View status")
        print("5. Quit")

        choice = int(input("Choose an action: "))

        if choice == 1:
            farm.water_crops()
        elif choice == 2:
            farm.next_turn()
        elif choice == 3:
            farm.harvest_crops()
        elif choice == 4:
            farm.game_status()
        elif choice == 5:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
