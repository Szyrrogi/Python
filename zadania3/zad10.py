import math

def odleglosc(P1, P2):
    return math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)
def czy_wspolliniowe(P1, P2, P3):
    return (P2[1] - P1[1]) * (P3[0] - P2[0]) == (P3[1] - P2[1]) * (P2[0] - P1[0])
def obwodTrojkata(P1, P2, P3):
    if czy_wspolliniowe(P1, P2, P3):
        print("Punkty są współliniowe, nie można utworzyć trójkąta.")
        return 0
    else:
        return odleglosc(P1, P2) + odleglosc(P2, P3) + odleglosc(P3, P1)

# Przykład użycia
print(obwodTrojkata([0, 0], [1, 1], [2, 2]))