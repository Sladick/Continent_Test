from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, verbose_name='Url', unique=True, default='http://127.0.0.1:8000/api/video//')

    def __str__(self):
      return self.title


class Video(models.Model):
    title = models.CharField(max_length=120)
    counter = models.IntegerField(default=0, blank=True)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Audio(models.Model):
    title = models.CharField(max_length=120)
    counter = models.IntegerField(default=0, blank=True)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Text(models.Model):
    title = models.CharField(max_length=120)
    counter = models.IntegerField(default=0, blank=True)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title