.POSIX:
.SUFFIXES:

.PHONY: default
default: build

.PHONY: build
build:
	rm -fr build/
	python3 -m pip install -r requirements.txt --target build
	rm -fr build/*.dist-info/
	cp app.py build/__main__.py
	python3 -m zipapp -c -p "/usr/bin/env python3" -o coffee build

.PHONY: dist
dist: build
	rm -fr dist/
	mkdir dist/
	cp coffee dist/
	cp -r static dist/
	cp -r templates dist/

.PHONY: run
run: build
	./coffee

.PHONY: clean
clean:
	rm -fr coffee build/ dist/
