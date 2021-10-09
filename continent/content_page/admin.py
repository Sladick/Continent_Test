from django.contrib import admin
from .models import Page, Audio, Video, Text


class AudioInline(admin.TabularInline):
    model = Audio


class VideoInline(admin.TabularInline):
    model = Video


class TextInline(admin.TabularInline):
    model = Text


class PageAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [
        AudioInline,
        VideoInline,
        TextInline
    ]


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

