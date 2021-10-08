from django.urls import path
from .views import PageView, ContentView

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', PageView.as_view()),
    path('<pk>/', ContentView.as_view()),
]