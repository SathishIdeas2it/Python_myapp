from django.urls import path
from .import views

urlpatterns = [
    path("", views.audio_to_text, name="audio_to_text")
] 
