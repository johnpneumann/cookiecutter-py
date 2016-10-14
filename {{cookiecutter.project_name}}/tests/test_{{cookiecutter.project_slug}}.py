# -*- coding: utf-8 -*-
"""
    tests.test_{{ cookiecutter.project_slug }}
    ~~~~~~~~~~~{% for n in range(cookiecutter.project_slug|length) %}~{% endfor %}

    Tests for `{{ cookiecutter.project_slug }}` module.

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
import pytest


def test_failure():
    """Base test that will always fail so remove it."""
    assert True == False
