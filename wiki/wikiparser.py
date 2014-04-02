# -*- coding: utf8 -*-

import wikipedia, json


page_figures = [{"title":"Atlas_(mythology)"}, {"title" : "Zeus"}, {"title": "Odin"}, {"title": "Háma"}, {"title" : "The_Dagda"}, {"title" : "The_Morrígan"}, {"title" : "Shiva"}, {"title" : "Vishnu"}, {"title" : "Hunab_Ku"}, {"title" : "Ixchel"}]
page_stories = [{"title": "Trojan_war"}, {"title": "Trojan_war"}, {"title": "Trojan_war"}, {"title": "Trojan_war"}, {"title": "Trojan_war"}, {"title": "Trojan_war"}, {"title": "Trojan_war"}, {"title": "Trojan_war"}, {"title": "Trojan_war"}, {"title": "Trojan_war"}]
page_cultures = [{"title": "Greek_mythos"}, {"title": "Celtic_mythology"}, {"title": "Maya_mythology"},{"title": "Norse_mythology"}, {"title": "Hindu_mythology"}, {"title": "Egyptian_mythology"}, {"title": "Mesopotamian_mythology"}, {"title": "Roman_mythology"}, {"title": "Jewish_mythology  "}, {"title": "Islamic_mythology"}]

all_media = []
all_figures = []
all_cultures = []
all_stories = []

pk = 1

page_figures = page_figures[0:3]
page_cultures = page_cultures[0:3]
page_stories = page_stories[0:3]

for id_dict in page_figures:
    this_figure = {"pk" : pk, "model" : "mythos.figure", "fields" : {}}
    media = {}
    title = id_dict["title"]
    page = wikipedia.page(title=title)
    try:
        images = page.images
    except:
        pass

    title, summary, references = page.title, page.summary, page.references
    this_figure["fields"]["name"] = title
    this_figure["fields"]["biography"] = summary
    all_figures.append(this_figure)

    pk = pk + 1
    for img in images:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "Figure image", "link" : img}}
        all_media.append(media)
        pk = pk + 1

for id_dict in page_stories:
    this_stories = {"pk" : pk, "model" : "mythos.story", "fields" : {}}
    media = {}
    title = id_dict["title"]
    page = wikipedia.page(title=title)
    try:
        images = page.images
    except:
        pass
    title, summary, references = page.title, page.summary, page.references
    this_stories["fields"]["name"] = title
    this_stories["fields"]["summary"] = summary
    all_stories.append(this_stories)

    pk = pk + 1
    for img in images:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "Story image", "link" : img}}
        all_media.append(media)
        pk = pk + 1

for id_dict in page_cultures:
    this_culture = {"pk" : pk, "model" : "mythos.culture", "fields" : {}}
    media = {}
    title = id_dict["title"]
    page = wikipedia.page(title=title)
    try:
        images = page.images
    except:
        pass
    title, summary, references = page.title, page.summary, page.references
    this_culture["fields"]["name"] = title
    this_culture["fields"]["history"] = summary
    all_cultures.append(this_culture)

    pk = pk + 1
    for img in images:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "Culture image", "link" : img}}
        all_media.append(media)
        pk = pk + 1

#Kind
# all_figures[0]["fields"]["kind"] = "Titan"
# all_figures[1]["fields"]["kind"] = "Deity"
# all_figures[2]["fields"]["kind"] = "Deity"
# all_figures[3]["fields"]["kind"] = "Hero"
# all_figures[4]["fields"]["kind"] = "Deity"
# v[5]["fields"]["kind"] = "Goddess"
# all_figures[6]["fields"]["kind"] = "Deity"
# all_figures[7]["fields"]["kind"] = "Deity"
# all_figures[8]["fields"]["kind"] = "Deity"
# all_figures[9]["fields"]["kind"] = "Deity"

#related_figures
# all_figures[0]["fields"]["related_figures"] = [2]
# all_figures[0]["fields"]["related_cultures"] = []
# all_figures[0]["fields"]["related_stories"] = []

for fig in all_figures:
    print(json.dumps(fig, indent=4))

for fig in all_cultures:
    print(json.dumps(fig, indent=4))

for fig in all_stories:
    print(json.dumps(fig, indent=4))

for fig in all_media:
    print(json.dumps(fig, indent=4))
