from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.html")

def library_view(request):
    return render(request, "home/libraries.html", {'activeMenu': 'library'})
