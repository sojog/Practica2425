from django.shortcuts import render
from .models import Question, Answer
# Create your views here.
from django.http import HttpResponse
from .rearanjeaza import rearanjeaza

def home_view(request):
    context = {

    }
    return render(request, "home.html", context)

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