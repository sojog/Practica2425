from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .potriveste import rearanjeaza
from .flash import get_qa
import json



class ListOfListsEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, list):
			return obj
		return json.JSONEncoder.default(self, obj)
     
def home_view(request):
    context = {

    }
    return render(request, "home.html", context)

def potriveste_view(request):
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
        corect_solution=True
        corect = [False]*len(cod)
        for index, line_s in enumerate(cod):
              line_s = line_s.replace(" ", "")
              print("De comparat")
              print(line_s)
              for line_r in solution[:-1].split(";"):
                  if line_r.replace(" ","") == line_s:
                      corect[index]=True
                      break
        for i in range(len(corect)):
            if corect[i] == False:
                corect_solution = False
                break
        
        print("am primit")    
        print(solution.replace(" ", ""))
        
        
        if corect_solution:
            return HttpResponse('Ai răspuns corect')
        else:
            return HttpResponse('Nu ai răspuns corect')

    exercitiu = rearanjeaza(cod)
    print(exercitiu)
    context = {
        'exercitiu': exercitiu,
        'code': cod,
        'chei':exercitiu.keys(),
        'cuvinte':exercitiu.values()
    }
    return render(request, "potriveste.html", context)

def flash_view(request):
    cod = {"Which type of Programming does Python support?": "Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.",
           "Is Python case sensitive when dealing with identifiers?": "Case is always significant while dealing with identifiers in python.",
           "Which of the following is the correct extension of the Python file?":".py is the correct extension of the Python file.",
           "Is Python code compiled or interpreted?":"Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.",
           "What will be the value of the following Python expression? 4 + 3 % 5=":"7",
           "Which keyword is used for function in Python language?":"def",
           "Which of the following character is used to give single-line comments in Python?":"#",
           "What will be the output of the following Python code? <br> i = 1 <br> while True: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if i%3 == 0: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(i) <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i + = 1":"SyntaxError, in expression i + = 1 must have +=, without a space between + and =.",
           }
        
   
    json_output = json.dumps(cod, cls=ListOfListsEncoder)

    context = {
        'exercitiu': json_output,
        'code': cod
    }
    return render(request, "flash.html", context)

    