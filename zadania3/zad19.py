def rysuj_figure(typ, *args):
    if typ == "koło":
        promień = args[0]
        print(f"Rysuję koło o promieniu {promień}")
        return 3.14 * promień**2
    elif typ == "kwadrat":
        bok = args[0]
        print(f"Rysuję kwadrat o boku {bok}")
        return bok**2
    else:
        print("Nieznany typ figury")

print(rysuj_figure("koło", 5))