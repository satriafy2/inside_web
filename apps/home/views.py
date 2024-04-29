from django.shortcuts import render

def index(request):
    return render(request, 'home.html', {'showBanner': True})

def library_view(request):
    return render(request, 'library/list.html', {
        'activeMenu': 'library',
        'showBanner': True,
        'showPagination': True
    })

def topic_view(request):
    return render(request, 'topic/list.html', {
        'activeMenu': 'topic',
        'showBanner': True,
        'showPagination': True
    })

def learning_view(request):
    return render(request, 'learning/list.html', {
        'activeMenu': 'learning',
        'showBanner': True,
        'showPagination': True
    })

def course_view(request):
    category = request.GET.get('category', None)
    render_html = 'course/categories.html'
    show_page = False
    
    if category:
        render_html = 'course/list.html'
        show_page = True
        category = category.replace('-', ' ')

    return render(request, render_html, {
        'activeMenu': 'course',
        'showBanner': True,
        'showPagination': show_page,
        'courseCategory': category.title() if category else None
    })

def course_detail_view(request, courseSlug):
    return render(request, 'course/detail.html', {'activeMenu': 'course'})
    
def learning_detail_view(request, learningSlug):
    return render(request, 'learning/detail.html', {'activeMenu': 'learning'})

def library_detail_view(request, librarySlug):
    return render(request, 'library/detail.html', {'activeMenu': 'library'})
