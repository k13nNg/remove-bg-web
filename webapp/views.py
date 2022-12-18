from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view functions are functions that takes a request and 
# returns a response

# view functions are also called request handler

def upload_image_render(request):
    return render(request, 'upload_image.html')