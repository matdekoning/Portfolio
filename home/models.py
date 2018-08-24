from django.db import models
from PIL import Image
from django.urls import path
import os
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class Article(models.Model):
    image = models.ImageField(blank=False, upload_to="static/images", default='album_logos/no-image.jpg')
    url = models.CharField(max_length=180, blank=True)
    pic_id = models.AutoField(primary_key=True)

    def save(self):
        self.url = '/images/' + str(self.image)

        super(Article, self).save()
    def __str__(self):
        return self.url


