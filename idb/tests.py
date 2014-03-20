from django.test import TestCase
from urllib.request import urlopen, request
from json import dumps, loads


# Create your tests here.



class APItests(TestCase) :

	def test_get_all_figures(self) :


		request = Request("http://cs373idb.apiary-mock.com/api/figures")
		response_body = urlopen(request).read()
		self.assertEqual(response_body.getcode(), 200)
		response = loads(response_body)
		expected_response = [{
		    "id": 1,
		    "title":"Atlas",
		    "kind":"Titan",
		    "biography":"Long text description here."
		}, {
		    "id": 2,
		    "title":"Athena",
		    "kind":"Olympian",
		    "biography":"Long text description here."
		}, {
		    "id": 3,
		    "title":"Loki",
		    "kind":"God",
		    "biography":"Long text description here."
		}]

		self.assertTrue(expected_response == response)

	def test_post_figure(self) :

		values = dumps({
            "title":"Loki",
            "kind":"God",
            "biography":"Long text description here.",
            "images":[{link:"http://upload.wikimedia.org/wikipedia/commons/4/40/Processed_SAM_loki.jpg"},
                      {link:"http://upload.wikimedia.org/wikipedia/commons/a/ac/Loki_taunts_Bragi.jpg"},
                      {link:"http://upload.wikimedia.org/wikipedia/commons/c/cb/Louis_Huard_-_The_Punishment_of_Loki.jpg"}],
            "videos":[{link:"http://www.youtube.com/embed/o43-oAL2ogY"}],
            "related_figures":[],
            "related_stories":[],
            "related_cultures":[{id:3, name:"Nordic"}],
            "external_links":[{name:"Wikipedia: Loki", link:"http://en.wikipedia.org/wiki/Loki"},
                              {name:"Pantheon.Org", link:"http://www.pantheon.org/articles/l/loki.html"}]
        })
		headers = {"Content-Type": "application/json"}
		request = Request("http://cs373idb.apiary-mock.com/api/figures", data=values, headers=headers)
		response_body = urlopen(request).read()
		self.assertEqual(response_body.getcode(), 200)
		response = loads(response_body)
		expected_response = {
		    "id": 3
		}

		self.assertTrue(expected_response == response)






print("Done.")