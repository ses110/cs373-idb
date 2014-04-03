#mythos/api.py
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from mythos.models import *
from mythos.prettyPrint import *

class CultureResource(ModelResource):
	related_cultures = fields.ManyToManyField('self', 'related_cultures', related_name='cultures')
	related_figures = fields.ManyToManyField('mythos.api.resources.FigureResource', 'related_figures', related_name='cultures')
	related_stories = fields.ManyToManyField('mythos.api.resources.StoryResource', 'related_stories', related_name='cultures')

	class Meta:
		queryset = Culture.objects.all()
		resource_name = 'cultures'
		authorization = Authorization()
		serializer = PrettyJSONSerializer()

class StoryResource(ModelResource):
	related_stories = fields.ManyToManyField('self', 'related_stories', related_name='stories')
	related_cultures = fields.ManyToManyField(CultureResource, 'related_cultures', related_name='stories')
	related_figures = fields.ManyToManyField('mythos.api.resources.FigureResource', 'related_figures', related_name='stories')

	class Meta:
		queryset = Story.objects.all()
		resource_name = 'stories'
		authorization = Authorization()
		serializer = PrettyJSONSerializer()

class FigureResource(ModelResource):
	related_figures = fields.ManyToManyField('self', 'related_figures', related_name='figures')
	related_cultures = fields.ManyToManyField(CultureResource, 'related_cultures', related_name='figures')
	related_stories = fields.ManyToManyField(StoryResource, 'related_stories', related_name='figures')

	class Meta:
		queryset = Figure.objects.all()
		resource_name = 'figures'
		authorization = Authorization()
		serializer = PrettyJSONSerializer()

class MediaResource(ModelResource):
	figure = fields.ForeignKey(FigureResource, 'figure', blank=True, null=True)
	culture = fields.ForeignKey(CultureResource, 'culture', blank=True, null=True)
	story = fields.ForeignKey(StoryResource, 'story', blank=True, null=True)

	class Meta:
		queryset = Media.objects.all()
		resource_name = 'media'
		authorization= Authorization()
		serializer = PrettyJSONSerializer()