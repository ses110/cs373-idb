from django.conf.urls import patterns, include, url
from django.contrib import admin
from mythos import views


admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^figures/$', views.figures, name='figures'),
        url(r'^figures/(\d+)/$', views.figure, name='figure'),
        url(r'^cultures/$', views.cultures, name='cultures'),
        url(r'^cultures/(\d+)/$', views.culture, name='culture'),
        url(r'^stories/$', views.stories, name='stories'),
        url(r'^stories/(\d+)/$', views.story, name='story')
)
