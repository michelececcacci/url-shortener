from urllib import request
from django.conf import settings
from django.test import RequestFactory, TestCase
from api.models import Site
from api.views import ShortenerClickLink, ShortenerLinkInfo
from urllib.parse import  urlparse

class SiteGenerationTestCase(TestCase):
    def setUp(self):
        self.google_site = Site.objects.create(long="https://www.google.com/")

    def test_generate_site(self):
        returned_site = Site.objects.get(long="https://www.google.com/")
        self.assertEquals(returned_site, self.google_site)

    def test_default_clicks_zero(self):
        self.assertEquals(self.google_site.clicked, 0)

    def test_increment_clicks(self):
        factory = RequestFactory()
        url_path = urlparse(self.google_site.short).path
        final_url  = settings.BASE_URL + url_path[1:] + "/"
        request = factory.get(final_url)
        response = ShortenerClickLink().as_view()(request, short=url_path[1:])
        self.assertEquals(response.data['clicked'], 1)