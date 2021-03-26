import art
import random
from replit import clear
from game_data import data as game_data

currentList = []
prevWin = {}
score = 0

def generate_randData(dataList):
    if(len(dataList) > 1):
      randInt = random.randint(0, len(game_data) - 1)
      while randInt in dataList:
        randInt = random.randint(0, len(game_data) - 1)
      dataList.append(randInt)
      return randInt
    else:
      firstInt = random.randint(0,len(game_data) - 1)
      secInt = random.randint(0, len(game_data) - 1)
      while secInt == firstInt:
        secInt = random.randint(0, len(game_data) - 1)
      dataList.append(firstInt)
      dataList.append(secInt)
      return [firstInt, secInt]

def printVsList(dict1, dict2):
  print(f"Compare A: {dict1['name']}, {dict1['description']}, from {dict1['country']}")
  print(art.vs)
  print(f"Compare B: {dict2['name']}, {dict2['description']}, from {dict2['country']}")

def correctOrNot(guess, a, b):
  if(a > b):
    return guess == 'a'
  else:
    return guess == 'b'

gameIsRunning = True;
while gameIsRunning:
  print(art.logo)
  isCorrect = False
  print(f"Your Current Score is {score}")
  if(len(currentList) > 1):
    randData = generate_randData(currentList)
    data1 = prevWin
    data2 = game_data[randData]
    prevWin = data2
    printVsList(data1, data2)
    aorB = input("Who has More Followers? Type A or B: ").lower()
    isCorrect = correctOrNot(aorB, data1["follower_count"], data2["follower_count"]);
  else:
    randData = generate_randData(currentList)
    data1 = game_data[randData[0]]
    data2 = game_data[randData[1]]
    prevWin = data2
    printVsList(data1, data2)
    aorB = input("Who has More Followers? Type A or B: ").lower()
    isCorrect = correctOrNot(aorB, data1["follower_count"], data2["follower_count"]);
  
  clear()

  if isCorrect:
    score += 1
  else:
    gameIsRunning = False

if not gameIsRunning:
  print(art.logo)
  print(f"You Lose with Score - {score}")