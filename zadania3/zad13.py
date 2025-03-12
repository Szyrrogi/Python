def sortuj_liste(lista, kierunek="rosnąco"):
    return sorted(lista, reverse=(kierunek == "malejąco"))

print(sortuj_liste([3, 1, 4, 1, 5, 9], "malejąco"))