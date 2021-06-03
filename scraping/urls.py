from django.urls import path
from .views import ScrapingView

urlpatterns=[
    path("", ScrapingView.as_view(), name="home"),
]