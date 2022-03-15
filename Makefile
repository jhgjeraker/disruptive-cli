PYTHON?=python3
PIP?=pip3
VENV?=venv

SHELL := /bin/bash

.PHONY: build venv VENV

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	$(PIP) install --upgrade pip virtualenv
	@test -d $(VENV) || $(PYTHON) -m virtualenv --clear $(VENV)
	${VENV}/bin/python -m pip install --upgrade pip
	${VENV}/bin/python -m pip install -r requirements.txt

build: venv
	${VENV}/bin/pyinstaller --name dt --noconfirm main.py

clean:
	rm -rf build/ dist/ pip-wheel-metadata/ *.egg-info
	find . -name '__pycache__' -exec rm --force --recursive {} +
	rm -rf .pytest_cache/ .mypy_cache/
	rm -rf $(VENV)
	rm -f coverage.xml
	rm -f dt.spec
