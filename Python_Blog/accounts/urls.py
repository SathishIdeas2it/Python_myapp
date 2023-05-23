from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path('add_post/', views.add_post, name='add_post'),
     path('post_list/', views.post_list, name='post-list'),
]
