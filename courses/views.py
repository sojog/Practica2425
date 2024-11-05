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


def multiple_answers_view(request):
    first_question = Question.objects.all().first()
    answers = Answer.objects.filter(question = first_question)

    context = {
        'question': first_question.text,
        'answers':[ans.text for ans in answers]
    }
    return render(request, "multiple_answers.html", context)