from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView
from sympy import re
from .models import Site
from .serializer import SiteSerializer
from django.conf import  settings
import pdb
from rest_framework import exceptions



class ShortenerListAPIView(ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class ShortenerCreateApiView(CreateAPIView):
    serializer_class = SiteSerializer

class Redirector(View):
    def get(self, request, short, *args, **kwargs):
        short_link = settings.BASE_URL + self.kwargs["short"]
        redirect_instance = get_object_or_404(Site, short=short_link)
        redirect_instance.clicked += 1
        redirect_instance.save()
        return redirect(redirect_instance.long)


class TopClicked(ListAPIView):
    queryset = Site.objects.order_by('-clicked')[:5]
    serializer_class = SiteSerializer
