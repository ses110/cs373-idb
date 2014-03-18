from django.conf.urls import patterns, include, url
from django.contrib import admin
from mythos import views


admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^figures/$', views.figures, name='figures'),
        url(r'^figures/(\w+)/$', views.figure, name='figure'),
        url(r'^cultures/$', views.cultures, name='cultures'),
        url(r'^cultures/(\w+)/$', views.culture, name='culture'),
        url(r'^stories/$', views.stories, name='stories'),
        url(r'^stories/(\w+)/$', views.story, name='story')
)
