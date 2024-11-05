## Logica de business a generariid e exercitii

import random

def rearanjeaza(cod):
    cuvinte = cod.split()
    # print(cuvinte)

    random.shuffle(cuvinte)
    # print(cuvinte)

    exercitiul_de_reordonare = " ".join(cuvinte)
    # print(exercitiul_de_reordonare)

    return exercitiul_de_reordonare


if __name__ == "__main__":
    cod = """<a href = "default.html"> Visit our HTML tutorial. </a>"""
    exercitiu = rearanjeaza(cod)
    print(exercitiu)

