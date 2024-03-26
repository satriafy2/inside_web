from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.html")

def library_view(request):
    return render(request, "home/libraries.html", {'activeMenu': 'library'})

def topic_view(request):
    return render(request, "home/topic.html", {'activeMenu': 'topic'})

def learning_view(request):
    return render(request, "home/learning.html", {'activeMenu': 'learning'})

def course_view(request):
    return render(request, "home/course.html", {
        'activeMenu': 'course',
        'disablePagination': True
    })
