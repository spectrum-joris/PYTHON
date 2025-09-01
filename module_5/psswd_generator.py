import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "<", ">", "?", "/", "~"]

aantal_letters = int(input("Hoeveel letters wil je in je wachtwoord? \n"))
aantal_numbers = int(input("Hoeveel cijfers wil je in je wachtwoord? \n"))
aantal_symbols = int(input("Hoeveel symbolen wil je in je wachtwoord? \n"))

wachtwoord = []

for letter in range(1, aantal_letters + 1):
    wachtwoord.append(random.choice(letters))
for cijfer in range(1, aantal_numbers + 1):
    wachtwoord.append(random.choice(numbers))
for symbool in range(1, aantal_symbols + 1):
    wachtwoord.append(random.choice(symbols))

random.shuffle(wachtwoord)

print(f"Je wachtwoord is: {''.join(wachtwoord)}")




