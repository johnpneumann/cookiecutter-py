# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""
    cmds.cli
    ~~~~~~~~

    Command line interface for use with {{ cookiecutter.project_slug }}.

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
from __future__ import absolute_import

import logging

import click

from .. import __version__ as version


LOGGER = logging.getLogger(__name__)


@click.group()
@click.version_option(version, help="Print the version number and exit.")
def {{ cookiecutter.project_slug }}():
    """{{ cookiecutter.project_name }} CLI.

    You can find the logs directory in your home directory under pylogs/{{cookiecutter.project_slug}}.

    """
    pass  # pragma: no cover


if __name__ == "__main__":
    {{ cookiecutter.project_slug }}()
