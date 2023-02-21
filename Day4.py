import random

random_side = random.randint(0,1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]


# Banker Roulette
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{names[random.randint(0,len(names)-1)].title()} will pay the bill.")

# Treasure map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

map[int(position[1])-1][int(position[0])-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")


# rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choices = [rock, paper, scissors]

computer_choice = random.randint(0,len(choices)-1)

print(choices[player_choice])

print(f"Computer chose:\n{choices[computer_choice]}")

if player_choice == computer_choice:
    print("Draw")
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print("You Won!")
else:
    print("You lose")
