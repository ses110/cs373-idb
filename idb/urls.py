from django.conf.urls import patterns, include, url
from django.contrib import admin
from mythos import views


admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^figures/?$', views.figures, name='figures'),
        url(r'^figures/(.+)$', views.figure, name='figure')
)
