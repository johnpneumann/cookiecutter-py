Documentation
=============

Documentation is handled via `Sphinx <http://www.sphinx-doc.org/en/stable/>`_.
We also utilize the `sphinx-rtd-theme <http://read-the-docs.readthedocs.io/en/latest/theme.html>`_
so that we can maintain consistency across our documentations look and functionality.

Building the documentation
--------------------------

To build the documentation, you'll need to have ``{{ cookiecutter.project_slug }}``, ``sphinx`` and the
``sphinx-rtd-theme`` installed (via virtualenv or otherwise). Once you have that
done, simply cd into the *docs* directory and run::

   make html

You should see the build output into *_build/html*, which you can then browse.

Building the API documentation
------------------------------

To build the documentation for the module, run the following command from the
top level directory of the repo::

   sphinx-apidoc -f -o docs/api {{ cookiecutter.project_slug }}

This will generate the docs for any code that has docstrings in it. From there
you can follow the same instructions for building the documentation above.

.. links go below here
.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _sphinx-rtd-theme: http://read-the-docs.readthedocs.io/en/latest/theme.html
