getallen = [1, 2, 3, 4, 5]

print(f"Het hoogste getal is: {max(getallen)}")

#of:

max_getal = 0
for getal in getallen:
    if getal > max_getal:
        max_getal = getal
print(f"De manuele berekening is: {max_getal}")


