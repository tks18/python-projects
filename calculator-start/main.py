from art import logo

print(logo)

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mult(a, b):
  return a * b

def div(a, b):
  return a / b

mathFunc = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div,
}

is_another_needed = True
prev_ans = 0
new_calc = False

while is_another_needed:
  if(prev_ans > 0) and not new_calc:
    num1 = prev_ans
    print(f"Enter a Operation to do with {num1}")
  else:
    num1 = float(input("Enter the First Number  "))
    for func in mathFunc:
      print(func)
  oper = input("Enter any operation from the Above  ");
  num2 = float(input("Enter the Second Number  "))
  maths_ans = mathFunc[oper](num1, num2)
  prev_ans = maths_ans
  print(f"{num1} {oper} {num2} = {maths_ans}")
  anotherTime = input("Do you need to run the Calc on the Answer(y) or fresh Calc(n) or (e) ")
  if(anotherTime == "e"):
    is_another_needed = False
  elif(anotherTime == 'n'):
    new_calc = True
