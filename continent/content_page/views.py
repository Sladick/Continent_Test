from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Page, Video, Audio, Text
from .serializers import PageSerializer, VideoSerializer, AudioSerializer, TextSerializer, Page1Serializer
from django.db.models import F


class PageView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ContentView(APIView):
    def get(self, request, pk):
        video_articles = Video.objects.filter(page_id=pk)
        serializer_video = VideoSerializer(video_articles, many=True)
        audio_articles = Audio.objects.filter(page_id=pk)
        serializer_audio = AudioSerializer(audio_articles, many=True)
        text_articles = Text.objects.filter(page_id=pk)
        serializer_text = TextSerializer(text_articles, many=True)
        page_articles = Page.objects.filter(id=pk)
        serializer_page = Page1Serializer(page_articles, many=True)

        video_counter_list = Video.objects.filter(page_id=pk)
        for video_counter in video_counter_list:
            video_counter.views = F('views') + 1
            video_counter.save()
            video_counter.refresh_from_db()

        audio_counter_list = Audio.objects.filter(page_id=pk)
        for audio_counter in audio_counter_list:
            audio_counter.views = F('views') + 1
            audio_counter.save()
            audio_counter.refresh_from_db()

        text_counter_list = Text.objects.filter(page_id=pk)
        for text_counter in text_counter_list:
            text_counter.views = F('views') + 1
            text_counter.save()
            text_counter.refresh_from_db()

        return Response({f"Page {pk}": serializer_page.data, 'Content ':{"Video": serializer_video.data, "Audio": serializer_audio.data, "Text": serializer_text.data}})

