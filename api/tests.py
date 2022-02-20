from django.test import TestCase
from api.models import Site
from api.views import Redirector

class SiteGenerationTestCase(TestCase):
    def setUp(self):
        self.google_site = Site.objects.create(long="https://www.google.com/")

    def test_generate_site(self):
        returned_site = Site.objects.get(long="https://www.google.com/")
        self.assertEquals(returned_site, self.google_site)

    def test_default_clicks_zero(self):
        self.assertEquals(self.google_site.clicked, 0)

