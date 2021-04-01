MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 400, #300
    "milk": 250, #200
    "coffee": 200, #100
    "money": 0,
}

quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

def resource_report():
  print(f"Water: {resources['water']}")
  print(f"Milk: {resources['milk']}")
  print(f"Coffee: {resources['coffee']}")
  print(f"Money: ${resources['money']}")

def resources_needed(drink_ingredients):
  enough_ingredients = True
  if "water" in drink_ingredients:
    if drink_ingredients["water"] <= resources["water"]:
      enough_ingredients = True
    else:
      enough_ingredients = False
      return enough_ingredients
  if "coffee" in drink_ingredients:
    if drink_ingredients["coffee"] <= resources["coffee"]:
      enough_ingredients = True
    else:
      enough_ingredients = False
      return enough_ingredients
  if "milk" in drink_ingredients:
    if drink_ingredients["milk"] <= resources["milk"]:
      enough_ingredients = True
    else:
      enough_ingredients = False
      return enough_ingredients
  return enough_ingredients

def coins_and_change(drink):
  print("Please insert coins.")
  quarters_paid = int(input("How many quarters? "))
  dimes_paid = int(input("How many dimes? "))
  nickles_paid = int(input("How many nickles? "))
  pennies_paid = int(input("How many pennies? "))
  total_paid = (quarters_paid * quarter) + (dimes_paid * dime) +(nickles_paid * nickle) + (pennies_paid * penny)
  if total_paid >= MENU[drink]['cost']:
    ### Need to calculate change and return the change ####
    change = round(total_paid - MENU[drink]['cost'], 2)
    resources['money'] += MENU[drink]['cost'] 
    return change
  else:
    return False
    #return f"Here is ${change} in change."
  # else:
  #   return "Sorry, that is not enough. Money refunded."

def deduct_resources(items):
  if "water" in ingredients:
    resources["water"] -= ingredients["water"]
  if "milk" in ingredients:
    resources["milk"] -= ingredients["milk"]
  if "coffee" in ingredients:
    resources["coffee"] -= ingredients["coffee"]


machine_on = True

while machine_on:
  customer_choice = input("   What would you like? (latte, espresso, cappuccino) ")
  if customer_choice == "report":
    resource_report()
  elif customer_choice == "off":
    exit()
  elif customer_choice == "latte" or customer_choice == "espresso" or customer_choice == "cappuccino":
    ingredients = MENU[customer_choice]['ingredients']
    ingredients_check = resources_needed(ingredients)
    if ingredients_check == True:
      change = coins_and_change(customer_choice)
      if change:
        print(f"Here is your ${change} in change.")
        print(f"Here is your {customer_choice}. Enjoy!")
        deduct_resources(ingredients)
      elif change == False:
        print("Sorry, that is not enough. Refund money.")
    else:
      print("Sorry, there are not enough resources.")
