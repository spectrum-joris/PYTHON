# hoger_lager_data.py

DATASETS = {
    # 10 grootste Belgische gemeenten (populatie, 2025)
    # Bron: Wikipedia "List of most populous municipalities in Belgium" (kolom 2025)
    "be_cities_bevolking": [
        {"name": "Antwerpen (stad)", "bevolking": 562002, "region": "Vlaanderen", "note": "2025"},
        {"name": "Gent",              "bevolking": 272657, "region": "Vlaanderen", "note": "2025"},
        {"name": "Charleroi",         "bevolking": 205763, "region": "Wallonië",   "note": "2025"},
        {"name": "Brussel (stad)",    "bevolking": 198314, "region": "Brussels",   "note": "2025"},
        {"name": "Luik (Liège)",      "bevolking": 197323, "region": "Wallonië",   "note": "2025"},
        {"name": "Schaarbeek",        "bevolking": 129775, "region": "Brussels",   "note": "2025"},
        {"name": "Anderlecht",        "bevolking": 128724, "region": "Brussels",   "note": "2025"},
        {"name": "Brugge",            "bevolking": 120283, "region": "Vlaanderen", "note": "2025"},
        {"name": "Namen (Namur)",     "bevolking": 115029, "region": "Wallonië",   "note": "2025"},
        {"name": "Leuven",            "bevolking": 104906, "region": "Vlaanderen", "note": "2025"},
    ],

    # Belgische voetbalclubs — aantal landstitels (mannen, hoogste klasse)
    "be_football_landstitels": [
        {"club": "RSC Anderlecht",           "landstitels": 34, "city": "Brussel"},
        {"club": "Club Brugge",              "landstitels": 19, "city": "Brugge"},
        {"club": "Union Saint-Gilloise",     "landstitels": 12, "city": "Brussel"},
        {"club": "Standard Liège",           "landstitels": 10, "city": "Luik"},
        {"club": "Beerschot VAC",            "landstitels":  7, "city": "Antwerpen"},
        {"club": "Racing de Bruxelles",      "landstitels":  6, "city": "Brussel"},
        {"club": "Royal Antwerp FC",         "landstitels":  5, "city": "Antwerpen"},
        {"club": "RFC Liège",                "landstitels":  5, "city": "Luik"},
        {"club": "Daring de Bruxelles",      "landstitels":  5, "city": "Brussel"},
        {"club": "KV Mechelen",              "landstitels":  4, "city": "Mechelen"},
    ],

    # Belgische bieren — alcoholpercentage (ABV)
    "be_beers_abv": [
        {"beer": "Chimay Blauw (Grande Réserve)", "alcoholpercentage": 9.0,  "type": "Trappist"},
        {"beer": "Chimay Rood (Première)",        "alcoholpercentage": 7.0,  "type": "Trappist"},
        {"beer": "Chimay Wit (Cinq Cents)",       "alcoholpercentage": 8.0,  "type": "Trappist"},
        {"beer": "Chimay Dorée (Gold)",           "alcoholpercentage": 4.8,  "type": "Trappist"},
        {"beer": "Orval",                          "alcoholpercentage": 6.2,  "type": "Trappist"},
        {"beer": "Rochefort 6",                    "alcoholpercentage": 7.5,  "type": "Trappist"},
        {"beer": "Rochefort 8",                    "alcoholpercentage": 9.2,  "type": "Trappist"},
        {"beer": "Rochefort 10",                   "alcoholpercentage": 11.3, "type": "Trappist"},
        {"beer": "Westmalle Tripel",               "alcoholpercentage": 9.5,  "type": "Trappist"},
        {"beer": "Westmalle Dubbel",               "alcoholpercentage": 7.0,  "type": "Trappist"},
    ],

    # Zelfdoding (WHO, leeftijdsgestandaardiseerd, per 100.000, jaar=2021)
    "zelfmoorden_2021": [
        {"land": "Lesotho",     "zelfmoorden/100K_inwoners": 28.7, "year": 2021},
        {"land": "Zuid-Korea",  "zelfmoorden/100K_inwoners": 27.5, "year": 2021},
        {"land": "Eswatini",    "zelfmoorden/100K_inwoners": 27.2, "year": 2021},
        {"land": "Guyana",      "zelfmoorden/100K_inwoners": 24.8, "year": 2021},
        {"land": "Uruguay",     "zelfmoorden/100K_inwoners": 24.8, "year": 2021},
        {"land": "Litouwen",    "zelfmoorden/100K_inwoners": 22.1, "year": 2021},
        {"land": "Zuid-Afrika", "zelfmoorden/100K_inwoners": 22.3, "year": 2021},
        {"land": "Suriname",    "zelfmoorden/100K_inwoners": 22.3, "year": 2021},
        {"land": "Rusland",     "zelfmoorden/100K_inwoners": 21.4, "year": 2021},
        {"land": "Oekraïne",    "zelfmoorden/100K_inwoners": 21.2, "year": 2021},
    ],

    # Moorden per jaar (2023) — wereldwijd; 'moorden/dag' = moorden/jaar / 365
    # Opmerking: voor niet-VS steden zijn placeholders gezet (None) tot de exacte cijfers bevestigd zijn.
    "city_moorden/jaar": [
        # VS (bestaande gegevens)
        {"stad": "Chicago",       "country": "USA", "continent": "North America", "moorden/jaar": 617, "moorden/dag": round(617/365, 2)},
        {"stad": "Washington, DC","country": "USA", "continent": "North America", "moorden/jaar": 274, "moorden/dag": round(274/365, 2)},
        {"stad": "Detroit",       "country": "USA", "continent": "North America", "moorden/jaar": 252, "moorden/dag": round(252/365, 2)},
        {"stad": "Indianapolis",  "country": "USA", "continent": "North America", "moorden/jaar": 216, "moorden/dag": round(216/365, 2)},
        {"stad": "New Orleans",   "country": "USA", "continent": "North America", "moorden/jaar": 193, "moorden/dag": round(193/365, 2)},
        {"stad": "St. Louis",     "country": "USA", "continent": "North America", "moorden/jaar": 158, "moorden/dag": round(158/365, 2)},
        {"stad": "Atlanta",       "country": "USA", "continent": "North America", "moorden/jaar": 135, "moorden/dag": round(135/365, 2)},
        {"stad": "Oakland",       "country": "USA", "continent": "North America", "moorden/jaar": 126, "moorden/dag": round(126/365, 2)},
        {"stad": "Richmond (VA)", "country": "USA", "continent": "North America", "moorden/jaar":  62, "moorden/dag": round( 62/365, 2)},
        {"stad": "Rochester (NY)","country": "USA", "continent": "North America", "moorden/jaar":  58, "moorden/dag": round( 58/365, 2)},

        # Europa
    {"stad": "Londen",       "country": "Verenigd Koninkrijk", "continent": "Europe",        "moorden/jaar": 110,   "moorden/dag": round(110/365, 2)},  # ≈0.30
    {"stad": "Parijs",       "country": "Frankrijk",            "continent": "Europe",        "moorden/jaar": 111,   "moorden/dag": round(111/365, 2)},  # ≈0.30

    # Zuid-Amerika
    {"stad": "São Paulo",    "country": "Brazilië",            "continent": "South America", "moorden/jaar": 2015,  "moorden/dag": round(2015/365, 2)},  # ≈5.52
    {"stad": "Rio de Janeiro","country": "Brazilië",           "continent": "South America", "moorden/jaar": 4459,  "moorden/dag": round(4459/365, 2)},  # ≈12.22

    # Afrika
    {"stad": "Johannesburg", "country": "Zuid-Afrika",         "continent": "Africa",        "moorden/jaar": 563,   "moorden/dag": round(563/365, 2)},   # ≈1.54
    {"stad": "Kaapstad",     "country": "Zuid-Afrika",         "continent": "Africa",        "moorden/jaar": 1681,  "moorden/dag": round(1681/365, 2)},  # ≈4.60

    # Azië (2022 data gebruikt als placeholder)
    {"stad": "Karachi",      "country": "Pakistan",            "continent": "Asia",          "moorden/jaar": 3356,  "moorden/dag": round(3356/365, 2)},  # ≈9.19
    {"stad": "Manilla",      "country": "Filipijnen",          "continent": "Asia",          "moorden/jaar": 1534,  "moorden/dag": round(1534/365, 2)},  # ≈4.20
    ],

    # Drukste treinstations in België (gem. instappers op weekdagen, 2014)
    "be_drukste_treinstations_2014": [
        {"rank": 1,  "station": "Treinstation Brussel-Zuid",       "province": "Brussels Hoofdstedelijk Gewest", "reizigers/weekdag": 61941, "year": 2014},
        {"rank": 2,  "station": "Treinstation Brussel-Centraal",   "province": "Brussels Hoofdstedelijk Gewest", "reizigers/weekdag": 61234, "year": 2014},
        {"rank": 3,  "station": "Treinstation  Brussel-Noord",      "province": "Brussels Hoofdstedelijk Gewest", "reizigers/weekdag": 58345, "year": 2014},
        {"rank": 4,  "station": "Treinstation  Gent-Sint-Pieters",  "province": "Oost-Vlaanderen",                 "reizigers/weekdag": 54169, "year": 2014},
        {"rank": 5,  "station": "Treinstation Antwerpen-Centraal", "province": "Antwerpen",                       "reizigers/weekdag": 34265, "year": 2014},
        {"rank": 6,  "station": "Treinstation Leuven",             "province": "Vlaams-Brabant",                  "reizigers/weekdag": 32247, "year": 2014},
        {"rank": 7,  "station": "Treinstation Namen",              "province": "Namen",                           "reizigers/weekdag": 18704, "year": 2014},
        {"rank": 8,  "station": "Treinstation Mechelen",           "province": "Antwerpen",                       "reizigers/weekdag": 18593, "year": 2014},
        {"rank": 9,  "station": "Treinstation Brugge",             "province": "West-Vlaanderen",                 "reizigers/weekdag": 18122, "year": 2014},
        {"rank":10,  "station": "Treinstation Ottignies",          "province": "Waals-Brabant",                   "reizigers/weekdag": 17753, "year": 2014},
    ],

    # Belgische attracties/pretparken (bezoekers/jaar, 10 items)
    "be_attractions_bezoekers/jaar": [
        {"attractie": "Pairi Daiza",         "bezoekers/jaar": 2650000, "year": 2024},
        {"attractie": "Plopsaland De Panne", "bezoekers/jaar": 1388732, "year": 2024},
        {"attractie": "ZOO Planckendael",    "bezoekers/jaar":  927000, "year": 2023},
        {"attractie": "ZOO Antwerpen",       "bezoekers/jaar":  857000, "year": 2023},
        {"attractie": "Atomium",             "bezoekers/jaar":  844427, "year": 2024},
        {"attractie": "Mini-Europe",         "bezoekers/jaar":  390000, "year": 2018},
        {"attractie": "Bokrijk (domein)",    "bezoekers/jaar":  977823, "year": 2024},
        {"attractie": "Walibi Belgium",      "bezoekers/jaar": 1450000, "year": 2018},
        {"attractie": "Bellewaerde",         "bezoekers/jaar":  875000, "year": 2023},
        {"attractie": "KMSKA (Antwerpen)",   "bezoekers/jaar":  534000, "year": 2023},
    ],
}
