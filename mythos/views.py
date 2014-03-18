from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    return render_to_response('mythos/index.html', None, context)

def figure(request):
    context = RequestContext(request)

    # Do other work

    # TESTING 
    context_dict = {'title':'Test Figure'}

    return render_to_response('mythos/figure.html', context_dict, context)