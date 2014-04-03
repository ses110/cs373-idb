from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from mythos.models import *
from json import dumps, loads

#from django.shortcuts import get_object_or_404
#thepost = get_object_or_404(Content, name='test')

from mythos import models

def index(request):
    context = RequestContext(request)
    return render_to_response('mythos/index.html', None, context)

def figure(request, id):
    context = RequestContext(request)
    try:
        figure = Figure.objects.get(pk=id)
        return render_to_response('mythos/figure.html', dict_from_figure(figure), context)
    except:
        return render_to_response('mythos/404.html', None, context)

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
# Helper Methods
# -----

def dict_from_figure(figure):
    return {
        'title': figure.name,
        'kind': figure.kind,
        'biography': figure.biography,
        'images': figure.media_set.filter(kind="image"),
        'videos': figure.media_set.filter(kind="video"),
        'related_figures': figure.related_figures.all(),
        'related_cultures': figure.related_cultures.all(),
        'related_stories': figure.related_stories.all()
    }


# -----
# API Methods
# -----
# Sample return
# return HttpResponse("{'test':%d}" % (int(id),), content_type="application/json")

def api_figure(request, id):
   return HttpResponse("{'test':%d}" % (int(id),), content_type="application/json", status=200)

def api_figures(request):
    if request.method == 'GET' :
        models = Figure.objects.all()
        li = []
        for model in models :
            di = {  "id" : model.id,
                    "name" : model.name,
                    "kind" : model.kind,
                    "biography" : model.biography}
            li.append(di)
        return HttpResponse(dumps(li, ensure_ascii=True), content_type="application/json", status=200)
    elif request.method == 'POST' :
        request_body = request.read().decode("utf-8")
        data = loads(request_body)
        #build Figure
        fig = Figure(name = data["name"], kind = data["kind"], 
            biography = data["biography"])
        #build Media
        for image in data["images"] :
            try:
                med = Media.objects.get(link=image)
                med.figure = fig
            except ObjectDoesNotExist:
                med = Media(link = image, kind = "image", figure = fig)
            med.save()
        for video in data["videos"] :
            try:
                med = Media.objects.get(link=video)
                med.figure = fig
            except ObjectDoesNotExist:
                med = Media(link = video, kind = "video", figure = fig)
            med.save()
        for ex_link in data["external_links"] :
            try:
                med = Media.objects.get(link=ex_link["link"])
                med.figure = fig
            except ObjectDoesNotExist:
                med = Media(name = ex_link["name"], link = ex_link["link"], kind = "link", figure = fig)
            med.save()
        #build related_figures
        for rel_fig_data in data["related_figures"] :
            try:
                rel_fig = Figures.objects.get(pk=rel_fig_data["id"])
                rel_fig.related_figures.add(fig)
                fig.related_figures.add(rel_fig)
                rel_fig.save()
            except ObjectDoesNotExist:
                pass

        #build related_stories
        for rel_story_data in data["related_stories"] :
            try:
                rel_story = Figures.objects.get(pk=rel_story_data["id"])
                rel_story.related_figures.add(fig)
                fig.related_stories.add(rel_story)
                rel_story.save()
            except ObjectDoesNotExist:
                pass

        #build related_cultures
        for rel_cult_data in data["related_cultures"] :
            try:
                rel_cult = Figures.objects.get(pk=rel_fig_data["id"])
                rel_cult.related_figures.add(fig)
                fig.related_cultures.add(rel_cult)
                rel_cult.save()
            except ObjectDoesNotExist:
                pass

        fig.save()

        return HttpResponse("{'id':%d}" % (fig.pk,), content_type="application/json", status=201)

    elif request.method == 'PUT' :

        return HttpResponse("{'id':%d}" % (1,), content_type="application/json", status=200)
    else :
        return HttpResponse("", content_type="application/json", status=405)

    

def api_culture(request, id):
    pass

def api_cultures(request):
    pass

def api_story(request, id):
    pass

def api_stories(request):
    pass

