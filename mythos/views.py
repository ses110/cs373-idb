from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': '#yoloswag'}
    return render_to_response('mythos/index.html', context_dict, context)