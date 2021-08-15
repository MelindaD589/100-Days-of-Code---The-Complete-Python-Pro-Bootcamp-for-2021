# Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choise1 = input('You are at a cross road. Where do you want to go? Type "Left" or "Right"\n').lower()
if choise1 == "right":
    choise2 = input("A troll mocked you, so you throw a stone on him.\n This stone is Denmark's biggest granite stone, it called Bolundstenen.\n You continue your trip. Do you go to Roskilde or Copenhagen?\n").lower()
    if choise2 == "roskilde":
        choice3 = input("You arrived to Roskilde, where you find the time-travelling boots.\n It will take you to the viking times.\n Who will help you in the viking battle? Thor or Loki or Odin?\n").lower()
        if choice3 == "thor":
            print("Thor helped you and took you to Tisvilde, Thor's city, where you drink from St. Helene's spring. You heal. You Win!")
        elif choice3 == "odin":
            print("Today Odin is busy. Game Over.")
        else: 
            print("Loki refuses to help. Game Over.")
    else:
        print("The big flood washed away everything in downtown Copenhagen. Game Over.")
else:
    print("Your superpower was not enough. Game Over.")