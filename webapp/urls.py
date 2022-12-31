from django.contrib import admin
from django.urls import path, include
from . import views


# URLConf
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('upload_image/', views.upload_image_render),
    path('index/', views.main_render, name="index"),  # default page
    path('about/', views.about_render, name="about"),
    path('signup/', views.signup, name="signup" ),
    path('view_image/', views.view_image),
    path('gallery/', views.gallery)
]

