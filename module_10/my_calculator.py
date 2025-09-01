# rekenmachine
import time

# ----- variabelen declareren en initialiseren -----

logo = r"""
.----------------.
|  REKENMACHINE  |
|----------------|
| 7 | 8 | 9 | /  |
| 4 | 5 | 6 | *  |
| 1 | 2 | 3 | -  |
| 0 | . | = | +  |
'----------------'
"""

def clear_screen(): 
    """2J wist het scherm, en H brengt de cursor naar de eerste positie.
    end="" geeft aan dat we geen nieuwe regel willen."""
    print("\033[2J\033[H", end="")

operators = {
    "optellen": "+", 
    "aftrekken": "-", 
    "vermenigvuldigen": "x", 
    "delen": ":", 
    "machtsverheffing": "**"
}

def calculate(getal1, chosen_operator, getal2):
    if chosen_operator not in operators.values():
        return print(f"Je koos {chosen_operator}. Dat is geen geldige operator.")
    else:
        if chosen_operator == "+":
            return print(f"{getal1} {chosen_operator} {getal2} = {getal1+getal2}")
        elif chosen_operator == "-":
            return print(f"{getal1} {chosen_operator} {getal2} = {getal1-getal2}")
        elif chosen_operator == "x":
            return print(f"{getal1} {chosen_operator} {getal2} = {getal1*getal2}")
        elif chosen_operator == ":":
            return print(f"{getal1} {chosen_operator} {getal2} = {getal1/getal2}")
        elif chosen_operator == "**":
            return print(f"{getal1} {chosen_operator} {getal2} = {getal1**getal2}")

# ----- beginscherm -----
print(logo)
print()

timer = 1
should_continue = True
yes_or_no_options = ["y", "n"]

time.sleep(timer)

clear_screen()

# ----- start -----
while should_continue == True:
    getal1 = float(input("getal 1: \n").strip().replace(",", "."))
    clear_screen()

    print("kies een operator.")
    for key in operators:
        print(f"{key}: {operators[key]}")
    chosen_operator = input("operator: \n").strip()
    clear_screen()

    getal2 = float(input("getal 2: \n").strip().replace(",", "."))
    clear_screen()

    calculate(getal1, chosen_operator, getal2)
    yes_or_no = input("wil je verdergaan? (y/n) \n")

    if yes_or_no not in yes_or_no_options:
        yes_or_no
    else:
        if yes_or_no == "y":
            should_continue = True
            clear_screen()
        else:
            should_continue = False
            print("Ok. Tot later!")
            time.sleep(timer)
            clear_screen()




