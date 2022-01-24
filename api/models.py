from string import ascii_letters
from django.db import models
from django.forms import DateField
from django.utils import timezone
from random import choices
from django.conf import settings

class Site(models.Model):
    short = models.URLField(blank=True, null=True)
    long = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    clicked = models.IntegerField(default=0)

    def shortener(self):
        while True:
            string_list = choices(ascii_letters + "".join([str(i) for i in range(10)]), k=6)
            random_string = "".join(string_list)
            new_link = settings.BASE_URL + random_string

            if not Site.objects.filter(short=new_link).exists():
                break

        return new_link

    def save(self, *args, **kwargs):
        if not self.short:
            new_link = self.shortener()
            self.short = new_link
        return super().save(*args, **kwargs)