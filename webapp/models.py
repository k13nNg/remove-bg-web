from django.db import models
from PIL import Image

# Create your models here.
class Upload_Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
