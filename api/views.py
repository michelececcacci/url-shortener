from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from sympy import re
from .models import Site
from .serializer import SiteSerializer
from django.conf import  settings
from rest_framework import exceptions



class ShortenerListAPIView(ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class ShortenerCreateApiView(CreateAPIView):
    serializer_class = SiteSerializer

class ShortenerLinkInfo(RetrieveAPIView):
    serializer_class = SiteSerializer
    def get(self, request, short, *args, **kwargs):
        short_link = settings.BASE_URL + self.kwargs['short']
        shortened_instance = get_object_or_404(Site, short=short_link)
        serializer =  self.get_serializer(shortened_instance)
        return Response(serializer.data)

class ShortenerClickLink(RetrieveAPIView):
    serializer_class = SiteSerializer
    def get(self, request, short, *args, **kwargs):
        short_link = settings.BASE_URL + self.kwargs['short']
        shortened_instance = get_object_or_404(Site, short=short_link)
        shortened_instance.clicked += 1
        shortened_instance.save()
        serializer = self.get_serializer(shortened_instance)
        return Response(serializer.data)


class TopClicked(ListAPIView):
    queryset = Site.objects.order_by('-clicked')[:5]
    serializer_class = SiteSerializer
