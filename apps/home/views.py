from django.shortcuts import render

def index(request):
    return render(request, "home.html")

def library_view(request):
    return render(request, "library/list.html", {'activeMenu': 'library'})

def topic_view(request):
    return render(request, "topic/list.html", {'activeMenu': 'topic'})

def learning_view(request):
    return render(request, "learning/list.html", {'activeMenu': 'learning'})

def course_view(request):
    category = request.GET.get('category', None)
    render_html = 'course/categories.html'
    disable_page = True
    
    if category:
        render_html = 'course/list.html'
        disable_page = False
        category = category.replace('-', ' ')

    return render(request, render_html, {
        'activeMenu': 'course',
        'disablePagination': disable_page,
        'courseCategory': category.title() if category else None
    })

def course_detail_view(request, courseSlug):
    return render(request, 'course/detail.html', {
        'activeMenu': 'course',
        'disablePagination': True,
        'disableBanner': True
    })
    
def learning_detail_view(request, learningSlug):
    return render(request, 'learning/detail.html', {
        'activeMenu': 'learning',
        'disablePagination': True,
        'disableBanner': True
    })
