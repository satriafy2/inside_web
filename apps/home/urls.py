from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("libraries/", views.library_view, name="libraries"),
    path("topic/", views.topic_view, name="topic"),
    path("learning/", views.learning_view, name="learning"),
    path("course/", views.course_view, name="course"),
    path("course/<slug:courseSlug>/", views.course_detail_view, name="course_detail"),
    path("learning/<slug:learningSlug>/", views.learning_detail_view, name="learning_detail"),
    path("libraries/<slug:librarySlug>/", views.library_detail_view, name="library_detail"),
]