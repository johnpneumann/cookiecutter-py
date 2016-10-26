.PHONY: clean-pyc clean-build clean-tests clean-log lint checkmanifest docs test

# allows us to spawn a new subshell for each command
# which fixes "argument list too long" errors when cleaning pyc files
define NL


endef

rwildcard = $(wildcard $1$2) $(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))
rrmdir = $(foreach dir,$1,$(RM) -r $(dir)$(NL))
rrmfile = $(foreach fname,$1,$(RM) $(fname)$(NL))

pypi_url = {{ cookiecutter.pypi_url }}

ifeq "$(OS)" "Windows_NT"
	OPEN=start
else
	OPEN=open
endif

ROOT_DIRECTORY = .
BUILDDIR = build
DISTDIR = dist
TOXDIR = .tox
COVERAGEDIR = coverage
COVERAGEFILE = .coverage
EGGDIR = .eggs
CACHEDIR = .cache

help:
	@echo "clean - runs clean-build, clean-pyc, clean-tests and clean-log"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-tests - remove test files"
	@echo "clean-log - remove log files"
	@echo "lint - check style with flake8"
	@echo "checkmanifest - ensure the MANIFEST.in file is up to date"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean: clean-build clean-tests clean-pyc clean-log

clean-build:
	@echo "Cleaning build directories"
	@$(RM) -r $(BUILDDIR)
	@$(RM) -r $(DISTDIR)
	@$(call rrmdir,$(call rwildcard,$(ROOT_DIRECTORY),*.egg-info))

clean-tests:
	@echo "Cleaning testing files and directories"
	@$(RM) -r $(TOXDIR)
	@$(RM) -r $(COVERAGEDIR)
	@$(RM) $(COVERAGEFILE)
	@$(RM) -r $(EGGDIR)
	@$(RM) -r $(CACHEDIR)

clean-pyc:
	@echo "Cleaning pycache, pyc and pyo files"
	@$(call rrmdir,$(call rwildcard,$(ROOT_DIRECTORY),__pycache__))
	@$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.pyc))
	@$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.pyo))
	@$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*~))

clean-log:
	@echo "Cleaning log files"
	@$(call rrmfile,$(call rwildcard,$(ROOT_DIRECTORY),*.log))

lint:
	flake8 {{ cookiecutter.project_slug }}
	pylint {{ cookiecutter.project_slug }}

checkmanifest:
	check-manifest

test:
	env PYTHONPATH=$(pwd):$(pwd)/tests py.test -vvv --showlocals --tb=long

test-all:
	tox

coverage:
	env PYTHONPATH=$(pwd):$(pwd)/tests py.test -vvv --cov --cov-report=term-missing --cov-report=xml --cov-report=html
	$(OPEN) coverage/html/index.html

docs:
	$(RM) -f docs/{{ cookiecutter.project_slug }}.rst
	$(RM) -f docs/modules.rst
	$(RM) -rf docs/api
	sphinx-apidoc -f -o docs/api {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(OPEN) docs/_build/html/index.html

release: clean checkmanifest
	python setup.py sdist upload -r $(pypi_url)
	python setup.py bdist_wheel upload -r $(pypi_url)

sdist: clean checkmanifest
	python setup.py sdist
	ls -l dist
