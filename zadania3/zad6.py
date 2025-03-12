def szukajWliscie(lista, a):
    if isinstance(a, (int, float)):
        liczba_wystapien = lista.count(a)
    elif isinstance(a, str):
        if a.isdigit():
            liczba_wystapien = lista.count(int(a))
        else:
            liczba_wystapien = lista.count(sum(ord(c) for c in a))
    elif isinstance(a, bool):
        liczba_wystapien = lista.count(1 if a else 0)
    else:
        raise TypeError("Nieobsługiwany typ danych")
    
    return liczba_wystapien

print(szukajWliscie([1, 2, 3, 4, 2, 2, 5], "2"))