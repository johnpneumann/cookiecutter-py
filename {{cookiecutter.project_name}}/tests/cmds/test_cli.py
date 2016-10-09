# -*- coding: utf-8 -*-
"""
    cmds.test_cli
    ~~~~~~~~~~~~~

    Runs the unit tests for the CLI.

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

from click import testing

from {{ cookiecutter.project_slug }} import __version__ as version
from {{ cookiecutter.project_slug }}.cmds import cli


@pytest.fixture
def clirunner():
    """CLI runner fixture."""
    return testing.CliRunner()


def test_cli_version(clirunner):
    """Ensure that the cli version is called correctly."""
    result = clirunner.invoke(cli.dopeproject, ['--version'])
    assert result.exception is None
    assert 0 == result.exit_code
    assert 'dopeproject, version {0}\n'.format(version) == result.output
