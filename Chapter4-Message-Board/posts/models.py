from django.db import models

class Post(models.Model):
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.text[:250]

class Author(models.Model):
    author_name = models.TextField()
    author_email = models.EmailField()
    author_date = models.DateField()

    def __str__(self):
        return self.author_email[:50]

class Student(models.Model):
    name = models.TextField(max_length=200)
    school = models.TextField(max_length=200)
    student_email = models.EmailField()
    student_programme = models.TextField(max_length=200)

    def __str__(self):
        return self.student_programme[:50]

