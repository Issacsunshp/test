from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image_bat = models.CharField(max_length=100)
    ocr_letter = models.CharField(max_length=100)