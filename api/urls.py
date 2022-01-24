from django.urls import path
from api.views import ShortenerCreateApiView, ShortenerListAPIView

from . import views

urlpatterns = [
    path("", ShortenerListAPIView().as_view(), name="all_links"),
    path("add/", ShortenerCreateApiView.as_view(), name="add_api")
]

