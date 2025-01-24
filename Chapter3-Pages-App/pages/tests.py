from django.test import SimpleTestCase
from django.urls import reverse

# Testing for the Status of the Page
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
#Testing for the URL for the page
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # Testing for the template name and content
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Welcome to DevOps Engineering</h1>")

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

# Testing for the template name and content
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h3>I am Benjamin a DevOps Engineer with 3yrs Experience. I currently live in USA-Chicago and I work with Amazon.</h3>")

class BlogpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("blog"))
        self.assertTemplateUsed(response, "pages/blog.html")

    def test_template_content(self):
        response = self.client.get(reverse("blog"))
        self.assertContains(response, "<p>Lorem Ipsum Welcome to Software Employment</p>")

class ServicespageTests(SimpleTestCase):
    def tests_url_exists_at_correct_location(self):
        response = self.client.get("/services/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("services"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("services"))
        self.assertTemplateUsed(response, "pages/services.html")

    def test_template_content(self):
        response = self.client.get(reverse("services"))
        self.assertContains(response, "<h1>We Offer Variety of Services</h1>")

class ContactpageTests(SimpleTestCase):
    def tests_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)


    def test_template_name_correct(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "pages/contact.html")

    def test_template_content(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h1>Please Kindly Contact Us</h1>")