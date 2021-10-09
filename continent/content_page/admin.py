from django.contrib import admin
from .models import Page, Audio, Video, Text


class PageAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class AudioAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class VideoAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class TextAdmin(admin.ModelAdmin):
    search_fields = ('title',)


admin.site.register(Page, PageAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Text, TextAdmin)

