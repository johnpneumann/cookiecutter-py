===============
cookiecutter py
===============

An opinionated cookiecutter template for python projects.

Install
=======

To install the package you need to install the cookiecutter_ package using::

   pip install cookiecutter

From there you can run::

   cookiecutter <path/to/this/directory>

or::

   cookiecutter https://github.com/johnpneumann/cookiecutter-py

Do not run the above command within this directory as it will create the project
inside of here. Run the command from whereever it is that you want to have the project
be created (eg. $HOME/github/<username>).

You'll be stepped through the setup process and have a new project created
for you. For more information on the cookiecutter_ package, see the aforementioned
packages documentation

What's Included
===============

- basic tox configuration
- Makefile
- .editorconfig
- .pythonversion
- sphinx docs
- MANIFEST.in checking
- sane coverage defaults
- sane pylint defaults

Credits
=======

Cookiecutter was created by `Audrey Roy Greenfeld`_.

.. links go below here
.. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/
.. _`Audrey Roy Greenfeld`: https://github.com/audreyr
