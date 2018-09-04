.PHONY: release
release:
	python3 setup.py bdist_wheel upload

.PHONY: test
test: | pytest lint

.PHONY: pytest
pytest:
	. venv/bin/activate && python3 -m pytest

.PHONY: lint
lint:
	. venv/bin/activate && flake8 jsonlogic-transpiler tests

.PHONY: clean
clean:
	rm -rf dist *.egg-info build dist .pytest_cache

.PHONY: venv
venv:
	pip3 install virtualenv
	virtualenv venv
	. venv/bin/activate && \
	pip3 install -r requirements.txt && \
	pip3 install -r test_requirements.txt
