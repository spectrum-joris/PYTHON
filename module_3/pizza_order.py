print("Welkom bij de Pizza Bestel App!")

size = input("Welke maat pizza wil je? (small, medium, large)\n").lower()

if size not in ["small", "medium", "large"]:
    print("Ongeldige maat. Kies uit small, medium of large.")
else:  
    bill = 0
    if size == "small":
        bill += 15
    elif size == "medium":
        bill += 20
    elif size == "large":
        bill += 25

    pepperoni = input("Wil je pepperoni? (ja/nee)\n").lower()
    if pepperoni not in ["ja", "nee"]:
        print("Ongeldige keuze. Kies 'ja' of 'nee'.")
    else:
        if pepperoni == "ja":
            bill += 2

        extra_cheese = input("Wil je extra kaas? (ja/nee)\n").lower()

        if extra_cheese not in ["ja", "nee"]:
            print("Ongeldige keuze. Kies 'ja' of 'nee'.")
        else:
            if extra_cheese == "ja":
                bill += 1

            print(f"De totale prijs voor jouw pizza is: {bill}€")
            print("Bedankt voor je bestelling!")





