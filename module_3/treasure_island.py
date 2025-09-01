print('''
           mm###########mmm
        m####################m
      m#####`"#m m###"""'######m
     ######*"  "   "   "mm#######
   m####"  ,             m"#######m
  m#### m*" ,'  ;     ,   "########m
  ####### m*   m  |#m  ;  m ########
 |######### mm#  |####  #m##########|
  ###########|  |######m############
  "##########|  |##################"
   "#########  |## /##############"
     ########|  # |/ m###########
      "#######      ###########"
        """"""       """""""""
''')

print("Welcome op Treasure Island!")
print("Jouw missie is om de schat te vinden.")

keuze1 = input("Ga naar links of rechts? (type 'links' of 'rechts')\n").lower()
if keuze1 == "links":
    keuze2 = input("Je komt bij een rivier. Wil je zwemmen of een boot nemen? (type 'zwemmen' of 'boot')\n").lower()
    if keuze2 == "boot":
        keuze3 = input("Je komt aan bij een eiland met drie deuren: rood, blauw en geel. Welke deur kies je? (type 'rood', 'blauw' of 'geel')\n").lower()
        if keuze3 == "geel":
            print("Gefeliciteerd! Je hebt de schat gevonden! 🎉")
        elif keuze3 == "rood":
            print("Oh nee! Je bent verbrand door vuur! Game over.")
        elif keuze3 == "blauw":
            print("Je bent opgegeten door wilde beesten! Game over.")
        else:
            print("Dat is geen geldige keuze. Game over.")
    else:
        print("Je bent verdronken in de rivier! Game over.")
else:
    print("Je bent aangevallen door een tijger! Game over.")
print("Bedankt voor het spelen van Treasure Island!")






