import statistics

def statystyki(lista):
    return {
        "mediana": statistics.median(lista),
        "średnia": statistics.mean(lista),
        "min": min(lista),
        "max": max(lista),
        "odchylenie standardowe": statistics.stdev(lista)
    }

print(statystyki([1, 2, 3, 4, 5]))