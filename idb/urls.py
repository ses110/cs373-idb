from django.conf.urls import patterns, include, url
from django.contrib import admin
from mythos import views
from mythos.api import *

admin.autodiscover()

figure_resource = FigureResource()
story_resource = StoryResource()
culture_resource = CultureResource()

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^figures/$', views.figures, name='figures'),
        url(r'^figures/(\d+)/$', views.figure, name='figure'),
        url(r'^cultures/$', views.cultures, name='cultures'),
        url(r'^cultures/(\d+)/$', views.culture, name='culture'),
        url(r'^stories/$', views.stories, name='stories'),
        url(r'^stories/(\d+)/$', views.story, name='story'),
        url(r'^api/', include(figure_resource.urls)),
        url(r'^api/', include(story_resource.urls)),
        url(r'^api/', include(culture_resource.urls)),
        #url(r'^api/figures/$', views.api_figures, name='api_figures'),
        #url(r'^api/figures/(\d+)/$', views.api_figure, name='api_figure'),
        #url(r'^api/cultures/$', views.api_cultures, name='api_cultures'),
        #url(r'^api/cultures/(\d+)/$', views.api_culture, name='api_culture'),
        #url(r'^api/stories/$', views.api_stories, name='api_stories'),
        #url(r'^api/stories/(\d+)/$', views.api_story, name='api_story')
)
