# form_demo/views.py

from django.shortcuts import render
from django.http import HttpResponse

def form_view(request):
    return render(request, "form_demo/form.html")

def submit_view(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")

        # Process the data (in this example, just displaying it)
        return render(request, "form_demo/submit.html", {"name": name, "email": email})
    else:
        # Redirect to the form page if accessed via GET
        return render(request, "form_demo/form.html")
