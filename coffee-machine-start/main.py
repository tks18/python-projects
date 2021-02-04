from menu import MENU, resources

def printResources():
  print("Current Level of Resources Available: ")
  for obj in resources:
    print(obj.capitalize() + ": " + str(resources[obj]))

def checkAvblRes(selDict):
  checDict = {
    "water": True,
    "coffee": True,
    "milk": True
  }
  for resource in selDict["ingredients"]:
    requiredRes = selDict["ingredients"][resource]
    avblRes = resources[resource];
    if(avblRes > requiredRes):
      checDict[resource] = True;
    else:
      checDict[resource] = False;
  if(checDict["water"] and checDict["coffee"] and checDict["milk"]):
    return True
  elif not checDict["water"]:
    return "Water is Not Available"
  elif not checDict["coffee"]:
    return "Coffee is Not Available"
  elif not checDict["milk"]:
    return "Milk is Not Available"

def askMoneyFromUser():
  quarters = float(input("How Many Quarters ?: "))
  dimes = float(input("How Many Dimes ?: "))
  nickles = float(input("How Many Nickles ?: "))
  pennies = float(input("How Many Pennies ?: "))
  return {
    "quarters": quarters,
    "dimes": dimes,
    "nickles": nickles,
    "pennies": pennies
  }


def returnMoneyValue(quarters, dimes, nickles, pennies, selDict):
  quarterMon = quarters * 0.25
  dimesMon = dimes * 0.10
  nicklesMon = nickles * 0.05
  penniesMon = pennies * 0.01
  totalMoneyVal = quarterMon + dimesMon + nicklesMon + penniesMon
  requiredVal = selDict["cost"]
  if (totalMoneyVal < requiredVal):
    return {
      "val": False,
      "money": totalMoneyVal
    }
  else:
    return {
      "val": True,
      "money": totalMoneyVal
    }

def checkRefund(monVal, selDict):
  reqValue = selDict["cost"]
  refund = monVal - reqValue
  if(refund < 0):
    refund = 0
  return round(refund, 2)

def updateRes(selDict):
  ingredients = selDict["ingredients"]
  for res in  ingredients:
    resources[res] = resources[res] - ingredients[res]
  resources["money"] = resources["money"] + selDict["cost"]

isRunning = True
while isRunning:
  mainPrompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if(mainPrompt != 'off'):
    if(mainPrompt != 'report'):
      if(mainPrompt != 'espresso' and mainPrompt != 'latte' and mainPrompt != 'cappuccino'):
        print("Enter Correct name of the Drink")
      else:
        selCoff = MENU[mainPrompt];
        resAvbl = checkAvblRes(selCoff)
        if(resAvbl == True):
          getMoneyInfo = askMoneyFromUser();
          isEnoughMoney = returnMoneyValue(getMoneyInfo["quarters"], getMoneyInfo["dimes"], getMoneyInfo["nickles"], getMoneyInfo["pennies"], selCoff)
          if(isEnoughMoney["val"]):
            refundAmt = checkRefund(isEnoughMoney["money"], selCoff)
            if(refundAmt != 0): 
              print(f"Here is {refundAmt} in Change")
            updateRes(selCoff)
            print(f"Here is Your {mainPrompt.capitalize()}")
          else:
            print(f"Your Money is Not Enough for the Coffee Selected. Your Money of {isEnoughMoney['money']} got Refunded.")
        else:
          print(resAvbl)
    else:
      printResources();
  else:
    isRunning = False