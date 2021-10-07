from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Page, Video, Audio, Text
from .serializers import PageSerializer, VideoSerializer, AudioSerializer, TextSerializer


class PageView(APIView):
    def get(self, request):
        articles = Page.objects.all()
        serializer = PageSerializer(articles, many=True)
        return Response(serializer.data)



class VideoView(APIView):
    def get(self, request, pk):
        articles = Video.objects.filter(page_id=pk)
        serializer = VideoSerializer(articles, many=True)
        articles2 = Audio.objects.filter(page_id=pk)
        serializer2 = AudioSerializer(articles2, many=True)
        articles3 = Text.objects.filter(page_id=pk)
        serializer3 = TextSerializer(articles3, many=True)
        return Response({"Video": serializer.data, "Audio": serializer2.data, "Text": serializer3.data, })

