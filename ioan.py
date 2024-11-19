# 1. Raspuns doar 1 cuvant - 8, append, float
# 2. Expresie Python - care trebuie evaluata (ex: functia eval)
# 3. Mai multe valori

def test_python():
    intrebari = [
        {
            "intrebare": "Care este rezultatul expresiei: 5 + 3?",
            "raspuns_corect": "8"
        },
        {
            "intrebare": "Cum se adaugă un element la o listă în Python?",
            "raspuns_corect": "append"
        },
        {
            "intrebare": "Ce tip de date este rezultatul expresiei 3.14?",
            "raspuns_corect": "float"
        },
        {
            "intrebare": "Cum se creează un dicționar în Python?",
            "raspuns_corect": "{'cheie': 'valoare'}"
        },
        {
            "intrebare": "Ce se întâmplă când încerci să împarți un număr la zero în Python?",
            "raspuns_corect": "ZeroDivisionError"
        },
        {
            "intrebare": "Cum afișezi un mesaj pe ecran în Python?",
            "raspuns_corect": "print()"
        },
        {
            "intrebare": "Cum creezi o variabilă de tip șir de caractere în Python?",
            "raspuns_corect": "'mesaj' sau \"mesaj\""
        },
        {
            "intrebare": "Ce face funcția len() în Python?",
            "raspuns_corect": "Returneaza lungimea unui obiect"
        },
        {
            "intrebare": "Ce face operatorul == în Python?",
            "raspuns_corect": "Compara doua valori"
        },
        {
            "intrebare": "Care este diferența dintre list și tuple în Python?",
            "raspuns_corect": "list este mutabila, tuple este imutabila"
        }
    ]
    
    scor = 0

    for intrebare in intrebari:
        print("\n" + intrebare["intrebare"])
        raspuns = input("Răspunsul tău: ").strip().lower()
        
        if raspuns == intrebare["raspuns_corect"].lower():
            print("Corect!")
            scor += 1
        else:
            print(f"Greșit! Răspunsul corect era: {intrebare['raspuns_corect']}")

    print(f"\nTestul s-a încheiat! Ai obținut {scor} din {len(intrebari)} puncte.")

test_python()

## 2. Evaluare
raspuns = input("Cum creezi un dictionar in Python\n")
print(raspuns)
x =  eval(raspuns)
print(type(x) == dict)
assert type(x) == dict, 'X nu este dictionar'

## 3. Mai multe raspunsuri
raspuns = input("Cum creezi o variabilă de tip șir de caractere în Python?")
print(raspuns)
raspunsuri_corecte = ["'mesaj'", '"mesaj"', '"""mesaj"""']
if raspuns in raspunsuri_corecte:
    print("Ai raspuns corect")
else:
    print("Nu ai raspuns corect")