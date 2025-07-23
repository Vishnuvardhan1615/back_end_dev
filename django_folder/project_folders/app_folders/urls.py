from django.urls import path,include
from . import views

urlpatterns = [
  path('api_calling',views.api_calling,name='api_calling'),  # Assuming you have an 'api' app with its own urls.py
]