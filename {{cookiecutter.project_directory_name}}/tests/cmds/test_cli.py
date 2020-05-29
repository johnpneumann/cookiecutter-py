# -*- coding: utf-8 -*-
"""Unit tests for {{ cookiecutter.project_slug }}.cmds.cli"""
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
