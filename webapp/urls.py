from django.contrib import admin
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('upload_image/', views.upload_image_render),
    path('index/', views.main_render)  # default page
]
