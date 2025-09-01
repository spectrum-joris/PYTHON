import random

# Rock
steen = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
blad = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
schaar = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

opties = [blad, steen, schaar]

computer_keuze = random.randint(0, 2)
jouw_keuze = int(input("Maak jouw keuze. 0 voor blad, 1 voor steen, 2 voor schaar: \n"))

if jouw_keuze < 0 or jouw_keuze > 2:
    print("Ongeldige keuze. Kies een getal tussen 0 en 2.")
else :
    print(f"De computer heeft gekozen:\n{opties[computer_keuze]}")
    print(f"Jij hebt gekozen:\n{opties[jouw_keuze]}")

    if computer_keuze == jouw_keuze:
        print("Gelijkspel!")
    elif (computer_keuze == 1 and jouw_keuze == 2) or \
        (computer_keuze == 2 and jouw_keuze == 0) or \
        (computer_keuze == 0 and jouw_keuze == 1):
        print("De computer wint!")
    else:
        print("Jij wint!")




