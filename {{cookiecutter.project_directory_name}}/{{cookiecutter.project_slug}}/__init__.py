# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.project_slug }}
    {% for n in range(cookiecutter.project_slug|length) %}~{% endfor %}
    {{ cookiecutter.project_description }}

    :copyright: (c) {{ cookiecutter.copyright_year }} by {% if cookiecutter.project_owner == "" %}{{ cookiecutter.author_name }}{% else %}{{ cookiecutter.project_owner }}{% endif %}.
    {%- if cookiecutter.open_source_license == 'Not open source' %}
"""
    {%- else %}
    {{ cookiecutter._license_strings[cookiecutter.open_source_license] }}
"""{% endif %}
from __future__ import absolute_import

import logging
import logging.config

from . import logger_config


__version__ = '{{ cookiecutter.version }}'
LOGGING_CONFIG = logger_config.get_logging_config()
logging.config.dictConfig(LOGGING_CONFIG)
