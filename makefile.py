all: manage.py
	python3 manage.py startapp
clean:
    rm -f *.pyc
    rm -f Models.html

Models.html: Models.py
    epydoc IDB

test: manage.py
    python3 manage.py test
