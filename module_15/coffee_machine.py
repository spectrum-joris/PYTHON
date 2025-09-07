import sys
import time

products = {
    "espresso": {
        "price": 1.50,
        "ingredients": {
            "water": 50,
            "coffee": 18
        }
    },
    "latte": {
        "price": 2.50,
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        }
    },
    "cappuccino": {
        "price": 3.00,
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        }
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 24
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

timer = 1
numbers = [1, 2, 3]

def clear_screen():
    print("\033[2J\033[H", end="")

def shutoff():
    for number in reversed(numbers):  # 3, 2, 1
        sys.stdout.write(f"\rshutting off... {number}")
        sys.stdout.flush()            # () AANROEPEN!
        time.sleep(timer)
    print()  # nieuwe lijn
    clear_screen()
    print("\ngoodbye...")
    time.sleep(timer)
    clear_screen()
    sys.exit()

def generate_report(res):
    # Gewoon printen; geen globale 'report' check
    print(
        f"water: {res['water']}\n"
        f"milk: {res['milk']}\n"
        f"coffee: {res['coffee']}"
    )

def ask_coins(coffee_choice):
    print("Please insert coins\n")
    # Aantallen munten zijn integers
    num_quarters = int(input("How many quarters: "))
    num_dimes    = int(input("How many dimes: "))
    num_nickles  = int(input("How many nickles: "))
    num_pennies  = int(input("How many pennies: "))

    # GEEN sum(); gewoon optellen
    credits = (
        coins["quarter"] * num_quarters +
        coins["dime"]    * num_dimes +
        coins["nickel"]  * num_nickles +
        coins["penny"]   * num_pennies
    )
    check_credits(coffee_choice, credits)

def make_coffee(coffee):
    print(f"Here's your {coffee}. Enjoy!")
    time.sleep(timer)

def return_change(money):
    print(f"And here's your change: {money:.2f}€")
    print("Thank you.")
    time.sleep(timer)
    shutoff()

def check_credits(product, credits):
    price_map = {
        "cappuccino": products["cappuccino"]["price"],
        "espresso":   products["espresso"]["price"],
        "latte":      products["latte"]["price"],
    }
    price = price_map[product]

    if credits >= price:
        make_coffee(product)
        change = credits - price
        return_change(change)
    else:
        print("You don't have sufficient funds. Please take back your money.")
        time.sleep(timer)
        sys.exit()

def process_order(c):
    c = c.lower()
    if c in ["cappuccino", "espresso", "latte"]:
        ask_coins(c)
    elif c == "report":
        generate_report(resources)
    elif c == "off":
        shutoff()
    else:
        print("Invalid choice. Try again later.")
        time.sleep(timer)
        sys.exit()

# ---- start ----
choice = input("Which coffee would you like?\nEspresso, Latte or Cappuccino\n")
process_order(choice)
