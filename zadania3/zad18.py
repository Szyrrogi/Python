def konwertuj_temperature(temp, z_skali, do_skali):
    if z_skali == "C" and do_skali == "F":
        return temp * 9/5 + 32
    elif z_skali == "F" and do_skali == "C":
        return (temp - 32) * 5/9
    else:
        return temp

print(konwertuj_temperature(100, "C", "F"))