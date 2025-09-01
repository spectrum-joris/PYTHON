import random
import sys
import time
from hoger_lager_data import DATASETS

def pick_two_distinct(pool):
    i = random.randrange(len(pool))
    j = random.randrange(len(pool))
    while j == i:
        j = random.randrange(len(pool))
    return pool[i], pool[j]

def pick_pool():
    key = random.choice(list(DATASETS.keys()))
    return key, DATASETS[key]

# 1) kies dataset + 2 items
dataset_name, pool = pick_pool()
first, second = pick_two_distinct(pool)
while first == second:
    second = random.choice(pool)

score = 0
game_is_over = False

# 2) hulpfunctie om de juiste label/metric te bepalen
def detect_keys(item):
    try:
        if "bevolking" in item:        
            return "name", "bevolking"
        if "beer" in item:           
            return "beer", "alcoholpercentage"
        if "landstitels" in item:            
            return "club", "landstitels"
        if "zelfmoorden/100K_inwoners" in item: 
            return "land", "zelfmoorden/100K_inwoners"
        if "moorden/jaar" in item:
            return "stad", "moorden/jaar"
        if "attractie" in item:          
            return "attractie", "bezoekers/jaar"
        if "station" in item: 
            return "station", "reizigers/weekdag"
    except ValueError:
        print("Onbekende dataset-structuur")

label_key, metric_key = detect_keys(first)

# 3) spel-loop
while game_is_over == False:
    # laat A zien
    print(f"{first[label_key]}: {metric_key} = {first[metric_key]}")
    # vraag naar B
    reply = input(f"Is {second[label_key]} hoger of lager? (hoger/lager) ").strip().lower()
    if reply not in ("hoger", "lager"):
        print("Typ 'hoger' of 'lager'.")
        continue

    a = first[metric_key]
    b = second[metric_key]
    # als b None is (bij onvolledige data), kies een andere tweede
    if b is None or a is None:
        second = random.choice(pool)
        while second == first:
            second = random.choice(pool)
        continue

    correct = (reply == "hoger" and b > a) or (reply == "lager" and b < a)

    if correct:
        score += 1
        print(f"✅ Correct! {second[label_key]} = {b}. Score: {score}\n")
        # schuif door: B wordt nieuwe A, kies nieuwe B
        first = second
        second = random.choice(pool)
        while second == first:
            second = random.choice(pool)
    else:
        print(f"❌ Fout. {second[label_key]} = {b}. Eindscore: {score}")
        game_is_over = True  # <-- ECHT toewijzen
        time.sleep(1)




