# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
letCorrectAge = int(age);
ageInDays = letCorrectAge*365
ageInWeeks = letCorrectAge*52
ageInMonths = letCorrectAge*12

leftDays = (90*365) - ageInDays
leftWeeks = (90*52) - ageInWeeks
leftMonths = (90*12) - ageInMonths

print(f"You have Currently {leftDays} Days, {leftWeeks} Weeks and {leftMonths} Months Left to Live");





