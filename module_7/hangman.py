import random
from stadia import HANGMAN_STAGES
from words import word_list
from results import results
from hangman_art import hangman_logo


chosen_word = random.choice(word_list)
# print(f"Chosen word: {chosen_word}")
print(hangman_logo)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder +"\n")

game_over = False
correct_letters = [] # lijst van letters die correct zijn geraden ; deze moet buiten de while loop staan, anders wordt deze telkens opnieuw geinitialiseerd
lives = 6
stadium = 0 # indien je stadia omgekeerd geordend staan, heb je deze variabele en kan je lives gebruiken om de index van de HANGMAN_STAGES te bepalen

def print_star_lives(lives):
    if lives > 1:
        msg = f"* {lives} LEVENS OVER *"
        line = "*"*(len(msg)+4)
        print(line)
        print(f"* {msg} *")
        print(line, "\n")
    elif lives == 1:
        msg = "* 1 LEVEN OVER *"
        line = "*"*(len(msg)+4)
        print(line)
        print(f"* {msg} *")
        print(line, "\n")
    else:
        print("")

while not game_over:

    guess = input("Raad een letter: ").lower()

    display = ""

    if guess in correct_letters:
        print(f"Je koos {guess}. Deze had je al geraden. Probeer een andere letter.\n")
        continue

    for letter in chosen_word:
        # als je de letter al correct hebt geraden, dan moet deze ook in de display komen
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        # als de letter al in onze lijst van correct_letters zit, dan moet deze ook in de display komen
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display +"\n")

    if guess not in chosen_word:
        lives -= 1
        print_star_lives(lives)
        stadium += 1
        print(f"Je gaf {guess} in. Deze letter zit niet in het woord.\n")
        print(HANGMAN_STAGES[stadium] +"\n")
    elif not guess:
        print("Je gaf geen letter in. Probeer opnieuw.\n")
    else:
        print("Goed geraden! \n")

    if "_" not in display and lives > 0:
        print(f"Het woord was: {chosen_word}\n")
        print(results[0])
        game_over = True
    elif lives == 0:
        print(f"Het woord was: {chosen_word}\n")
        print(print(results[1]))
        game_over = True





