from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

# import the AI model
#from rembg import remove
#from PIL import Image

# Create your views here.
# view functions are functions that takes a request and
# returns a response

# view functions are also called request handler


def main_render(request):
    return render(request, 'index.html')


def navbar_render(request):
    navbar = loader.get_template('navbar.html')
    return HttpResponse(navbar.render())


def login(request):
    return render(request, 'login.html')


def upload_image_render(request):
    return render(request, 'upload_image.html')


def about_render(request):
    return render(request, 'about.html')

# def get_remove_bg_image(request):
#     image_to_process = request.GET.get("img", None)
#     return remove(image_to_process)
        
    

