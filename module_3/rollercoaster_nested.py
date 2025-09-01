print("Welcome op onze rollercoaster!\nEerst even nagaan of je voldoet aan de vereisten.")
height = float(input("Wat is je lengte in meters? (bijv. 1.75)\n"))

length_requirement = 1.40  # minimum vereiste lengte 
age_requirement = 12  # minimum vereiste leeftijd

minimum_price = 5.00  # minimum prijs voor kinderen onder de 12 jaar
medium_price = 10.00  # prijs voor volwassenen
maximum_price = 15.00  # maximum prijs voor VIP toegang

if height >= length_requirement:
    print("Je bent groot genoeg voor de rollercoaster\n")
    age = int(input("Hoe oud ben je?\n"))
    if age >= age_requirement:
        print("Je voldoet aan alle eisen. Veel plezier in de rollercoaster!")
        if age < 15:
            print(f"betaal {round(minimum_price)}€") 
        elif age < 18:
            print(f"betaal {round(medium_price)}€")
        else:
            print(f"betaal {round(maximum_price)}€")
        print("Geniet van de rit!")
    else:
        print("Sorry, je bent jammer genoeg te jong. Je mag de rollercoaster niet in.")
else:
    print("Sorry, je bent jammer genoeg te klein. Je mag de rollercoaster niet in.")




