from .import views
from django.urls import path

urlpatterns = [
    path('', views.web, name='web'),
]