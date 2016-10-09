# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.project_slug }}.logger_config
    {% for n in range(cookiecutter.project_slug|length) %}~{% endfor %}~~~~~~~~~~~~~~

    Handles the logging configuration for the module.

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
import os
import sys
import errno


def get_logging_config():
    """Creates the logging configuration for us with some standard checking.

    Returns:
        dict. The dictionary configuration of the logger.

    """
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s [%(levelname)s]: %(message)s - %(filename)s'
            },
            'simple': {
                'format': '%(asctime)s [%(levelname)s]: %(message)s'
            },
            'verbose': {
                'format': '%(asctime)s [%(levelname)s]: %(message)s - %(filename)s -> (%(lineno)d)'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
        },
        'loggers': {
            'root': {
                'handlers': ['console'],
                'level': 'INFO'
            },
            '{{cookiecutter.project_slug}}': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'INFO'
            },
        },
    }
    log_dir = os.path.join(os.path.expanduser('~'), 'pylogs', '{{cookiecutter.project_slug}}')
    try:
        os.makedirs(log_dir)
    except OSError as err:
        if err.errno == errno.EEXIST and os.path.isdir(log_dir):
            pass
        else:
            sys.stderr.write('Could not create log directory {0}\n'.format(log_dir))
            return logging_config

    logging_config['handlers']['file'] = {
        'level': 'WARNING',
        'filename': os.path.join(log_dir, '{{cookiecutter.project_slug}}.log'),
        'class': 'logging.handlers.RotatingFileHandler',
        'maxBytes': 1024 * 5,
        'backupCount': 3,
        'formatter': 'default',
    }
    logging_config['loggers']['root']['handlers'].append('file')
    logging_config['loggers']['{{cookiecutter.project_slug}}']['handlers'].append('file')
    return logging_config
