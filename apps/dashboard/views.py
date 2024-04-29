from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/index.html', {
        'disablePagination': True,
        'disableBanner': True
    })
