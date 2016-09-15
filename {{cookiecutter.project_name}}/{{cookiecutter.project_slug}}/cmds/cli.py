# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""
    cmds.cli
    ~~~~~~~~

    Command line interface for use with {{cookiecutter.project_slug}}.

    :copyright: (c) 2016 by {{ cookiecutter.project_owner }}.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import

import sys
import logging

import click

from .. import __version__ as version


LOGGER = logging.getLogger(__name__)


@click.group()
@click.version_option(version, help="Print the version number and exit.")
def {{cookiecutter.project_slug}}():
    """{{cookiecutter.project_slug}} Cli.

    You can find the logs directory in your home directory under pylogs/{{cookiecutter.project_slug}}.

    """
    pass


if __name__ == "__main__":
    {{cookiecutter.project_slug}}()
