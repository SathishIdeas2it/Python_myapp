from django.urls import path,include
from .import views

urlpatterns = [
    path("", views.consume_api, name="consume-api"),
] 
