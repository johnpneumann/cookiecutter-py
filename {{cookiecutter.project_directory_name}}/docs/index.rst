:orphan:

.. {{ cookiecutter.project_slug }} documentation master file, created by
   sphinx-quickstart on Thu Nov 13 14:46:01 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

###########{% for n in range(cookiecutter.project_name|length) %}#{% endfor %}
Welcome to {{ cookiecutter.project_name}}
###########{% for n in range(cookiecutter.project_name|length) %}#{% endfor %}

Welcome to the {{ cookiecutter.project_name }} documentation. The documentation is
divided into different sections so you can get what you need easily.

{{ cookiecutter.project_description }}

Getting Started
===============

.. toctree::
   :maxdepth: 4

   setup
   install
   usage

Additional Notes
================

Any additional notes that may help with usage, testing,
building, etc.


.. toctree::
   :maxdepth: 2

   testing
   documentation

Module API Reference
====================

.. toctree::
   :maxdepth: 2

   api/modules

Third Party Libraries
=====================

{{ cookiecutter.project_slug }} depends on several libraries that are not documented within
these pages. If you'd like to read the documentation on those libraries
feel free to visit the links below:
{% if cookiecutter.command_line_interface|lower == 'click' %}
- Click_

.. _Click: http://click.pocoo.org/6/
{%- else %}
- `example library Documentation`_

.. _`example library Documentation`: http://example.com/en/latest/
{%- endif %}

Credits
=======

This package was created with Cookiecutter_ and the `johnpneumann/cookiecutter-py`_ project
template version {{ cookiecutter._cookiecutter_py_version }}.

Documentation is generated by Sphinx_ using the sphinx-rtd-theme_.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. links go below here
.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _sphinx-rtd-theme: http://read-the-docs.readthedocs.io/en/latest/theme.html
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`johnpneumann/cookiecutter-py`: https://github.com/johnpneumann/cookiecutter-py
