# generator/views.py

from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, "generator/index.html")

def password(request):
    if request.method == 'POST':
        characters = list("abcdefghijklmnopqurstuvwxyz")

        length = int(request.POST.get("length"))

        if request.POST.get("uppercase"):
            characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

        if request.POST.get("numbers"):
            characters.extend(list("1234567890"))

        if request.POST.get("special_characters"):
            characters.extend(list("!@#$%^&*()-_+={}[]|\\:;\"'"))

        password = ""
        for x in range(length):
            password = password + random.choice(characters)
        return render(request, "generator/password.html", {"password": password})
    return HttpResponse("Wrong Request")
