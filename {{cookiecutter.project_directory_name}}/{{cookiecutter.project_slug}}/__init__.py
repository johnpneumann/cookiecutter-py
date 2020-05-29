# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_slug }}"""
import logging
import logging.config

from . import logger_config


__version__ = '{{ cookiecutter.version }}'
LOGGING_CONFIG = logger_config.get_logging_config()
logging.config.dictConfig(LOGGING_CONFIG)
