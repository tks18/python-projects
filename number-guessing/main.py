import random

print("Welcome to Number Guessing Game ")
print("I am Thinking of a Number between 1 and 100 ");
comp_num = random.randint(0, 100);
print(comp_num)
attempts = 0
difficulty = input("Choose a Difficult, Type 'easy' or 'hard': ").lower();
if(difficulty == 'easy'):
  attempts = 10
  print("You have 10 Attempts remaining to Guess the Number")
else:
  attempts = 5
  print("You have 5 Attempts remaining to Guess the Number")

while attempts > 0:
  guess = int(input("Make a Guess: "));
  if(guess > comp_num):
    print("Too High")
    attempts -= 1
    if(attempts == 0):
      print(f"You Lose, You didn't Guess the Number")
    else:
      print(f"You have only {str(attempts)} left to Guess")
  elif(guess < comp_num):
    print("Too Low")
    attempts -= 1
    if(attempts == 0):
      print(f"You Lose, You didn't Guess the Number")
    else:
      print(f"You have only {str(attempts)} left to Guess")
  elif(guess == comp_num):
    print("You have Won it !!")
    attempts = 0