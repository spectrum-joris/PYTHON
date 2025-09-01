alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(direction, text, shift):
        encrypted_text = ""
        for letter in text:
            if letter not in alphabet:
                encrypted_text += letter
            else:
                letter_index = alphabet.index(letter)
            if direction == "decode":
                letter_index -= int(shift)
            else:
                letter_index += int(shift)
            shifted_index = letter_index % len(alphabet)
            encrypted_text += alphabet[shifted_index]
        print(f"\nde {direction}d tekst is:\n{encrypted_text}\n")

should_continue = True

while should_continue is True:
    direction = input("Wat wil je doen? Typ 'encode' of 'decode': \n").lower()
    if direction not in ["encode", "decode"]:
        print("Ongeldige keuze. Typ 'encode' of 'decode'.")
        exit()
    text = input("Typ je boodschap: \n").lower()
    shift = int(input("Met hoeveel posities wil je verschuiven? \n"))

    caesar(direction, text, shift)

    should_continue = True

    restart = input("Wil je verder gaan? Typ 'ja'. Anders 'nee': \n").lower()
    if restart == "ja":
        should_continue = True
    elif restart == "nee":
        print("Bedankt voor het spelen!")
        should_continue = False
    else:
        print("Ongeldige keuze. Typ 'ja' of 'nee'.")
        exit()




