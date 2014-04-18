from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from mythos.models import *
from json import dumps, loads
from haystack.query import SearchQuerySet
import simplejson as json
from django.core import urlresolvers
import watson
from urllib2 import *

#from django.shortcuts import get_object_or_404
#thepost = get_object_or_404(Content, name='test')

from mythos import models

def index(request):
    context = RequestContext(request)
    return render_to_response('mythos/index.html', None, context)

def search(request):
    context = RequestContext(request)
    query = ""

    if ('q' in request.GET) and request.GET['q'].strip():
        query = request.GET['q']
    
    results = watson.search(query, ranking=True)
    for r in results:
        print(r)
    return render_to_response('mythos/search.html', {"results":results}, context)

def not_found(request, val):
    context = RequestContext(request)
    return render_to_response('mythos/404.html', None, context)

def figure(request, id):
    context = RequestContext(request)
    try:
        figure = Figure.objects.get(pk=id)
        figure_dict = {
            'title': figure.name,
            'kind': figure.kind,
            'biography': figure.biography,
            'images': figure.media_set.filter(kind="image"),
            'videos': figure.media_set.filter(kind="video"),
            'related_figures': figure.related_figures.all(),
            'related_cultures': figure.related_cultures.all(),
            'related_stories': figure.related_stories.all()
        }
        return render_to_response('mythos/figure.html', figure_dict, context)
    except:
        return not_found(request)

def figures(request):
    context = RequestContext(request)

    figures = Figure.objects.all()
    context_dict = {'title':'Figures', 'items':figures}

    return render_to_response('mythos/figures.html', context_dict, context)

def culture(request, id):
    context = RequestContext(request)

    try:
        culture = Culture.objects.get(pk=id)
        culture_dict = {
            'title': culture.name,
            'region': culture.region,
            'language': culture.language,
            'history': culture.history,
            'images': culture.media_set.filter(kind="image"),
            'videos': culture.media_set.filter(kind="video"),
            'related_figures': Figure.objects.filter(related_cultures__pk=id),
            'related_cultures': culture.related_cultures.all(),
            'related_stories': Story.objects.filter(related_cultures__pk=id)
        }
        return render_to_response('mythos/culture.html', culture_dict, context)
    except:
        return not_found(request)

def cultures(request):
    context = RequestContext(request)

    cultures = Culture.objects.all()
    context_dict = {'title':'Cultures', 'items':cultures}

    return render_to_response('mythos/cultures.html', context_dict, context)


def story(request, id):
    context = RequestContext(request)

    try:
        story = Story.objects.get(pk=id)
        story_dict = {
            'title': story.name,
            'summary': story.summary,
            'images': story.media_set.filter(kind="image"),
            'videos': story.media_set.filter(kind="video"),
            'related_figures': Figure.objects.filter(related_stories__pk=id),
            'related_cultures': story.related_cultures.all(),
            'related_stories': story.related_stories.all()
        }
        return render_to_response('mythos/story.html', story_dict, context)
    except:
        return not_found(request)

def stories(request):
    context = RequestContext(request)

    stories = Story.objects.all()
    context_dict = {'title':'Stories', 'items':stories}

    return render_to_response('mythos/stories.html', context_dict, context)

def queries(request):
    return render_to_response('mythos/queries.html')

def pictures(request):
    url = "http://127.0.0.1:8000"
    context = RequestContext(request)
    req = Request(url+"/api/media/?format=json")
    response = urlopen(req)
    response_body = response.read().decode("utf-8")
    response_data = loads(response_body)
    response_objects = response_data["objects"]
    l = []
    for media in response_objects:
        if media['kind'] == 'image':
            l.append(media['link'])
    """while response_data["meta"]["next"] != None :
        req = Request(url+response_data["meta"]["next"])
        response = urlopen(req)
        response_body = response.read().decode("utf-8")
        response_data = loads(response_body)
        response_objects = response_data["objects"]
        for media in response_objects:
            if media['kind'] == 'image':
                l.append(media['link'])"""


    return render_to_response('mythos/pictures.html', {"l":l}, context)