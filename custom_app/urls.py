from django.urls import path
from custom_app import views

urlpatterns = [path("hello", views.say_hello)]
