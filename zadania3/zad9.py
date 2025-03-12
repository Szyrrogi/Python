def czy_wspolliniowe(P1, P2, P3):
    return (P2[1] - P1[1]) * (P3[0] - P2[0]) == (P3[1] - P2[1]) * (P2[0] - P1[0])

print(czy_wspolliniowe([0, 0], [1, 1], [2, 2]))