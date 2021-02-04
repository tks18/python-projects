#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

billAmt = float(input("Enter the Total Amount of Bill: "))
billPers = int(input("Enter the Number of Persons to Split: "));
billTip = float(int(input("Enter the tip Percentage: ")) / 100);

billSplit = round(billAmt / billPers, 2)
tipPerS = round(billSplit * billTip, 2);

print(f"Your Bill Amt is Rs.{billSplit}")
print(f"Your Tip is Rs.{tipPerS}");
print(f"Your Total Outflow is {billSplit + tipPerS}");