# -*- coding: utf-8 -*-
"""
    tests.test_logger_config
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Tests the logger config.

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

import pytest
from mock import patch

from {{ cookiecutter.project_slug }} import logger_config


@patch('os.makedirs')
def test_logger_config_not_none(mock_makedirs, monkeypatch):
    """Ensure that the base call gets a valid logger config."""
    monkeypatch.setattr(os.path, 'expanduser', lambda x: '/tmp')
    mock_makedirs.return_value = True
    cfg = logger_config.get_logging_config()
    expected_logdir = '/tmp/pylogs/{{ cookiecutter.project_slug }}'
    mock_makedirs.assert_called_with(expected_logdir)
    assert isinstance(cfg, dict)


@patch('os.path.isdir')
@patch('os.makedirs')
def test_logger_oserror_no_exist(mock_makedirs, mock_isdir, monkeypatch):
    """Ensure that we still get a dictionary back if we can't make the directory and it doesn't exist."""
    monkeypatch.setattr(os.path, 'expanduser', lambda x: '/tmp')
    mock_isdir.return_value = False
    mock_makedirs.side_effect = OSError
    cfg = logger_config.get_logging_config()
    assert isinstance(cfg, dict)
