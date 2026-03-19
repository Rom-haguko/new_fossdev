create-structure:
	mkdir src test docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep test/.gitkeep


install-dep:
	pip install -r requirements.txt

install:
	pip install -e .


test-pytest:
	python3 -m pytest

test: install-dep install test-pytest