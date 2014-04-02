from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from json import dumps, loads

#from django.shortcuts import get_object_or_404
#thepost = get_object_or_404(Content, name='test')

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
# Sample return
# return HttpResponse("{'test':%d}" % (int(id),), content_type="application/json")

def api_figure(request, id):
   return HttpResponse("{'test':%d}" % (int(id),), content_type="application/json", status=200)

def api_figures(request):
    if request.method == 'GET' :
        models = Figures.objects().all()
        li = []
        for model in models :
            di = {  "id" : model.id,
                    "title" : model.title,
                    "kind" : model.kind,
                    "biography" : model.biography}
            li.append(di)

        return HttpResponse(li, content_type="application/json", status=200)
    elif request.method == 'POST' :
        request_body = request.read().decode("utf-8")
        data = loads(request_body)
        #build Figure
        fig = Figure(title = data["title"], kind = data["kind"], 
            biography = data["biography"])
        #build Media
        for image in data["images"] :
            try:
                med = Media.objects.get(link=image)
                med.figure = fig
            except ObjectDoesNotExist:
                med = Media(link = image, figure = fig)
            med.save()
        for video in data["videos"] :
            try:
                med = Media.objects.get(link=video)
                med.figure = fig
            except ObjectDoesNotExist:
                med = Media(link = video, figure = fig)
            med.save()
        for ex_link in data["external_links"] :
            try:
                med = Media.objects.get(link=ex_link["link"])
                med.figure = fig
            except ObjectDoesNotExist:
                med = Media(name = ex_link["name"], link = ex_link["link"], figure = fig)
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

