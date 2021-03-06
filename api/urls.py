from django.urls import path
from api.views import ShortenerCreateApiView, ShortenerLinkInfo, ShortenerListAPIView

from . import views

urlpatterns = [
    path("", ShortenerListAPIView().as_view(), name="all_links"),
    path("add/", ShortenerCreateApiView.as_view(), name="add_api"),
    path("infos/<str:short>", ShortenerLinkInfo.as_view(), name="infos")
]

