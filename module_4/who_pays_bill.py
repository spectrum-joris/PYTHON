import random

friends = ["An", "Julie", "Mohamed", "Sofia", "Alice"]

wie_betaalt = random.choice(friends)
print(f"{wie_betaalt} betaalt de rekening.")

# of:

wie_betaalt_met_index = random.randint(0, 4)
print(f"{friends[wie_betaalt_met_index]} betaalt de rekening.")

# of:

wie_betaalt_met_dynamische_index = random.randint(0, len(friends) - 1)
print(f"{friends[wie_betaalt_met_dynamische_index]} betaalt de rekening.")


