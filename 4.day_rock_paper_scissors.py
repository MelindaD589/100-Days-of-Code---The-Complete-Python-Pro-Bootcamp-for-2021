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

import random

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
hand = [rock, paper, scissors]
print(f'You chose:\n {hand[your_choice]}')

computer_chose = random.randint(0, 2)
print(f'Computer chose:\n {hand[computer_chose]}')

if your_choice >= 3 or your_choice < 0:
    print("Type 0 or 1 or 2.")
elif your_choice == 0 and computer_chose == 2:  
    print('You win')
elif your_choice == 2 and computer_chose == 0:
    print('You lose')
elif your_choice > computer_chose:
    print('You win')
elif computer_chose > your_choice:
    print('You lose')
elif your_choice == computer_chose:
    print('It is a draw')



