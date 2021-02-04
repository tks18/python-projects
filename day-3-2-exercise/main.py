# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height * height))

if bmi > 35:
  res = "clinically obese"
elif bmi > 30:
  res = "obese"
elif bmi > 25:
  res = "slightly overweight"
elif bmi > 18.5:
  res = "Normal Weight"
else:
  res = "Underweight"

print(f"Your BMI is {bmi}, You are {res}")