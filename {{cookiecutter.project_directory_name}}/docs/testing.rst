Testing
=======

Testing is done via tox_. The only requirement to run the unit tests is...
tox, so all you need to do is::

   pip install --upgrade tox

And then run::

   tox

We use pytest_ for running the tests and pytest-cov_ to generate
the coverage reports. For more information, check the ``tox.ini`` file
to see the individual pieces that are run.

.. links go below here
.. _tox: http://tox.readthedocs.io/en/latest/
.. _pytest: http://pytest.org/latest/
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/
