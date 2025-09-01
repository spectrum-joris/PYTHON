from auction_logo import logo, proficiat
import time

WIDTH = 60 # we doen alsof het scherm 60 karakters breed is, zodat we mooi kunnen centreren

def clear_screen():
    # print("\n" * 100)  # we printen 100 lege regels om het scherm te 'wissen'
    print("\033[2J\033[H", end="")
    # 2J wist scherm, en H zet cursor terug naar begin van het scherm (home). Met end="" zorgen we ervoor dat de cursor niet naar een nieuwe regel gaat

# ------- Startscherm -------
clear_screen()
print(logo)

logo_time = 3
bid_time = 1

print(f"De veiling start over {logo_time} seconden...")
time.sleep(logo_time)

bids = {} # buiten de loop, anders wordt deze telkens opnieuw geinitialiseerd, en overschrijven we de vorige biedingen

# ----- afsluiten van de veiling -----
def close_auction(bidding_dictionary):
    # ----- einde veiling -----
    time.sleep(bid_time)
    clear_screen()
    print("De veiling is gesloten!")
    print("-" * 30)
    print()
    # ----- hoogste bod bepalen -----
    time.sleep(bid_time)
    clear_screen()

    highest_bid = -1.0 # start onder het laagste mogelijke bod
    highest_bidder = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder

    print(proficiat)
    print()
    print(f"{highest_bidder} won deze veiling met een bod van {highest_bid:,.2f}€\n") # we tonen het hoogste bod met 2 decimalen ("fixed point", 2 cijfers na de komma) en duizendtallen met scheidingsteken (de komma)


next_bid = "ja"
while next_bid == "ja":
    clear_screen()
    print("Welkom bij de stille veiling!")
    print("-" * 30)
    print() # een lege regel voor wat ruimte

    time.sleep(bid_time)

    clear_screen()

    print("Wat is je naam?")
    name = input(">> ")
    print(f"Wat is je bod, {name}? ")
    raw_amount = input(">> ")
    raw_amount = raw_amount.strip().replace(",", ".")  # Verwijder eventuele spaties aan het begin en einde en vervang komma's door punten
    try: # zorgt ervoor dat we een foutmelding krijgen als de invoer geen geldig getal is zonder te crashen
        bid = float(raw_amount)
    except ValueError: # als de invoer geen geldig getal is, dan vangen we de fout op
        print("Ongeldig getal. Probeer opnieuw.")
        time.sleep(bid_time)
        continue # gaat terug naar het begin van de while loop ; 'break' zou de loop stoppen, maar we willen dat de gebruiker opnieuw kan bieden

    # bids aanpassen
    bids[name] = bid
    print("Je bod werd geregistreerd.")
    print("Wil nog iemand bieden? (ja/nee)")
    next_bid = input(">> ").strip().lower()
    while next_bid not in ["ja", "nee"]:
        print("Ongeldige invoer. Typ 'ja' of 'nee'.")
        next_bid = input(">> ").strip().lower()

    if next_bid == "nee":
        close_auction(bids)
        break


