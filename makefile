all: manage.py
	python manage.py startapp
clean:
	rm -f *.pyc
	rm -f Models.html

Models.html: mythos/models.py
	epydoc mythos/models.py

test: manage.py
	python manage.py test

runserver: manage.py
	python manage.py runserver

run_elastic:
	./elasticsearch-1.1.1/bin/elasticsearch &
