from django.urls import path
from .views import PageView, ContentView

urlpatterns = [
    path('', PageView.as_view()),
    path('<pk>/', ContentView.as_view()),
]