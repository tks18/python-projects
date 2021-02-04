# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
res1 = 0
res2 = 0
comb_string = name1+name2

for char in comb_string:
  if char.lower() == 't':
    res1 += 1
  if char.lower() == 'r':
    res1 += 1
  if char.lower() == 'u':
    res1 += 1
  if char.lower() == 'e':
    res1 += 1
  if char.lower() == 'l':
    res2 += 1
  if char.lower() == 'o':
    res2 += 1
  if char.lower() == 'v':
    res2 += 1
  if char.lower() == 'e':
    res2 += 1

fin_res = res1 + res2;

if(fin_res < 10) or (fin_res > 90):
  print(f"Your score is {name1}x{name2}, you go together like coke and mentos.")
elif (fin_res > 40) and (fin_res < 50):
  print(f"Your score is {name1}y{name2}, you are alright together")
else:
  print(f'Your Love Score is {fin_res}')

