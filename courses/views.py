from django.shortcuts import render
from .models import Question, Answer
# Create your views here.
from django.http import HttpResponse
from .rearanjeaza import rearanjeaza, rearanjeaza_in_dict

def home_view(request):
    context = {

    }
    return render(request, "home.html", context)


def potrivire_view(request):
    cod = ["""<a href =# "default.html"> Visit our HTML tutorial. </a>""","""<a href = "default.html"># Visit our HTML tutorial. </a>""","""<a href = "default.html"> Visit our HTML tutorial. #</a>"""]
    code_l=""
    for line_s in cod:
        print(line_s)
        code_l += line_s + "#"
    code_l = code_l.replace(" ", "")
    code_l = code_l[:-1]
    print("Codul este:")
    print(code_l)
    
    if request.method == "POST":
        solution = request.POST.get('solution')
        print(solution.replace(" ", ""))
        print("am primit")
        
        if code_l == solution.replace(" ", ""):
            return HttpResponse('Ai răspuns corect')
        else:
            return HttpResponse('Nu ai răspuns corect')

    exercitiu = rearanjeaza_in_dict(cod)
    print(exercitiu)
    context = {
        'exercitiu': exercitiu,
        'code': cod,
        'chei':exercitiu.keys(),
        'cuvinte':exercitiu.values()
    }
    return render(request, "potriveste.html", context)


def rearange_view(request):
    cod = """<a href = "default.html"> Visit </a>"""

    if request.method == "POST":
        solution = request.POST.get('solution')
        print("Primesc:", solution)
        solution = solution.replace("  ", " ")

        if cod == solution:
            return HttpResponse('Ai răspuns corect')
        else:
            return HttpResponse('Nu ai răspuns corect')

    exercitiu = rearanjeaza(cod)
    print(exercitiu)
    context = {
        
        'exercitiu': exercitiu,
        'cuvinte':exercitiu.split()
    }
    return render(request, "rearanjare.html", context)


def rearange_input_view(request):
    cod = """<a href = "default.html"> Visit </a>"""

    if request.method == "POST":
        print(request.POST)
        param_keys = request.POST.keys()
        print(request.POST.keys())
        param_keys = [k for k in param_keys if k.startswith('solution_part')]
        param_keys.sort()
        
        solution = ""
        for key in param_keys:
            if solution:
                solution += (" " + request.POST.get(key))
            else:
                solution += (request.POST.get(key))

        print("Primesc:", solution)
        solution = solution.replace("  ", " ")

        if cod == solution:
            return HttpResponse('Ai răspuns corect')
        else:
            return HttpResponse('Nu ai răspuns corect')

    exercitiu = rearanjeaza(cod)
    print(exercitiu)
    context = {
        'exercitiu': exercitiu,
        'cuvinte':cod.split()
    }
    return render(request, "rearanjare_input.html", context)

def multiple_answers_view(request):
    first_question = Question.objects.all().first()
    answers = Answer.objects.filter(question = first_question)

    context = {
        'question': first_question.text,
        'answers':[ans.text for ans in answers]
    }
    return render(request, "multiple_answers.html", context)


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

import json 

def flash_view(request):
    cod = {
        "Which of the following is the attribute in this example?": "href",
        "Which input type is used for selecting one of many choices?": "radio",
    }
        
    if request.method == "POST":
        solution = request.POST.get('solution')
        print(solution.replace(" ", ""))
        print("am primit")
    
    exercitiu = get_qa(cod)
    print(exercitiu)
    context = {
        'exercitiu': exercitiu,
        'exercitiustr': json.dumps(exercitiu),
        'code': cod
    }
    return render(request, "flash.html", context)