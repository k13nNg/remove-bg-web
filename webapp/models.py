from django.db import models
from PIL import Image

# Create your models here.
class Upload_Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

class Processed_Image(models.Model):
    save_image = models.ImageField(null=False, blank=False, upload_to="processed_images")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.save_image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.save_image.path)