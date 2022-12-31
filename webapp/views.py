from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from .models import Upload_Image, Processed_Image
from rembg import remove
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def main_render(request):
    return render(request, 'index.html')


def navbar_render(request):
    navbar = loader.get_template('navbar.html')
    return HttpResponse(navbar.render())

def view_image(request):
    img = Processed_Image.objects.last()

    context = {'img_to_display': img}

    return render(request, 'view_image.html', context)

def upload_image_render(request):
    processed_image=0
    image = ""
    image_to_display=0

    if request.method == "POST":
        data = request.POST
        image = request.FILES['image']
        user = request.user
        if not user.is_authenticated:
            user = None

        Upload_Image.objects.create(image=image)

        processed_image = remove(Image.open(BytesIO(image.read())))
        buffer = BytesIO()
        processed_image.save(buffer, format='PNG')
        image_file = InMemoryUploadedFile(buffer, None, 'dummy.png', 'image/png', buffer.getbuffer().nbytes, None)
        Processed_Image.objects.create(save_image= image_file, user = user)

        image_to_display = Processed_Image.objects.last()

        return redirect('../view_image/')

    return render(request, 'upload_image.html')


def about_render(request):
    return render(request, 'about.html')

def gallery(request):
    images = request.user.processed_image_set.all()
    context = {'images': images}
    return render(request, "gallery.html", context)

        
    

