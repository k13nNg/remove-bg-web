from django.contrib import admin

# Register your models here.
from .models import Upload_Image, Processed_Image

admin.site.register(Upload_Image)
admin.site.register(Processed_Image)
