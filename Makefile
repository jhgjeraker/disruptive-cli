PYTHON?=python3
PIP?=pip3
VENV?=venv

SHELL := /bin/bash

.PHONY: build venv VENV

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: setup.py
	$(PIP) install --upgrade pip virtualenv
	@test -d $(VENV) || $(PYTHON) -m virtualenv --clear $(VENV)
	${VENV}/bin/python -m pip install -e .[dev]

build: venv
	${VENV}/bin/python -m build

test: venv
	source ${VENV}/bin/activate && pytest tests/

lint: venv
	source ${VENV}/bin/activate && mypy dtcli/ --config-file ./mypy.ini && flake8 dtcli/

clean:
	rm -rf build/ dist/ pip-wheel-metadata/ *.egg-info
	rm -rf .pytest_cache/ .mypy_cache/
	rm -rf $(VENV)
	rm -f coverage.xml
	rm -f dt.spec
