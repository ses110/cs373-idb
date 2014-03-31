import wikipedia


page_ids = [{"title":"Roman_Empire"}]
put_url_for_catgories = {
    "culture":"",
    "figure":"",
    "story":""
}


for id_dict in page_ids:
    title = id_dict["title"]
    # category = id_dict["category"]
    page = wikipedia.page(title=title)
    summary, images, references = page.summary, page.references, page.images
    print(title)
    print()
    print(summary)
    print()
    print(images)
    print(references)

