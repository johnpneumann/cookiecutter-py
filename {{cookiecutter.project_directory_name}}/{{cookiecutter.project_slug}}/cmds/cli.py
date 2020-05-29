# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""CLI commands for use with {{ cookiecutter.project_slug }}."""
import logging

import click

from .. import __version__ as version


LOGGER = logging.getLogger(__name__)


@click.group()
@click.version_option(version, help="Print the version number and exit.")
def {{ cookiecutter.project_slug }}():
    """{{ cookiecutter.project_name }} CLI.

    {% if cookiecutter.use_file_logger == 'yes' -%}
    You can find the logs directory in your home directory under pylogs/{{cookiecutter.project_slug}}.
    {% endif -%}

    """
    pass  # pragma: no cover


if __name__ == "__main__":
    {{ cookiecutter.project_slug }}()
