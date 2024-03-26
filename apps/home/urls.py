from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("libraries/", views.library_view, name="libraries"),
]