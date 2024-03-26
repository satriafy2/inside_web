from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("libraries/", views.library_view, name="libraries"),
    path("topic/", views.topic_view, name="topic"),
    path("learning/", views.learning_view, name="learning"),
]