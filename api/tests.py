from django.test import TestCase
from api.models import Site

class SiteGenerationTestCase(TestCase):
    def site_creation_test(self):
        original_long = "https://www.google.com/"
        google_site = Site.objects.create(long=original_long)
        generated_short = google_site.short
        db_long  = Site.objects.filter(short=generated_short).first().long
        self.assertEqual(db_long, original_long)