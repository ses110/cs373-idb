from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from mythos import models














def index(request):
    context = RequestContext(request)
    return render_to_response('mythos/index.html', None, context)


def figure(request, val):
    context = RequestContext(request)

    # Retrieve correct figure

    # TESTING 
    context_dict = {'title':'Test Figure'}

    return render_to_response('mythos/figure.html', context_dict, context)


def figures(request):
    context = RequestContext(request)

    # Get list of all figures

    # TESTING
    context_dict = {'title':'Figures'}

    return render_to_response('mythos/figures.html', context_dict, context)


def culture(request, val):
    context = RequestContext(request)

    # Retrieve correct figure

    # TESTING 
    context_dict = {'title':'Test Culture'}

    return render_to_response('mythos/culture.html', context_dict, context)

def cultures(request):
    context = RequestContext(request)

    # Get list of all figures

    cultures = [
        models.Culture(name='Greeks'),
        models.Culture(name='Romans'),
        models.Culture(name='Chinese'),
        models.Culture(name='Persian'),
        models.Culture(name='Norse')
    ]

    # TESTING
    context_dict = {'title':'Cultures', 'items':cultures}

    return render_to_response('mythos/cultures.html', context_dict, context)


def story(request, val):
    context = RequestContext(request)

    # Retrieve correct figure

    # TESTING 
    context_dict = {'title':'Test Story'}

    return render_to_response('mythos/story.html', context_dict, context)

def stories(request):
    context = RequestContext(request)

    # Get list of all figures

    # TESTING
    context_dict = {'title':'Stories'}

    return render_to_response('mythos/stories.html', context_dict, context)
