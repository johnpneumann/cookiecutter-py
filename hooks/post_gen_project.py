# -*- coding: utf-8 -*-
"""
    hooks.post_gen_project
    ~~~~~~~~~~~~~~~~~~~~~~

    Post generation hooks to modify the project based on options.

    :copyright: (c) 2016 by John P. Neumann.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys
import errno
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_dir(dirpath):
    """Removes a directory.

    Args:
        dirpath (str): The path to the directory to remove.

    Returns:
        int. Status code of success or failure.
             0 is success, 1 is failure.

    """
    try:
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))
    except OSError as err:
        if err.errno == errno.ENOENT:
            return 0
        return 1
    return 0


def remove_file(filepath):
    """Removes a file.

    Args:
        filepath (str): The path to the file to remove.

    Returns:
        int. Status code of success or failure.
             0 is success, 1 is failure.

    """
    try:
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    except OSError as err:
        if err.errno == errno.ENOENT:
            return 0
        return 1
    return 0


if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
    if remove_dir(os.path.join('{{ cookiecutter.project_slug }}', 'cmds')):
        sys.stderr.write('Failed to remove cmds dir.\n')
    if remove_dir(os.path.join('tests', 'cmds')):
        sys.stderr.write('Failed to remove tests/cmds dir.\n')


if 'Not open source' == '{{ cookiecutter.open_source_license }}':
    if remove_file('LICENSE'):
        sys.stderr.write('Failed to remove LICENSE file.\n')
