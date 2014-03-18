from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    return render_to_response('mythos/index.html', None, context)


def figures(request):
    context = RequestContext(request)

    # Get list of all figures

    # TESTING
    context_dict = {'title':'Figures'}

    return render_to_response('mythos/figures.html', context_dict, context)


def figure(request):
    context = RequestContext(request)

    # Retrieve correct figure

    # TESTING 
    context_dict = {'title':'Test Figure'}

    return render_to_response('mythos/figure.html', context_dict, context)