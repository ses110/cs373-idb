# -*- coding: utf8 -*-

import wikipedia, json

list_figures = ["Athena", 
                "Zeus" , 
                "Odin", 
                "Háma", "The_Dagda",
                "The_Dagda",
                "The_Morrígan",
                "Shiva",
                "Vishnu",
                "Osiris",
                "Ixchel"]
list_stories =["Trojan_war",
               "Labours_of_Hercules",
               "Ragnarök",
               "Beltane",
               "Ashvamedha",
               "Flooding_of_the_Nile",
               "Hannibalic_War",
               "Garden_of_Eden",
               "Kamiumi",
               "Kuniumi"]
list_cultures = ["Greek_mythos",
                 "Celtic_mythology",
                 "Maya_mythology",
                 "Norse_mythology",
                 "Hindu_mythology",
                 "Egyptian_mythology", 
                 "Slavic_mythology", 
                 "Roman_mythology", 
                 "Jewish_mythology", 
                 "Japanese_mythology"]

all_media = []
all_figures = []
all_cultures = []
all_stories = []

pk = 1
m_pk = 1

media_limit = 5

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

    title, summary = page.title.replace("_", " "), page.summary
    this_figure["fields"]["name"] = title
    this_figure["fields"]["biography"] = summary
    all_figures.append(this_figure)

    for i in range(min(media_limit, len(images))):
        img = images[i]
        if len(img) < 200:
            media = {"pk" : m_pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "image", "link" : img, "figure" : pk}}
            all_media.append(media)
            m_pk += 1

    for i in range(min(media_limit, len(references))):
        ref = references[i]
        if len(ref) < 200:
            media = {"pk" : m_pk, "model" : "mythos.media", "fields" : { "name" : "Reference", "kind" : "link", "link" : ref, "figure" : pk}}
            all_media.append(media)
            m_pk += 1

    pk += 1

pk = 1
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
    title, summary = page.title.replace("_", " "), page.summary
    this_stories["fields"]["name"] = title
    this_stories["fields"]["summary"] = summary
    all_stories.append(this_stories)

    for i in range(min(media_limit, len(images))):
        img = images[i]
        if len(img) < 200:
            media = {"pk" : m_pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "image", "link" : img, "story" : pk}}
            all_media.append(media)
            m_pk += 1

    for i in range(min(media_limit, len(references))):
        ref = references[i]
        if len(ref) < 200:
            media = {"pk" : m_pk, "model" : "mythos.media", "fields" : { "name" : "Reference", "kind" : "link", "link" : ref, "story" : pk}}
            all_media.append(media)
            m_pk += 1
    pk += 1


pk = 1
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
    title, summary = page.title.replace("_", " "), page.summary
    this_culture["fields"]["name"] = title
    this_culture["fields"]["history"] = summary
    all_cultures.append(this_culture)

    

    for i in range(min(media_limit, len(images))):
        img = images[i]
        if len(img) < 200:
            media = {"pk" : m_pk, "model" : "mythos.media", "fields" : { "name" : "Image of " + title, "kind" : "image", "link" : img, "culture" : pk}}
            all_media.append(media)
            m_pk += 1

    for i in range(min(media_limit, len(references))):
        ref = references[i]
        if len(ref) < 200:
            media = {"pk" : m_pk, "model" : "mythos.media", "fields" : { "name" : "Reference", "kind" : "link", "link" : ref, "culture" : pk}}
            all_media.append(media)
            m_pk += 1
    pk += 1

#Kind
all_figures[0]["fields"]["kind"] = "Olympian"
all_figures[1]["fields"]["kind"] = "Olympian"
all_figures[2]["fields"]["kind"] = "God"
all_figures[3]["fields"]["kind"] = "Hero"
all_figures[4]["fields"]["kind"] = "God"
all_figures[6]["fields"]["kind"] = "Goddess"
all_figures[7]["fields"]["kind"] = "Goddess"
all_figures[8]["fields"]["kind"] = "God"
all_figures[9]["fields"]["kind"] = "Goddess"

#Region
all_cultures[0]["fields"]["region"] = "Greece"
all_cultures[1]["fields"]["region"] = "Ireland"
all_cultures[2]["fields"]["region"] = "Mesoamerica"
all_cultures[3]["fields"]["region"] = "Scandinavia"
all_cultures[4]["fields"]["region"] = "India"
all_cultures[5]["fields"]["region"] = "Egypt"
all_cultures[6]["fields"]["region"] = "Eastern Europe"
all_cultures[7]["fields"]["region"] = "Italy"
all_cultures[8]["fields"]["region"] = "Israel"
all_cultures[9]["fields"]["region"] = "Japan"

