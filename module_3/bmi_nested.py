
print("Welkom bij de BMI Calculator!")
height = float(input("Wat is jouw lengte in meter? (bv. 1.75)\n"))
weight = float(input("Wat is jouw gewicht in kilogram?\n"))
bmi = weight / (height ** 2)  # BMI formule
print(f"Jouw BMI is: {round(bmi, 1)}")  # Output: Jouw BMI is: 25.7

if bmi < 18.5:
    print("Je hebt ondergewicht.")
elif bmi < 25:
    print("Je hebt een gezond gewicht.")
else:
    print("Je hebt overgewicht.")






    