from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class BlogPageView(TemplateView):
    template_name = "pages/blog.html"

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

class ServicesPageView(TemplateView):
    template_name = "pages/services.html"