from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
      return self.title


class Video(models.Model):
    title = models.CharField(max_length=120)
    views = models.IntegerField(default=0, verbose_name='Колличество просмотров')
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Audio(models.Model):
    title = models.CharField(max_length=120)
    views = models.IntegerField(default=0, verbose_name='Колличество просмотров')
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Text(models.Model):
    title = models.CharField(max_length=120)
    views = models.IntegerField(default=0, verbose_name='Колличество просмотров')
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title