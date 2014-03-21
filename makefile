all: manage.py
	python3 manage.py startapp
clean:
	rm -f *.pyc
	rm -f Models.html

Models.html: mythos/models.py
	epydoc mythos/models.py

test: manage.py
	python3 manage.py test
