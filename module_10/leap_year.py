year = int(input("Geef een jaar in: \n"))
is_leap = False

def check_leap(year):
    """deze functie krijgt een jaar als input en verifieert of dit jaar al dan niet een schrikkeljaar is.
    Opmerking: docstrings moeten net na de functie declarate komen te staan om correct te werken.
    Zoals je ziet kan je meerdere lijnen schrijven."""
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

is_leap = check_leap(year)

if is_leap == True:
    print(f"{year} is een schrikkeljaar")
else:
    print(f"{year} is geen schrikkeljaar")





