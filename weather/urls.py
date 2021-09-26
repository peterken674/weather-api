from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/locations/(?P<city>\D+)/$', views.Results.as_view()),
]