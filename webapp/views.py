from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# view functions are functions that takes a request and
# returns a response

# view functions are also called request handler


def main_render(request):
    return render(request, 'index.html')


def navbar_render(request):
    navbar = loader.get_template('navbar.html')
    return HttpResponse(navbar.render())


def upload_image_render(request):
    return render(request, 'upload_image.html')


def about_render(request):
    return render(request, 'about.html')
