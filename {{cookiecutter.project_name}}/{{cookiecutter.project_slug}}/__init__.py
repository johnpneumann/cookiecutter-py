# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.project_slug }}
    {% for n in range(cookiecutter.project_slug|length) %}~{% endfor %}
    {{ cookiecutter.project_description }}

    :copyright: (c) {{ cookiecutter.copyright_year }} by {% if cookiecutter.project_owner == "" %}{{ cookiecutter.author_name }}{% else %}{{ cookiecutter.project_owner }}{% endif %}.
    {% if cookiecutter.open_source_license == 'MIT license' -%}
    :license: MIT, see LICENSE for more details.
    {% elif cookiecutter.open_source_license == 'BSD license' -%}
    :license: BSD, see LICENSE for more details.
    {% elif cookiecutter.open_source_license == 'ISC license' -%}
    :license: ISC, see LICENSE for more details.
    {% elif cookiecutter.open_source_license == 'Apache Software License 2.0' -%}
    :license: Apache Software License, see LICENSE for more details.
    {% elif cookiecutter.open_source_license == 'GNU General Public License v3' -%}
    :license: GPLv3, see LICENSE for more details.
    {% endif -%}

"""
from __future__ import absolute_import

import logging
import logging.config

from . import logger_config


__version__ = '{{ cookiecutter.version }}'
LOGGING_CONFIG = logger_config.get_logging_config()
logging.config.dictConfig(LOGGING_CONFIG)
