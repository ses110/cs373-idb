#mythos/api.py
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from mythos.models import *

class CultureResource(ModelResource):
	related_cultures = fields.ManyToManyField('self', 'culture', blank=False, null=True)
	related_figures = fields.ManyToManyField('mythos.api.resources.FigureResource', 'figure', blank=False, null=True)
	related_stories = fields.ManyToManyField('mythos.api.resources.StoryResource', 'story', blank=False, null=True)

	class Meta:
		queryset = Culture.objects.all()
		resource_name = 'cultures'
		authorization= Authorization()

class StoryResource(ModelResource):
	related_stories = fields.ManyToManyField('self', 'story', blank=False, null=True)
	related_cultures = fields.ManyToManyField(CultureResource, 'culture', blank=False, null=True)
	related_figures = fields.ManyToManyField('mythos.api.resources.FigureResource', 'figure', blank=False, null=True)

	class Meta:
		queryset = Story.objects.all()
		resource_name = 'stories'
		authorization= Authorization()

class FigureResource(ModelResource):
	related_figures = fields.ManyToManyField('self', 'figure', blank=False, null=True)
	related_cultures = fields.ManyToManyField(CultureResource, 'culture', blank=False, null=True)
	related_stories = fields.ManyToManyField(StoryResource, 'story', blank=False, null=True)

	class Meta:
		queryset = Figure.objects.all()
		resource_name = 'figures'
		authorization = Authorization()

class MediaResource(ModelResource):
	figure = fields.ForeignKey(FigureResource, 'figure', blank=True, null=True)
	culture = fields.ForeignKey(CultureResource, 'culture', blank=True, null=True)
	story = fields.ForeignKey(StoryResource, 'story', blank=True, null=True)

	class Meta:
		queryset = Media.objects.all()
		resource_name = 'media'
		authorization= Authorization()