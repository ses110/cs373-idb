# -*- coding: utf8 -*-

import wikipedia, json


page_figures = [{"title":"Atlas_(mythology)"}, {"title" : "Zeus"}, {"title": "Odin"}, {"title": "Háma"}, {"title" : "The_Dagda"}, {"title" : "The_Morrígan"}, {"title" : "Shiva"}, {"title" : "Vishnu"}, {"title" : "Osiris"}, {"title" : "Ixchel"}]
page_stories = [{"title": "Trojan_war"}, {"title": "Labours_of_Hercules"}, {"title": "Ragnarök"}, {"title": "Beltane"}, {"title": "Ashvamedha"}, {"title": "Flooding_of_the_Nile"}, {"title": "Hannibalic_War"}, {"title": "Garden_of_Eden"}, {"title": "Kamiumi"}, {"title": "Kuniumi"}]
page_cultures = [{"title": "Greek_mythos"}, {"title": "Celtic_mythology"}, {"title": "Maya_mythology"},{"title": "Norse_mythology"}, {"title": "Hindu_mythology"}, {"title": "Egyptian_mythology"}, {"title": "Slavic_mythology"}, {"title": "Roman_mythology"}, {"title": "Jewish_mythology  "}, {"title": "Japanese_mythology"}]

all_media = []
all_figures = []
all_cultures = []
all_stories = []

pk = 1

#Delete this after testing
# page_figures = page_figures[0:3]
# page_cultures = page_cultures[0:3]
# page_stories = page_stories[0:3]

for id_dict in page_figures:
    this_figure = {"pk" : pk, "model" : "mythos.figure", "fields" : {}}
    media = {}
    title = id_dict["title"]
    page = wikipedia.page(title=title)
    try:
        images = page.images
        references = page.references
    except:
        pass

    title, summary = page.title, page.summary
    this_figure["fields"]["name"] = title
    this_figure["fields"]["biography"] = summary
    all_figures.append(this_figure)

    pk = pk + 1
    for img in images:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "image", "link" : img}}
        all_media.append(media)
        pk = pk + 1

    for ref in references:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Reference", "kind" : "link", "link" : ref}}
        all_media.append(media)
        pk = pk + 1

for id_dict in page_stories:
    this_stories = {"pk" : pk, "model" : "mythos.story", "fields" : {}}
    media = {}
    title = id_dict["title"]
    page = wikipedia.page(title=title)
    try:
        images = page.images
        references = page.references
    except:
        pass
    title, summary = page.title, page.summary
    this_stories["fields"]["name"] = title
    this_stories["fields"]["summary"] = summary
    all_stories.append(this_stories)

    pk = pk + 1
    for img in images:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "image", "link" : img}}
        all_media.append(media)
        pk = pk + 1

    for ref in references:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Reference", "kind" : "link", "link" : ref}}
        all_media.append(media)
        pk = pk + 1

for id_dict in page_cultures:
    this_culture = {"pk" : pk, "model" : "mythos.culture", "fields" : {}}
    media = {}
    title = id_dict["title"]
    page = wikipedia.page(title=title)
    try:
        images = page.images
        references = page.references
    except:
        pass
    title, summary = page.title, page.summary
    this_culture["fields"]["name"] = title
    this_culture["fields"]["history"] = summary
    all_cultures.append(this_culture)

    pk = pk + 1
    for img in images:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "image", "link" : img}}
        all_media.append(media)
        pk = pk + 1

    for ref in references:
        media = {"pk" : pk, "model" : "mythos.media", "fields" : { "name" : "Reference", "kind" : "link", "link" : ref}}
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

output = open('models.json', "w")
output.write("[")
for fig in all_figures:
    output.write(json.dumps(fig) + ",")

for fig in all_cultures:
    output.write(json.dumps(fig) + ",")

for fig in all_stories:
    output.write(json.dumps(fig) + ",")

for fig in all_media:
    output.write(json.dumps(fig))
    if not fig is all_media[-1]:
        output.write(",")
output.write("]")
output.close()
