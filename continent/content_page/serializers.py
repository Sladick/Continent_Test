from rest_framework import serializers
from .models import Page


class PageSerializer(serializers.ModelSerializer):
    Page_Detail_Url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['title', 'Page_Detail_Url']

    def get_Page_Detail_Url(self, Page):
        return (f'http://127.0.0.1:8000/{Page.pk}')


class VideoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    views = serializers.IntegerField()
    video_file = serializers.FileField()
    url_video_file = serializers.URLField()
    url_sub_file = serializers.URLField()


class AudioSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    views = serializers.IntegerField()
    audio_file = serializers.FileField()
    audio_bitrate = serializers.FloatField()


class TextSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    views = serializers.IntegerField()
    text = serializers.CharField()


class Page1Serializer(serializers.Serializer):
    title = serializers.CharField()




