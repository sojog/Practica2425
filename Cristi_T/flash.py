import random
from pprint import pprint

def get_qa(cod):
    print(cod)

  
    lista_code = []
    lista_key = []
    rezultat = []


    for i_key in cod.keys():       
        lista_key.append(i_key)
    
    random.shuffle(lista_key)

    print("Noua lista:    ")

    rezultat = []

    for i, i_key in enumerate(lista_key):
     #   rezultat[i][0] = i_key
     #   rezultat[i][1] = cod[i_key]
        rezultat.append([i_key, cod[i_key]])
    
    pprint (rezultat)

    return rezultat

if __name__ == "__main__":
    cod = {"Which of the following is the 'attribute' in this example? <a href='#' id='MyId'>Click me</a>": "href",
           "Which attribute will <img> tags display if the image cannot be loaded?": "alt",
           "Which tag will create a list which displays numbers next to each item by default?":"<ol>",
           "Which element will create a text input on a form?":"<input />",
           "Which input type is used for selecting one of many choices?":"radio",
           }
    exercitiu = get_qa(cod)
    print(exercitiu)