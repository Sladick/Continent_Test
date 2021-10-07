from django.urls import path
from .views import PageView, VideoView

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', PageView.as_view()),
    path('video/<pk>/', VideoView.as_view()),
]