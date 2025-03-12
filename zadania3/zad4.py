def piętro(znak):
    print(f"  ______  ")
    print(f" |      | ")
    print(f" |  {znak*2}  | ")
    print(f" |______| ")

def dach(znak):
    print(f"     ^     ")
    print(f"    /{znak*2}\\    ")
    print(f"   /{znak*4}\\   ")
    print(f"  /{znak*6}\\  ")
    print(f" /{znak*8}\\ ")

def rysuj_dom(liczba_pięter, znak_dach, znak_piętro):
    dach(znak_dach)
    for _ in range(liczba_pięter):
        piętro(znak_piętro)


rysuj_dom(3, '*', '#')