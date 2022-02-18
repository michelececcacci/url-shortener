from django.shortcuts import redirect
from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView
from sympy import re
from .models import Site
from .serializer import SiteSerializer
from django.conf import  settings


class ShortenerListAPIView(ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class ShortenerCreateApiView(CreateAPIView):
    serializer_class = SiteSerializer

class Redirector(View):
    def get(self, request, short, *args, **kwargs):
        short_link = settings.BASE_URL + self.kwargs["short"]
        redirect_instance = Site.objects.filter(short=short_link).first()
        redirect_instance.clicked += 1
        redirect_instance.save()
        return redirect(redirect_instance.long)

class TopClicked(ListAPIView):
    queryset = Site.objects.order_by('-clicked')[:5]
    serializer_class = SiteSerializer