all_cultures[0]["fields"]["language"] = "Greek"
all_cultures[1]["fields"]["language"] = "Gaelic"
all_cultures[2]["fields"]["language"] = "Mayan"
all_cultures[3]["fields"]["language"] = "Nordic"
all_cultures[4]["fields"]["language"] = "Hindi"
all_cultures[5]["fields"]["language"] = "Egyptian"
all_cultures[6]["fields"]["language"] = "Slavic"
all_cultures[7]["fields"]["language"] = "Latin"
all_cultures[8]["fields"]["language"] = "Hebrew"
all_cultures[9]["fields"]["language"] = "Japanese"

#related_fields
#Athena
all_figures[0]["fields"]["related_figures"] = [2]
all_figures[0]["fields"]["related_cultures"] = [1,8]
all_figures[0]["fields"]["related_stories"] = [1]
#Zeus
all_figures[1]["fields"]["related_figures"] = [1]
all_figures[1]["fields"]["related_cultures"] = [1,8]
all_figures[1]["fields"]["related_stories"] = [1,2]
#Odin
all_figures[2]["fields"]["related_figures"] = [4]
all_figures[2]["fields"]["related_cultures"] = [4]
all_figures[2]["fields"]["related_stories"] = [3]
#Hama
all_figures[3]["fields"]["related_figures"] = [3]
all_figures[3]["fields"]["related_cultures"] = [4]
all_figures[3]["fields"]["related_stories"] = [3]
#The Dagda
all_figures[4]["fields"]["related_figures"] = [6]
all_figures[4]["fields"]["related_cultures"] = [2]
all_figures[4]["fields"]["related_stories"] = [4]
#The Morrigan
all_figures[5]["fields"]["related_figures"] = [5]
all_figures[5]["fields"]["related_cultures"] = [2]
all_figures[5]["fields"]["related_stories"] = [4]
#Shiva
all_figures[6]["fields"]["related_figures"] = [8]
all_figures[6]["fields"]["related_cultures"] = [5]
all_figures[6]["fields"]["related_stories"] = [5]
#Vishnu
all_figures[7]["fields"]["related_figures"] = [7]
all_figures[7]["fields"]["related_cultures"] = [5]
all_figures[7]["fields"]["related_stories"] = [5]
#Osiris
all_figures[8]["fields"]["related_figures"] = []
all_figures[8]["fields"]["related_cultures"] = [6]
all_figures[8]["fields"]["related_stories"] = [6]
#Ixchel
all_figures[9]["fields"]["related_figures"] = [2]
all_figures[9]["fields"]["related_cultures"] = [3]
all_figures[9]["fields"]["related_stories"] = []

#Greek mythology
all_cultures[0]["fields"]["related_cultures"] = [8]
#Celtic Mythology
all_cultures[1]["fields"]["related_cultures"] = []
#Mayan Mythology
all_cultures[2]["fields"]["related_cultures"] = []
#Norse Mythology
all_cultures[3]["fields"]["related_cultures"] = []
#Hindu Mythology
all_cultures[4]["fields"]["related_cultures"] = []
#Egyptian mythology
all_cultures[5]["fields"]["related_cultures"] = []
#Slavic Mythology
all_cultures[6]["fields"]["related_cultures"] = []
#Roman Mythology
all_cultures[7]["fields"]["related_cultures"] = [1]
#Jewish Mythology
all_cultures[8]["fields"]["related_cultures"] = []
#Japanese Mythology
all_cultures[9]["fields"]["related_cultures"] = []


#Trojan War
all_stories[0]["fields"]["related_cultures"] = [1]
all_stories[0]["fields"]["related_stories"] = [2]
#Labours of Hercules
all_stories[1]["fields"]["related_cultures"] = [1]
all_stories[1]["fields"]["related_stories"] = [1]
#Ragnarok
all_stories[2]["fields"]["related_cultures"] = [4]
all_stories[2]["fields"]["related_stories"] = []
#Beltane
all_stories[3]["fields"]["related_cultures"] = [2]
all_stories[3]["fields"]["related_stories"] = []
#Ashvamedha
all_stories[4]["fields"]["related_cultures"] = [5]
all_stories[4]["fields"]["related_stories"] = []
#Flooding of the Nile
all_stories[5]["fields"]["related_cultures"] = [6]
all_stories[5]["fields"]["related_stories"] = []
#Hannibalic War
all_stories[6]["fields"]["related_cultures"] = [8]
all_stories[6]["fields"]["related_stories"] = []
#Garden of Eden
all_stories[7]["fields"]["related_cultures"] = [9]
all_stories[7]["fields"]["related_stories"] = []
#Kamiumi
all_stories[8]["fields"]["related_cultures"] = [10]
all_stories[8]["fields"]["related_stories"] = [10]
#Kuniuni
all_stories[9]["fields"]["related_cultures"] = [10]
all_stories[9]["fields"]["related_stories"] = [9]


# for fig in all_figures:
#     print(json.dumps(fig, indent=4))

# for fig in all_cultures:
#     print(json.dumps(fig, indent=4))

# for fig in all_stories:
#     print(json.dumps(fig, indent=4))

# for fig in all_media:
#     print(json.dumps(fig, indent=4))

output = open('../fixtures/models.json', "w")
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
