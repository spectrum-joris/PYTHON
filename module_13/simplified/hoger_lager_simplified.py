import random
import time
from data import INFLUENCERS
from logo import LOGO

print(LOGO)

answer = ""
score = 0
next = True
inf1 = random.choice(INFLUENCERS)
inf2 = random.choice(INFLUENCERS)

# start met twee verschillende
while inf2 is inf1:
    inf2 = random.choice(INFLUENCERS)

def clear_screen():
    print("\033[2J\033[H", end="")  

def ask(influencer1, influencer2):
    # die while weghalen; stel gewoon de vraag
    answer = input(
        f"{influencer1['name']} heeft {influencer1['followers']} volgers.\n"
        f"Heeft {influencer2['name']} er meer of minder? (schrijf 'meer' of 'minder').\n"
    )
    return answer

# sla het antwoord op
answer = ask(inf1, inf2)

while next == True:
    if answer not in ["meer", "minder"]:
        print(answer)
        # opnieuw vragen, anders blijf je met lege/ongeldige input zitten
        answer = ask(inf1, inf2)

    elif inf2['followers'] > inf1['followers'] and answer == "meer":
        score += 1
        print(f"Correct! {inf2['name']} heeft {inf2['followers']}. Jouw score is {score}")
        time.sleep(3)
        clear_screen()
        # doorschuiven en nieuwe 2e kiezen
        inf1 = inf2
        inf2 = random.choice(INFLUENCERS)
        while inf2 is inf1:  # verschillend houden
            inf2 = random.choice(INFLUENCERS)
        # opnieuw antwoord vragen
        answer = ask(inf1, inf2)

    elif inf2['followers'] < inf1['followers'] and answer == "minder":
        score += 1
        print(f"Correct! {inf2['name']} heeft {inf2['followers']}. Jouw score is {score}")
        time.sleep(3)
        clear_screen()
        # doorschuiven en nieuwe 2e kiezen
        inf1 = inf2
        inf2 = random.choice(INFLUENCERS)
        while inf2 is inf1:
            inf2 = random.choice(INFLUENCERS)
        # opnieuw antwoord vragen
        answer = ask(inf1, inf2)

    elif inf2['followers'] > inf1['followers'] and answer == "minder":
        print(f"Fout. {inf2['name']} heeft {inf2['followers']} volgers. Dat zijn er minder.\nJouw score is {score}")
        exit()

    elif inf2['followers'] < inf1['followers'] and answer == "meer":
        print(f"Fout. {inf2['name']} heeft {inf2['followers']} volgers. Dat zijn er meer.\nJouw score is {score}")
        exit()
