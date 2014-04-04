from django.contrib import admin
from mythos.models import *
# Register your models here.

class MediaAdmin(admin.ModelAdmin):
	list_display = ('name', 'kind', 'link', 'media_thumbnail')
class FigureAdmin(admin.ModelAdmin):
	list_display = ('name', 'kind')
class StoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
class CultureAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Figure, FigureAdmin)
admin.site.register(Culture, CultureAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Media, MediaAdmin)
