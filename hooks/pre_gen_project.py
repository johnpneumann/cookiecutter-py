# -*- coding: utf-8 -*-
"""
    hooks.pre_gen_project
    ~~~~~~~~~~~~~~~~~~~~~

    Hooks to run before project generation.

    :copyright: (c) 2016 by John P. Neumann.
    :license: BSD, see LICENSE for more details.
"""

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, module_name):
    sys.stderr.write('ERROR: The project slug ({0}) is not a valid Python module name. Please do not use a - and use '
                     '_ instead\n'.format(module_name))
    sys.exit(1)
