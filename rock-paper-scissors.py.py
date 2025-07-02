
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

game_images = [rock, paper, scissors]

user_input = int(input("What do you want to choose? Type 0 for rock, 1 for paper, 2 for scissors: "))
print(game_images[user_input])

computer_choice = random.randint(0, 2)
print("Computer's choice:")
print(game_images[computer_choice])

if user_input == computer_choice:
    print("TIED!")
elif user_input == 0 and computer_choice == 2:
    print("YOU WON!")  # Rock beats Scissors
elif user_input == 1 and computer_choice == 0:
    print("YOU WON!")  # Paper beats Rock
elif user_input == 2 and computer_choice == 1:
    print("YOU WON!")  # Scissors beats Paper
else:
    print("YOU LOSE!")



