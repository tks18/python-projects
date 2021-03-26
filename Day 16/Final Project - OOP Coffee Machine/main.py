from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

isRunning = True
while isRunning:
  mainPrompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if(mainPrompt != 'off'):
    if(mainPrompt != 'report'):
      drink = menu.find_drink(mainPrompt)
      if drink == None:
        print("Enter Correct name of the Drink")
      else:
        if (coffee_maker.is_resource_sufficient(drink)):
          moneyRcvd = money_machine.process_coins()
          makePaymt = money_machine.make_payment(moneyRcvd)
          if(makePaymt):
            coffee_maker.make_coffee(drink)
          else:
            isRunning = False
        else:
          isRunning = False
    else:
      coffee_maker.report()
  else: 
    isRunning = False