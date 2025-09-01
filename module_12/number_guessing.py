import random
import time
import sys
from art import logo #patorjk.com

print(logo)

print("Welkom bij Het Raad Het Getal Spel")
print("Ik denk aan een getal tussen 0 en 100")
level = input("Kies een moeilijkheidsgraad (hard / easy)").strip().lower()

while level not in ["hard", "easy"]:
    level = input("Typ 'hard' of 'easy'").strip().lower()

random_number = round(random.random()*100) # of randint(0, 100) wat 100 ook bevat
print(random_number)

def guess_number(rnum, lev):
    if lev == "hard":
        attempts = 5
    else:
        attempts = 10
    print(f"Je hebt {attempts} pogingen om het getal te raden.")
    guess = -1
    is_over = False
    while guess != rnum and is_over == False:
        for attempt in range(0, attempts):
            guess = round(float(input("Raad het getal: ").strip()))
            if guess == rnum:
                print(f"{guess} is juist! Proficiat!")
                is_over = True
            if guess < rnum:
                print(f"{guess} is te laag.\nProbeer opnieuw")
                attempts -= 1
            elif guess > rnum:
                print(f"{guess} is te hoog.\nProbeer opnieuw")
                attempts -= 1

            if attempts > 0 and guess != rnum:
                print(f"Je hebt nog {attempts} poging(en) over om het getal te raden.")
            else:
                print("Game Over.")
                is_over = True

            if is_over == True:
                time.sleep(3)
                sys.exit()

guess_number(random_number, level)    


