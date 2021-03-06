# -*- coding: utf-8 -*-
"""
    cmds.test_cli
    ~~~~~~~~~~~~~

    Runs the unit tests for the CLI.

    :copyright: (c) {{ cookiecutter.copyright_year }} by {% if cookiecutter.project_owner == "" %}{{ cookiecutter.author_name }}{% else %}{{ cookiecutter.project_owner }}{% endif %}.
    {%- if cookiecutter.open_source_license == 'Not open source' %}
"""
    {%- else %}
    {{ cookiecutter._license_strings[cookiecutter.open_source_license] }}
"""{% endif %}
import pytest

from click import testing

from {{ cookiecutter.project_slug }} import __version__ as version
from {{ cookiecutter.project_slug }}.cmds import cli


@pytest.fixture
def clirunner():
    """CLI runner fixture."""
    return testing.CliRunner()


def test_cli_version(clirunner):
    """Ensure that the cli version is called correctly."""
    result = clirunner.invoke(cli.{{ cookiecutter.project_slug }}, ['--version'])
    assert result.exception is None
    assert 0 == result.exit_code
