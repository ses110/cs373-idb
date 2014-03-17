from django.conf.urls import patterns, url
from mythos import views

urlpatterns = patterns('',
        url(r'^mythos/', include('mythos.urls')))