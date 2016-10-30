# -*- coding: utf-8 -*-
"""
    tests.test_logger_config
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Tests the logger config.

    :copyright: (c) {{ cookiecutter.copyright_year }} by {% if cookiecutter.project_owner == "" %}{{ cookiecutter.author_name }}{% else %}{{ cookiecutter.project_owner }}{% endif %}.
    {%- if cookiecutter.open_source_license == 'Not open source' %}
"""
    {%- else %}
    {{ cookiecutter._license_strings[cookiecutter.open_source_license] }}
"""{% endif %}
{% if cookiecutter.use_file_logger == 'yes' %}
import os
import errno
{% endif -%}

import pytest
from mock import patch

from {{ cookiecutter.project_slug }} import logger_config


{% if cookiecutter.use_file_logger == 'yes' -%}
@patch('os.makedirs')
def test_logger_config_not_none(mock_makedirs, monkeypatch):
    """Ensure that the base call gets a valid logger config."""
    monkeypatch.setattr(os.path, 'expanduser', lambda x: '/tmp')
    mock_makedirs.return_value = True
    cfg = logger_config.get_logging_config()
    expected_logdir = '/tmp/pylogs/{{ cookiecutter.project_slug }}'
    mock_makedirs.assert_called_with(expected_logdir)
    assert isinstance(cfg, dict)


@patch('os.makedirs')
def test_logger_dir_from_environ(mock_makedirs, monkeypatch):
    """Ensure that the logger dir attempts to create the directory from the environment variable."""
    monkeypatch.setenv('{{ cookiecutter.file_logger_env_var_name }}', '/foo/bar/baz')
    mock_makedirs.return_value = True
    logger_config.get_logging_config()
    expected_logdir = '/foo/bar/baz'
    mock_makedirs.assert_called_with(expected_logdir)


@patch('os.path.isdir')
@patch('os.makedirs')
def test_logger_oserror_no_exist(mock_makedirs, mock_isdir, monkeypatch):
    """Ensure that we still get a dictionary back if we can't make the directory and it doesn't exist."""
    monkeypatch.setattr(os.path, 'expanduser', lambda x: '/tmp')
    mock_isdir.return_value = False
    mock_makedirs.side_effect = OSError
    cfg = logger_config.get_logging_config()
    assert isinstance(cfg, dict)


@patch('os.path.isdir')
@patch('os.makedirs')
def test_logger_oserror_exist(mock_makedirs, mock_isdir, monkeypatch):
    """Ensure that we still get a dictionary back if we can't make the directory and it doesn't exist."""
    monkeypatch.setattr(os.path, 'expanduser', lambda x: '/tmp')
    mock_isdir.return_value = True
    mock_makedirs.side_effect = OSError(errno.EEXIST)
    cfg = logger_config.get_logging_config()
    assert isinstance(cfg, dict)
{% else -%}
def test_logger_config_not_none():
    """Ensure that the base call gets a valid logger config."""
    cfg = logger_config.get_logging_config()
    assert isinstance(cfg, dict)
{% endif -%}
