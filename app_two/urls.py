from django.urls import path
from app_two import views

urlpatterns = [
    path('', views.help, name="help")
]
