def szyfruj(tekst, klucz):
    zaszyfrowany = ""
    for znak in tekst:
        if znak.isalpha():
            przesuniecie = ord('A') if znak.isupper() else ord('a')
            zaszyfrowany += chr((ord(znak) - przesuniecie + klucz) % 26 + przesuniecie)
        else:
            zaszyfrowany += znak
    return zaszyfrowany

print(szyfruj("Hello, World!", 3))