from rest_framework import serializers


class PageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)


class VideoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    counter = serializers.IntegerField()
    page_id = serializers.IntegerField()


class AudioSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    counter = serializers.IntegerField()
    page_id = serializers.IntegerField()


class TextSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    counter = serializers.IntegerField()
    page_id = serializers.IntegerField()


