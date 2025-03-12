import random

def kamien_papier_nozyce():
    wybory = ["kamień", "papier", "nożyce"]
    komputer = random.choice(wybory)
    gracz = input("Wybierz kamień, papier lub nożyce: ").lower()
    print(f"Komputer wybrał: {komputer}")
    if gracz == komputer:
        print("Remis!")
    elif (gracz == "kamień" and komputer == "nożyce") or \
         (gracz == "papier" and komputer == "kamień") or \
         (gracz == "nożyce" and komputer == "papier"):
        print("Wygrałeś!")
    else:
        print("Przegrałeś!")

kamien_papier_nozyce()