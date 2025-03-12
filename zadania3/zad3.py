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

dach('*')
piętro('#')
piętro('@')