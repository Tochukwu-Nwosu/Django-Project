from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    first_time = models.CharField(max_length=200)
    second_time = models.CharField(max_length=200)

    def __str__(self):
        return self.title