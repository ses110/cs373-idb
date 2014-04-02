from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from mythos import models

def index(request):
    context = RequestContext(request)
    return render_to_response('mythos/index.html', None, context)


def figure(request, id):
    context = RequestContext(request)
    return render_to_response('mythos/figure.html', models.p1_figure(id), context)


def figures(request):
    context = RequestContext(request)

    # Get list of all figures

    figures = models.p1_figures()
    context_dict = {'title':'Figures', 'items':figures}

    return render_to_response('mythos/figures.html', context_dict, context)


def culture(request, id):
    context = RequestContext(request)
    return render_to_response('mythos/culture.html', models.p1_culture(id), context)

def cultures(request):
    context = RequestContext(request)

    cultures = models.p1_cultures()
    context_dict = {'title':'Cultures', 'items':cultures}

    return render_to_response('mythos/cultures.html', context_dict, context)


def story(request, id):
    context = RequestContext(request)
    return render_to_response('mythos/story.html', models.p1_story(id), context)

def stories(request):
    context = RequestContext(request)

    stories = models.p1_stories()
    context_dict = {'title':'Stories', 'items':stories}

    return render_to_response('mythos/stories.html', context_dict, context)


# -----
# API Methods
# -----

def api_figure(request, id):
    return HttpResponse("{'test':%d}" % (int(id),), content_type="application/json")

def api_figures(request):
    pass

def api_culture(request, id):
    pass

def api_cultures(request):
    pass

def api_story(request, id):
    pass

def api_stories(request):
    pass

