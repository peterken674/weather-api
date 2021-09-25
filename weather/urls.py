from django.urls import path
from . import views

urlpatterns = [
    path('api/locations/<city>/<num_of_days>/', views.Results.as_view())
]