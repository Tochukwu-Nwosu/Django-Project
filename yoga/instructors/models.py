from django.db import models

# Create your models here.

class Image_row1(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Image_row2(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name