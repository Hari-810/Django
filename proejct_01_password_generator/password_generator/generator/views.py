from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request,"generator/index.html")

def password(request):
    characters = list("abcdefghijklmnopqurstuvwxyz")
    
    
    length = int(request.GET.get("length"))
    
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    
    if request.GET.get("special_characters"):
        characters.extend(list("!@#$%^&*()-_+={}[]|\\:;\"'"))
        
    
    password = ""
    for x in range(length):
        password = password + random.choice(characters)
    return render(request,"generator/password.html",{"password":password})