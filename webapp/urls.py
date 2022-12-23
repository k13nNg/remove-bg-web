from django.contrib import admin
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('upload_image/', views.upload_image_render),
    path('index/', views.main_render, name="index"),  # default page
    path('about/', views.about_render, name="about"),
    # path('generate/', views.get_remove_bg_image, name = "generate_adjusted_image")
]
