import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]
wordOpt = ["rock", "paper", "scissors"]
inp = int(input("Select 0 for Rock, 1 for Paper, 2 for Scissors"))
rand_int = random.randint(0, 2)
userOption = options[inp]
compOption = options[rand_int]
userWordOpt = wordOpt[inp]
compWordOpt = wordOpt[rand_int]

all_res = f"""
 Computer Chose {compWordOpt}
 {compOption}
 You Chose {userWordOpt}
 {userOption}
"""

if compWordOpt == userWordOpt:
    print(all_res)
    print("Its a Draw")
elif userWordOpt == "paper" and compWordOpt == "rock":
    print(all_res)
    print("You won")
elif userWordOpt == "rock" and compWordOpt == "scissors":
    print(all_res)
    print("You Won")
elif userWordOpt == "scissors" and compWordOpt == "paper":
    print(all_res)
    print("You won")
else:
    print(all_res)
    print("You Lose")
