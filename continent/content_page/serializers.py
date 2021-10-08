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
    page_id = serializers.IntegerField()


class AudioSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    views = serializers.IntegerField()
    page_id = serializers.IntegerField()


class TextSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    views = serializers.IntegerField()
    page_id = serializers.IntegerField()