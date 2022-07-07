#makefile
SHELL := /bin/bash

run:
	python app/main.py ;\

lint:
	flake8 app/ --exit-zero ;\

install:
	pip install -r requirements.txt ;\

test:
	cd app && coverage run -m pytest && coverage report -m && coverage html && coverage erase ;\
