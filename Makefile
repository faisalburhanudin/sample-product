# useful targets:
#   make run ------------------ run flask
#   make test ----------------- run the tests

FLASK_APP = wsgi
FLASK_ENV = development

.PHONY: run
run:
	flask run

.PHONY: test
test:
	py.test