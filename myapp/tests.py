from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content.decode(),
            "<h1>Hello world! This is the homepage of my app</h1>",
        )

    def test_about_view(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content.decode(),
            "<h1>About Page</h1><p>This is the about page of my Django application.</p>",
        )

    def test_api_status_view(self):
        response = self.client.get(reverse("api_status"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"status": "ok", "app": "csc325Djangoproj"},
        )
