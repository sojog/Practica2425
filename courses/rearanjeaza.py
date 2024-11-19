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



def rearanjeaza_in_dict(cod):
    print(cod)
    lista_code = []
    lista_key = []
    rezultat = {}
    for line_s in cod:
        code_p = line_s.split("#")
        lista_key.append(code_p[0])
        lista_code.append(code_p[1])
        
    print("{}:{}".format(lista_key, lista_code))

    random.shuffle(lista_key)
    print("Noul code    ")
    i=0
    for i_code in lista_code:
        rezultat[lista_key[i]]=i_code
        print("{}:{}".format(i, i_code))
        i+=1
    
    print(rezultat)

    #exercitiul_de_reordonare = " ".join(cuvinte)
    # print(exercitiul_de_reordonare)
    return rezultat


if __name__ == "__main__":
    cod = """<a href = "default.html"> Visit our HTML tutorial. </a>"""
    exercitiu = rearanjeaza(cod)
    print(exercitiu)

