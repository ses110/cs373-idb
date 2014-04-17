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
        url(r'^cultures/(\d+)/$', views.culture, name='culture'),
        url(r'^cultures/$', views.cultures, name='cultures'),
        url(r'^stories/$', views.stories, name='stories'),
        url(r'^stories/(\d+)/$', views.story, name='story'),
        url(r'^api/', include(figure_resource.urls)),
        url(r'^api/', include(story_resource.urls)),
        url(r'^api/', include(culture_resource.urls)),
        url(r'^search/', include('haystack.urls')),
        url(r'^search/autocomplete/$', views.autocomplete, name='autocomplete'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^(\w+)/$', views.not_found, name='not_found')
)