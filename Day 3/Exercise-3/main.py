# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
mod1 = year % 4
mod2 = year % 100
mod3 = year % 400
print(mod1, mod2, mod3)
if mod1 == 0:
  if mod2 == 0 and mod3 == 0:
    print("Its a Leap Year")
  else:
    print("Not a Leap Year")
else:
  print("Not a Leap Year")