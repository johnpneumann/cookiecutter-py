# -*- coding: utf-8 -*-
"""
    tests.test_{{ cookiecutter.project_slug }}
    ~~~~~~~~~~~{% for n in range(cookiecutter.project_slug|length) %}~{% endfor %}

    Tests for `{{ cookiecutter.project_slug }}` module.

    :copyright: (c) {{ cookiecutter.copyright_year }} by {% if cookiecutter.project_owner == "" %}{{ cookiecutter.author_name }}{% else %}{{ cookiecutter.project_owner }}{% endif %}.
    {%- if cookiecutter.open_source_license == 'Not open source' %}
"""
    {%- else %}
    {{ cookiecutter._license_strings[cookiecutter.open_source_license] }}
"""{% endif %}
import pytest


def test_failure():
    """Base test that will always fail so remove it."""
    assert True == False
