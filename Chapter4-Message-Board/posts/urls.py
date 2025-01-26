from django.urls import path

from .views import HomePageView, AuthorPageView, StudentsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("author/", AuthorPageView.as_view(), name="author"),
    path("student/", StudentsPageView.as_view(), name="student"),
]