from django.shortcuts import render

# Create your views here.
def simple_page(request):
    return render(request, 'things/things.html')