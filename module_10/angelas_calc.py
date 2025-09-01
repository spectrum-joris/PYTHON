# rekenmachine
import time

# ----- start -----
def calculator():
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
    
    should_continue = True
    yes_or_no_options = ["y", "n"]
    timer = 1

    # ----- mogelijke berekeningen -----
    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    def multiply(n1, n2):
        return n1 * n2
    def divide(n1, n2):
        return n1 / n2
    def power(n1, n2):
        return n1 ** n2

    # ----- dictionary -----
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "**": power
    }

    # ----- beginscherm -----
    print(logo)
    print()

    time.sleep(timer)

    clear_screen()

    getal1 = float(input("getal 1: \n").strip().replace(",", "."))
    clear_screen()

    while should_continue == True:
        print("kies een operator:")
        for key in operations:
            print(f"{key}")
        print()
        chosen_operator = input("")
        clear_screen()

        if chosen_operator not in operations:
            print(f"Je koos {chosen_operator}. Dat is geen geldige operator.")
        else:
            getal2 = float(input("getal 2: \n").strip().replace(",", "."))
            clear_screen()

            result = operations[chosen_operator](getal1, getal2)
            print(f"{getal1} {chosen_operator} {getal2} = {result}")
            yes_or_no = input("wil je verdergaan met de berekening? (y/n) \n")

            if yes_or_no not in yes_or_no_options:
                should_continue = False
                print("Ongeldige keuze. We sluiten hier af.")
                time.sleep(timer)
                clear_screen()
            else:
                if yes_or_no == "y":
                    should_continue = True
                    clear_screen()
                    getal1 = result
                    print(f"We gaan verder met ons eerder resultaat {getal1} als getal 1.")
                else:
                    should_continue = False
                    print("Ok. Laat ons een nieuwe berekening starten.")
                    time.sleep(timer)
                    clear_screen()
                    calculator()

calculator()





