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
import subprocess
from collections import OrderedDict

from cookiecutter import prompt


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_dir(dirpath):
    """Removes a directory from the specified cookiecutter project directory.

    Args:
        dirpath (:obj:`str`): The relative path of the directory within the cookiecutter project directory to remove.

    Returns:
        int. Status code of success or failure. Anything over 0 is failure.

    Examples:
        >>> glob.glob(PROJECT_DIRECTORY)
		['/Users/someuser/MyPythonProject/CHANGES.rst', '/Users/someuser/MyPythonProject/CONTRIBUTORS.rst',
		 '/Users/someuser/MyPythonProject/docs', '/Users/someuser/MyPythonProject/LICENSE',
		 '/Users/someuser/MyPythonProject/Makefile', '/Users/someuser/MyPythonProject/MANIFEST.in',
		 '/Users/someuser/MyPythonProject/python_project', '/Users/someuser/MyPythonProject/README.rst',
		 '/Users/someuser/MyPythonProject/requirements', '/Users/someuser/MyPythonProject/requirements.txt',
		 '/Users/someuser/MyPythonProject/setup.cfg', '/Users/someuser/MyPythonProject/setup.py',
		 '/Users/someuser/MyPythonProject/tests', '/Users/someuser/MyPythonProject/tox.ini']

        Remove a directory that exists.
        >>> remove_dir('/Users/someuser/MyPythonProject/tests')
        0

        Removing a directory that does not exist, will still succeed,
        since the assumption is you don't want it there.
        >>> remove_dir('/Users/someuser/MyPythonProject/foobar')
        0

        Attempting to remove a file, will fail though.
        >>> remove_dir('/Users/someuser/MyPythonProject/CHANGES.rst')

    """
    try:
        shutil.rmtree(dirpath)
    except OSError as err:
        if err.errno == errno.ENOENT:
            return 0
        return 1
    return 0


def remove_file(filepath):
    """Removes a file from the specified cookiecutter project directory.

    Args:
        filepath (:obj:`str`): The relative path of the file within the cookiecutter project directory to remove.

    Returns:
        int. Status code of success or failure. Anything over 0 is failure.

    Examples:
        >>> glob.glob(PROJECT_DIRECTORY)
		['/Users/someuser/MyPythonProject/CHANGES.rst', '/Users/someuser/MyPythonProject/CONTRIBUTORS.rst',
		 '/Users/someuser/MyPythonProject/docs', '/Users/someuser/MyPythonProject/LICENSE',
		 '/Users/someuser/MyPythonProject/Makefile', '/Users/someuser/MyPythonProject/MANIFEST.in',
		 '/Users/someuser/MyPythonProject/python_project', '/Users/someuser/MyPythonProject/README.rst',
		 '/Users/someuser/MyPythonProject/requirements', '/Users/someuser/MyPythonProject/requirements.txt',
		 '/Users/someuser/MyPythonProject/setup.cfg', '/Users/someuser/MyPythonProject/setup.py',
		 '/Users/someuser/MyPythonProject/tests', '/Users/someuser/MyPythonProject/tox.ini']

        Remove a file that exists.
        >>> remove_file('/Users/someuser/MyPythonProject/CHANGES.rst')
        0

        Attempting to remove a file that doesn't exist, will still succeed,
        since the assumption is you don't want it there.
        >>> remove_file('/Users/someuser/MyPythonProject/foobar')
        0

		Attempting to remove a directory fails.
        >>> remove_file('/Users/someuser/MyPythonProject/tests')
        1

    """
    try:
        os.remove(filepath)
    except OSError as err:
        if err.errno == errno.ENOENT:
            return 0
        return 1
    return 0


def rename_path(filepath, newpath):
    """Renames a file or directory in the specified cookiecutter project directory.

    Args:
        filepath (:obj:`str`): The relative path of the file within the cookiecutter project directory to rename.
        newpath (:obj:`str`): The relative path of the file within the cookiecutter project directory to rename it to.

    Returns:
        int. Status code of success or failure. Anything over 0 is failure.

    Examples:
        >>> glob.glob(PROJECT_DIRECTORY)
		['/Users/someuser/MyPythonProject/CHANGES.rst', '/Users/someuser/MyPythonProject/CONTRIBUTORS.rst',
		 '/Users/someuser/MyPythonProject/docs', '/Users/someuser/MyPythonProject/LICENSE',
		 '/Users/someuser/MyPythonProject/Makefile', '/Users/someuser/MyPythonProject/MANIFEST.in',
		 '/Users/someuser/MyPythonProject/python_project', '/Users/someuser/MyPythonProject/README.rst',
		 '/Users/someuser/MyPythonProject/requirements', '/Users/someuser/MyPythonProject/requirements.txt',
		 '/Users/someuser/MyPythonProject/setup.cfg', '/Users/someuser/MyPythonProject/setup.py',
		 '/Users/someuser/MyPythonProject/tests', '/Users/someuser/MyPythonProject/tox.ini']

        Rename a file.
		>>> rename_path('/Users/someuser/MyPythonProject/CHANGES.rst', '/Users/someuser/MyPythonProject/CHANGES.md')
	    0

        Rename a directory.
        >>> rename_path('/Users/someuser/MyPythonProject/docs', '/Users/someuser/MyPythonProject/generated_docs')
        0

        Attempting to rename a file or directory that doesn't exist, fails.
        >>> rename_path('/Users/someuser/MyPythonProject/foo', '/Users/someuser/MyPythonProject/bar')
        1

    """
    try:
        os.rename(filepath, newpath)
    except OSError as err:
        return 1
    return 0


def copy_file(filepath, destination):
    """Copies a file from one location to another.

    Args:
        filepath (:obj:`str`): The full path of the file to copy.
        destination (:obj:`str`): The full path to where to copy the file to.

    Returns:
        int. Status code of success or failure. Anything over 0 is failure.

    """
    try:
        shutil.copy2(filepath, destination)
    except (OSError, shutil.Error):
        return 1
    return 0


def copy_dir(filepath, destination):
    """Copies a directory and it's contents from one place to another.

    Args:
        filepath (:obj:`str`): The full path to the directory to copy.
        destination (:obj:`str`): The full path to the location you want the directory copied to.

    Returns:
        int. Status code of success or failure. Anything over 0 is failure.

    """
    try:
        shutil.copytree(filepath, destination)
    except (OSError, shutil.Error):
        return 1
    return 0


def cleanup():
    """Cleanup files and directories based on cookiecutter options."""
    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        if remove_dir(os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}', 'cmds')):
            sys.stderr.write('Failed to remove cmds dir.\n')
        if remove_dir(os.path.join(PROJECT_DIRECTORY, 'tests', 'cmds')):
            sys.stderr.write('Failed to remove tests/cmds dir.\n')

    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        if remove_file(os.path.join(PROJECT_DIRECTORY, 'LICENSE')):
            sys.stderr.write('Failed to remove LICENSE file.\n')

    if '{{ cookiecutter.use_git }}' == 'yes':
        if rename_path(os.path.join(PROJECT_DIRECTORY, 'git'), os.path.join(PROJECT_DIRECTORY, '.git')):
            sys.stderr.write('Failed to rename git to .git.\n')
        else:
            git_cmd = ['git', 'init', PROJECT_DIRECTORY]
            if subprocess.call(git_cmd):
                sys.stderr.write('Failed to initialize git repository.\n')
    return


if __name__ == "__main__":
    cleanup()
