try:
    age = int(input("geef je leeftijd in: "))
except ValueError:
    print("Dit is geen geldige input. Geef een cijfer in: ")
    age = int(input("geef je leeftijd in: "))

if age > 18:
    print("je mag met de wagen rijden.")
else:
    print("je mag niet met de wagen rijden.")




