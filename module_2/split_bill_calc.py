print("Welcome bij de Split Bill Calculator!")
bill = float(input("Wat was de totale rekening?\n€"))
tip = int(input("Welk tip percentage wil je geven?\n%"))
persons = int(input("Hoeveel personen delen de rekening?\n"))
result = round((bill * (1 + tip / 100)) / persons, 2)
print(f"Elke persoon moet {result}€ betalen.")



