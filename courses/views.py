from django.shortcuts import render
from .models import Question, Answer
# Create your views here.

def home_view(request):
    context = {

    }
    return render(request, "home.html", context)


def multiple_answers_view(request):
    first_question = Question.objects.all().first()
    answers = Answer.objects.filter(question = first_question)

    context = {
        'question': first_question.text,
        'answers':[ans.text for ans in answers]
    }
    return render(request, "multiple_answers.html", context)