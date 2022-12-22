import random 

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
#lsit for the game
game = [rock, paper, scissors]

choice = int(input("What do you choose?\n Type 0 for rock, 1 for Paper, and 2 for Scissors.\n"))

print("You chose:" + game[choice])
0

comp_choice = random.randint(0,2)
print("Computer chose:")
print(game[comp_choice])

# game rules, deciding who wins 
#user wins
if choice == 0 and comp_choice == 2: #a- rock, b- scissors
    print("You win")
elif choice == 1 and comp_choice == 0: #a- paper, b-rock
    print("You win")
elif choice == 2 and comp_choice == 1: # a-scissors, b-paper
    print("You win")
#user loses
if choice == 2 and comp_choice == 0: #b- rock, a- scissors
    print("You lose")
elif choice == 0 and comp_choice == 1: #b- paper, a-rock
    print("You lose")
elif choice == 1 and comp_choice == 2: # b-scissors, a-paper
    print("You lose")
elif choice == comp_choice:
    print("It's a draw") #draw
else:
    print("You chose an invalid number, you lose!")
