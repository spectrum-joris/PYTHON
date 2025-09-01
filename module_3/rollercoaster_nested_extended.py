print("Welcome op onze rollercoaster!\nEerst even nagaan of je voldoet aan de vereisten.")
height = float(input("Wat is je lengte in meters? (bijv. 1.75)\n"))

length_requirement = 1.40  # minimum vereiste lengte 
age_requirement = 12  # minimum vereiste leeftijd

minimum_price = 5.00  # minimum prijs voor kinderen onder de 12 jaar
medium_price = 10.00  # prijs voor volwassenen
maximum_price = 15.00  # maximum prijs voor VIP toegang

bill = 0

if height >= length_requirement:
    print("Je bent groot genoeg voor de rollercoaster\n")
    age = int(input("Hoe oud ben je?\n"))
    if age >= age_requirement:
        print("Je voldoet aan alle eisen. Veel plezier in de rollercoaster!")
        if age < 15:
            print(f"kinderprijs is {round(minimum_price)}€") 
            bill = minimum_price
        elif age < 18:
            print(f"jeugdprijs is {round(medium_price)}€")
            bill = medium_price
        else:
            print(f"volwassenen prijs is {round(maximum_price)}€")
            bill = maximum_price
        wants_photo = input("wil je een foto? (j/n)\n")
        if wants_photo.lower() == "j":
            print("Je hebt gekozen voor een foto. De kosten hiervoor zijn 5€ extra.")
            total_price = round(bill + 5)
            print(f"Je totale prijs is {round(total_price)}€")
        else:
            print(f"Je hebt geen foto gekozen. Je totale prijs is {round(bill)}€")
    else:
        print("Sorry, je bent jammer genoeg te jong. Je mag de rollercoaster niet in.")
else:
    print("Sorry, je bent jammer genoeg te klein. Je mag de rollercoaster niet in.")




