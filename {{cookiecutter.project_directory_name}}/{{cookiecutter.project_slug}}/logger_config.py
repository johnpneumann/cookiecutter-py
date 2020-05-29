# -*- coding: utf-8 -*-
"""Centralized logging configuration for {{ cookiecutter.project_slug }}.

This handles setting up the logging configuration for the package.

"""
{% if cookiecutter.use_file_logger == 'yes' -%}
import os
import sys
import errno


{% else %}

{% endif -%}


def get_logging_config() -> dict:
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
    {% if cookiecutter.use_file_logger == 'yes' -%}if os.environ.get('{{cookiecutter.file_logger_env_var_name}}'):
        log_dir = os.environ['{{cookiecutter.file_logger_env_var_name}}']
    else:
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
        'maxBytes': 10 * 1024 * 1024,
        'backupCount': 5,
        'formatter': 'default',
    }
    logging_config['loggers']['root']['handlers'].append('file')
    logging_config['loggers']['{{cookiecutter.project_slug}}']['handlers'].append('file')
    return logging_config


    {%- else -%}
    return logging_config

    {%- endif %}
