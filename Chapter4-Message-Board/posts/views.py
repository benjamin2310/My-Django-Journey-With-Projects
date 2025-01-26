from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Post, Author , Student

class HomePageView(ListView):
    model = Post
    template_name = "posts/home.html"

class AuthorPageView(ListView):
    model = Author
    template_name = "posts/author.html"

class StudentsPageView(ListView):
    model = Student
    template_name = "posts/student.html"