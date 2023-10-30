# Import necessary modules and classes
from django.shortcuts import render, redirect
from .models import BusTiming
from .forms import BusTimingForm

# View function for displaying and processing the bus timing form
def bus_timing_form(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        # Create a BusTimingForm instance with the POST data
        form = BusTimingForm(request.POST)
        
        # Check if the form data is valid (passes validation rules)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Redirect to the same page after successful form submission
            return redirect('bus_timing_form')
    
    # If the request method is GET (initial form display) or if form validation failed,
    # create a new, empty BusTimingForm instance
    else:
        form = BusTimingForm()
    
    # Render the 'bus_timing_form.html' template and pass the form as context data
    return render(request, 'bustimings/bus_timing_form.html', {'form': form})

# View function for searching bus timings by bus name
def search_bus(request):
    # Check if the HTTP request method is GET
    if request.method == 'GET':
        # Retrieve the 'bus_name' parameter from the query string; default to an empty string if not present
        bus_name = request.GET.get('bus_name', '')
        
        # Perform a case-insensitive search for bus timings whose bus_name contains the specified text
        bus_timings = BusTiming.objects.filter(bus_name__icontains=bus_name)
        
        # Render the 'bus_search.html' template and pass the search results as context data
        return render(request, 'bustimings/bus_search.html', {'bus_timings': bus_timings})
