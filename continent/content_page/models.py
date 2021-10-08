from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
      return self.title


class Video(models.Model):
    title = models.CharField(max_length=120)
    views = models.IntegerField(default=0, verbose_name='Колличество просмотров')
    video_file = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='Видео', blank=True)
    url_video_file = models.URLField(null=True, blank=True)
    url_sub_file = models.URLField(null=True, blank=True)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Audio(models.Model):
    title = models.CharField(max_length=120)
    views = models.IntegerField(default=0, verbose_name='Колличество просмотров')
    audio_file = models.FileField(upload_to='audio/%Y/%m/%d/', verbose_name='Аудио', blank=True)
    audio_bitrate = models.FloatField(null=True, blank=True)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Text(models.Model):
    title = models.CharField(max_length=120)
    views = models.IntegerField(default=0, verbose_name='Колличество просмотров')
    text = models.TextField(null=True, blank=True)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.title