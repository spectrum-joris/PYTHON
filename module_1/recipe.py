print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

steps = [
    "Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.",
    "Knead the dough for 10 minutes.",
    "Add 3g of Salt.",
    "Leave to rise for 2 hours.",
    "Bake at 200 degrees C for 30 minutes."
]

for i, step in enumerate(steps, start=1):
    print(f"{i}. {step}")


