# subscripting: een element halen uit een string
print("hello"[0])  # Output: h
print("hello"[1])  # Output: e
print("hello"[-1])  # Output: 0
print("hello"[-2])  # Output: l

# string concatenation: twee strings samenvoegen
print("123" + " " + "456")  # Output: 123 456

# data types printen: string, int, float, boolean
print(type("Dit is een string"))  # Output: string
print(type(123))  # Output: int
print(type(3.14))  # Output: float
print(type(True))  # Output: boolean

# data type conversie: van string naar int
print(int("123"))  # Output: 123
print(int("456"))  # Output: 456

print(int("123") + int("456"))  # Output: 579

# los deze error op:
# print("het aantal letters in jouw naam is: " + len(input("Wat is jouw naam? ")))

# de oplossing is:
print("Het aantal letters in jouw naam is: " + str(len(input("Wat is jouw naam? "))))

# PEMDAS: volgorde van bewerkingen
print(3 * 3 + 3 / 3 - 3)  

# maak deze berekening opnieuw zodat de uitkomst 3 is:
print(3 * (3 + 3) / 3 - 3)  # Output: 3.0

# bereken BMI met deze waarden:
height = 1.87  
weight = 90  

bmi = weight / (height ** 2)  # BMI formule

print("bmi is: " + str(bmi))  # Output: bmi is: 25.7

# afronden
int(bmi) # Converteer BMI naar een integer. Hier wordt het getal "gefloored" naar beneden, dus 25.7 wordt 25.
round(bmi)  # Rond de BMI af naar het dichtstbijzijnde gehele getal, dus 25.7 wordt 26.
round(bmi, 1)  # Rond de BMI af naar 1 decimaal, dus 25.7 blijft 25.7.

# assignment operators
score = 0  # Initialiseer de score
score += 1  # Verhoog de score met 1
score -= 1  # Verlaag de score met 1
score *= 2  # Vermenigvuldig de score met 2
score /= 2  # Deel de score door 2
score **= 2  # Verhoog de score tot de macht van 2

# f-strings: een manier om strings te formatteren
name = "John"
age = 30
score = 100
height = 1.75
is_winning = True

print(f"Mijn naam is {name}, ik ben {age} jaar oud, mijn score is {score}, mijn lengte is {height} meter en je bent aan het winnen: {is_winning}.")  # Output: Mijn naam is John, ik ben 30 jaar oud, mijn score is 100, mijn lengte is 1.75 meter en je bent aan het winnen: True.



