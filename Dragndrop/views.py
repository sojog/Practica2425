from django.shortcuts import render
import json
import random
from django.http import JsonResponse

def joaca_jocul(request):
    with open(r"Dragndrop/capitale.json", "r") as f:
        data = json.load(f)
    
    # Select random elements (e.g., 2 items)
    random_items = random.sample(data, 5)  # Adjust number of items as needed

    countries = [item["country"] for item in random_items]
    capitals =  [item["city"] for item in random_items]
    print("countries:", countries)
    print("capitals:", capitals)


    random.shuffle(capitals)
    random.shuffle(countries)


    # Pass the random items to the template
    return render(request, "dragndrop.html", {"items": random_items, "countries": countries, "capitals":capitals})


def verifica_tara_view(request):
    print("Request venit pentru verifica_tara_view", request.GET)
    r_country = request.GET.get("country")
    r_city  = request.GET.get("city")

    with open(r"Dragndrop/capitale.json", "r") as f:
        data = json.load(f)

    for obj in data:
        if obj["country"] == r_country:
            return JsonResponse(obj["city"] == r_city, safe=False)
        
    return JsonResponse(False, safe=False)