.PHONY: clean clean-build clean-pyc clean-tests clean-log clean-docs api-docs docs lint checkmanifest test test-all cover sdist bdist build {% if cookiecutter.use_pypi == "yes" %}release{% endif %}

# Aliased calls for finding files and directories recursively
rwildcard = $(wildcard $1$2) $(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))
rrmdir = $(foreach dir,$1,$(RM) -r $(dir))
rrmfile = $(foreach fname,$1,$(RM) $(fname))

# Set base variables
ROOT_DIRECTORY = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
BUILDDIR = build
DISTDIR = dist
TOXDIR = .tox
COVERAGEDIR = coverage
COVERAGEFILE = .coverage
EGGDIR = .eggs
CACHEDIR = .cache
{% if cookiecutter.use_pypi == "yes" -%}PYPI_URL = {{ cookiecutter.pypi_url }}{% endif %}

help:
	@echo "Management commands for {{ cookiecutter.project_name }}"
	@echo
	@echo "Usage:"
	@echo "\tmake clean:          runs clean-build, clean-pyc, clean-tests and clean-log"
	@echo "\tmake clean-build:    remove build artifacts"
	@echo "\tmake clean-pyc:      remove Python file artifacts"
	@echo "\tmake clean-tests:    remove test files"
	@echo "\tmake clean-log:      remove log files"
	@echo "\tmake clean-docs:     remove generated docs"
	@echo "\tmake api-docs:       generate the api documentation files"
	@echo "\tmake docs:           generate Sphinx HTML documentation, including API docs"
	@echo "\tmake lint:           check style with flake8"
	@echo "\tmake checkmanifest:  ensure the MANIFEST.in file is up to date"
	@echo "\tmake test:           run tests quickly with the default Python"
	@echo "\tmake test-all:       run tests on every Python version with tox"
	@echo "\tmake cover:          check code coverage quickly with the default Python"
	@echo "\tmake sdist:          build an sdist package"
	@echo "\tmake bdist:          build a bdist_wheel package"
	@echo "\tmake build:          build the sdist and bdist_wheel packages"
	{% if cookiecutter.use_pypi == "yes" -%}@echo "\tmake release:        package and upload a release"{% endif %}
	@echo

clean: clean-build clean-tests clean-pyc clean-log clean-docs

clean-build:
	$(RM) -r $(BUILDDIR)
	$(RM) -r $(DISTDIR)
	$(call rrmdir,$(call rwildcard,$(ROOT_DIRECTORY),*.egg-info))

clean-tests:
	$(RM) -r $(TOXDIR)
	$(RM) -r $(COVERAGEDIR)
	$(RM) $(COVERAGEFILE)
	$(RM) -r $(EGGDIR)
	$(RM) -r $(CACHEDIR)

clean-pyc:
	$(call rrmdir,$(call rwildcard,$(ROOT_DIRECTORY),__pycache__))
	$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.pyc))
	$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.pyo))
	$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*~))

clean-log:
	$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.log))

clean-docs:
	$(MAKE) -C docs clean
	$(RM) -r docs/api

api-docs: clean-docs
	sphinx-apidoc -e -f -o docs/api {{ cookiecutter.project_slug }}

docs: api-docs
	$(MAKE) -C docs html

lint:
	flake8 {{ cookiecutter.project_slug }}
	pylint {{ cookiecutter.project_slug }}

checkmanifest:
	check-manifest

test:
	env PYTHONPATH=$(ROOT_DIRECTORY):$(ROOT_DIRECTORY)/tests py.test -vvv --showlocals --tb=long

test-all:
	tox

cover:
	env PYTHONPATH=$(ROOT_DIRECTORY):$(ROOT_DIRECTORY)/tests py.test -vvv --cov --cov-report=term-missing --cov-report=xml --cov-report=html

sdist: clean api-docs checkmanifest
	python setup.py sdist
	ls -l dist

bdist: clean api-docs checkmanifest
	python setup.py bdist_wheel
	ls -l dist

build: clean api-docs checkmanifest
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

{% if cookiecutter.use_pypi == "yes" -%}
release: clean api-docs checkmanifest
	python setup.py sdist upload -r $(PYPI_URL)
	python setup.py bdist_wheel upload -r $(PYPI_URL)
{% endif -%}
