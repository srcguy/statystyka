import random
from statistics import mode
from statistics import multimode
import statistics
import numpy as np

indeks = {
    "Anna Kowalska": random.randrange(1, 6),
    "Janusz Nowak": random.randrange(1, 6),
    "Wojciech Bruchal": random.randrange(1, 6),
    "Marcin Duda": random.randrange(1, 6),
    "Małgorzata Piernik": random.randrange(1, 6),
    "Gabriel Nowak": random.randrange(1, 6),
    "Oliwia Wiśniewska": random.randrange(1, 6),
    "Kacper Wójcik": random.randrange(1, 6),
    "Natalia Kaczmarek": random.randrange(1, 6),
    "Szymon Kwiatkowski": random.randrange(1, 6),
    "Zofia Kowalska": random.randrange(1, 6),
    "Filip Pawlak": random.randrange(1, 6),
    "Maja Zając": random.randrange(1, 6),
    "Michał Kowalczyk": random.randrange(1, 6),
    "Julia Mazur": random.randrange(1, 6),
    "Adam Krawczyk": random.randrange(1, 6),
    "Hanna Lewandowska": random.randrange(1, 6),
    "Mateusz Jankowski": random.randrange(1, 6),
    "Aleksandra Szymańska": random.randrange(1, 6),
    "Piotr Nowicki": random.randrange(1, 6),
    "Anna Wojciechowska": random.randrange(1, 6),
    "Kamil Grabowski": random.randrange(1, 6),
    "Zuzanna Piotrowska": random.randrange(1, 6),
    "Bartosz Tomczak": random.randrange(1, 6),
    "Laura Kwiatkowska": random.randrange(1, 6)
}

def stats(students):
    suma = sum(students.values())
    ilosc_studentow = len(students)
    srednia = suma / ilosc_studentow
    print(srednia)
    
    dominanta = multimode(students.values())
    print(dominanta)
    
    mediana = statistics.median(students.values())
    print(mediana)

    odchylenie_standardowe = np.std(list(students.values()))
    print(odchylenie_standardowe)

    return (srednia, dominanta, mediana, odchylenie_standardowe)

print(indeks)

stats(indeks)

print(stats(indeks))
