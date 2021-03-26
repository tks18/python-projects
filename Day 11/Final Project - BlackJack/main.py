############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from art import logo
from replit import clear

def deal_card(cards_list):
  rand = random.choice(cards_list)
  return rand

def calculate_score(cards_list):
  score = 0
  if sum(cards_list) == 21:
    score = 0
  else:
    for num in cards_list:
      if(num == 11):
        if(score > 21):
          score += 1
        else:
          score += num
      else:
        score += num
  return score

def compare(user, comp):
  if(user == comp):
    print("Its a Draw !!!!")
  elif(comp == 0) or (user > 21):
    print("Computer Wins")
  elif(user == 0) or (comp > 21):
    print("User Winss !!")
  elif(comp > user):
    print("Computer Wins")
  elif(user > comp):
    print("User Winss")

game_continues = True
while game_continues:
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  user_cards = []
  computer_cards = []

  for each in range(2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))

  another_one_is_there = True
  while another_one_is_there:
    comp_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    print(f"You Cards - {user_cards}, Current Score - {user_score}")
    print(f"Computer's First Card is {computer_cards[0]}")
    if(user_score > 21): 
      print("You Score Above 21, You Lose")
      another_one_is_there = False
    elif (comp_score == 0):
      print("Computer Scores a 21, You Lose")
      another_one_is_there = False
    else:
      another_one = input("Do You want to Draw Another Card from the Deck ? (y/n)").lower()
      if(another_one == 'y'):
        user_cards.append(deal_card(cards))        
      else:
        another_one_is_there = False  

  comp_score = calculate_score(computer_cards)
  while comp_score < 17:
    computer_cards.append(deal_card(cards))
    comp_score = calculate_score(computer_cards)

  print(f"Your Final hand: {user_cards}, Final Score is {user_score}")
  print(f"Computer's Final hand: {computer_cards}, Computer's Score is {comp_score}")
  compare(user_score, comp_score);
  continues = input("Do You want to Play Another Game? (y/n)").lower()
  if(continues == 'n'):
    game_continues = False
  else:
    clear();
