from django.contrib import admin
from .models import Page, Audio, Video, Text


admin.site.register(Page)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(Text)