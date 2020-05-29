# -*- coding: utf-8 -*-
"""Hooks to run before project generation.

Runs any checks against the variables that have been entered before the
project gets generated on disk. Generally this just acts as a sanity check
to ensure that someone doesn't enter something stupid.

"""

import re
import sys


MODULE_MATCHER = r'^[_a-zA-Z][_a-zA-Z\d]+$'
PYTHON_VERSION_MATCHER = r'^\d\.\d[\.\d]*$'


module_name = '{{ cookiecutter.project_slug }}'
if not re.match(MODULE_MATCHER, module_name):
    err = f'ERROR: Project slug ({module_name}) is not a valid module name. Allowed characters A-Z, a-z, 0-9, and _.\n'
    sys.stderr.write(err)
    sys.exit(1)

python_version = '{{ cookiecutter.python_version }}'
if not re.match(PYTHON_VERSION_MATCHER, python_version):
    err = f'ERROR: Python version ({python_version}) is not a valid version.\n'
    sys.stderr.write(err)
    sys.exit(1)

