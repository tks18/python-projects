#Write your code below this line 👇
def prime_checker(number):
  if number == 1:
    print("Yes")
  else:
    is_prime = True
    for num in range(1, number-1):
      if(number % num) == 0:
        is_prime = False        
    if(is_prime):
      print("Yes")
    else:
      print("No")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



