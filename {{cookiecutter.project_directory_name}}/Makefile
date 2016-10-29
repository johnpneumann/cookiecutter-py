.PHONY: clean-pyc clean-build clean-tests clean-log clean-docs lint checkmanifest cover docs test test-all sdist bdist build {% if cookiecutter.use_pypi == "yes" %}release{% endif %}

# allows us to spawn a new subshell for each command
# which fixes "argument list too long" errors when cleaning pyc files
define NL


endef

# Handles windowsy things
ifeq "$(OS)" "Windows_NT"
OPEN=start
else
OPEN=open
endif

# Make cp a first class make citizen
CP = cp

rwildcard = $(wildcard $1$2) $(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))
rrmdir = $(foreach dir,$1,$(RM) -r $(dir)$(NL))
rrmfile = $(foreach fname,$1,$(RM) $(fname)$(NL))

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
	@echo "clean - runs clean-build, clean-pyc, clean-tests and clean-log"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-tests - remove test files"
	@echo "clean-log - remove log files"
	@echo "clean-docs - remove generated docs"
	@echo "lint - check style with flake8"
	@echo "checkmanifest - ensure the MANIFEST.in file is up to date"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "cover - check code cover quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "sdist - package"
	@echo "bdist - create a wheel package"
	@echo "build - package for sdist and bdist_wheel"
	{% if cookiecutter.use_pypi == "yes" -%}@echo "release - package and upload a release"{% endif %}

clean: clean-build clean-tests clean-pyc clean-log clean-docs

clean-build:
	@echo "Cleaning build directories"
	$(RM) -r $(BUILDDIR)
	$(RM) -r $(DISTDIR)
	$(call rrmdir,$(call rwildcard,$(ROOT_DIRECTORY),*.egg-info))

clean-tests:
	@echo "Cleaning testing files and directories"
	$(RM) -r $(TOXDIR)
	$(RM) -r $(COVERAGEDIR)
	$(RM) $(COVERAGEFILE)
	$(RM) -r $(EGGDIR)
	$(RM) -r $(CACHEDIR)

clean-pyc:
	@echo "Cleaning pycache, pyc and pyo files"
	$(call rrmdir,$(call rwildcard,$(ROOT_DIRECTORY),__pycache__))
	$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.pyc))
	$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.pyo))
	$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*~))

clean-log:
	@echo "Cleaning log files"
	$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.log))

clean-docs:
	@echo "Cleaning generated documentation"
	$(MAKE) -C docs clean

lint:
	flake8 {{ cookiecutter.project_slug }}
	pylint {{ cookiecutter.project_slug }}

checkmanifest:
	check-manifest

test:
	env PYTHONPATH=$(ROOT_DIRECTORY):$(ROOT_DIRECTORY)tests py.test -vvv --showlocals --tb=long

test-all:
	tox

cover:
	env PYTHONPATH=$(ROOT_DIRECTORY):$(ROOT_DIRECTORY)tests py.test -vvv --cov --cov-report=term-missing --cov-report=xml --cov-report=html
	$(OPEN) coverage/html/index.html

docs: clean-docs
	$(RM) -f docs/{{ cookiecutter.project_slug }}.rst
	$(RM) -f docs/modules.rst
	$(RM) -rf docs/api
	sphinx-apidoc -f -o docs/api {{ cookiecutter.project_slug }}
	$(MAKE) -C docs html
	$(OPEN) docs/_build/html/index.html

sdist: clean checkmanifest
	python setup.py sdist
	ls -l dist

bdist: clean checkmanifest
	python setup.py bdist_wheel
	ls -l dist

build: clean checkmanifest
	python setup.py sdist bdist_wheel
	ls -l dist

{% if cookiecutter.use_pypi == "yes" -%}
release: clean checkmanifest
	python setup.py sdist upload -r $(PYPI_URL)
	python setup.py bdist_wheel upload -r $(PYPI_URL)
{% endif -%}
