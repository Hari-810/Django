from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 12))
    include_uppercase = 'uppercase' in request.GET
    include_numbers = 'numbers' in request.GET
    include_special = 'special' in request.GET

    characters = list(string.ascii_lowercase)
    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_special:
        characters.extend(string.punctuation)

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    print(generated_password)
    return render(request, 'generator/password.html', {'password': generated_password})
