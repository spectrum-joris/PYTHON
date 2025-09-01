print(r""" 
/====================<3====================\
|              LOVE CALCULATOR             |
\====================<3====================/
""")

print("\n") 

name1 = input("Geef je naam: ")
name2 = input("Geef de naam van je vriend(in): ")

def calculate_love_score(name1, name2):

    names = (name1 + name2).lower()

    true_count = 0
    love_count = 0

    love_score = 0

    print("\n")

    for letter in "true":
        count = names.count(letter)
        if count > 0:
            true_count += count
        print(f"{letter.capitalize()} komt {count} voor")
        
    print("\n")

    for letter in "love":
        count = names.count(letter)
        if count > 0:
            love_count += count
        print(f"{letter.capitalize()} komt {count} voor")   
        
    love_score = true_count + love_count

    print("\n")
    print(f"De love score is: {love_score}")
    print("\n")

calculate_love_score(name1, name2)



