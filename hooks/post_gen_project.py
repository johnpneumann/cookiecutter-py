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
    """Removes a directory from the specified cookiecutter project directory.

    Args:
        dirpath (str): The relative path of the directory within the cookiecutter project directory to remove.

    Returns:
        int. Status code of success or failure.
             0 is success, 1 is failure.

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
        >>> remove_dir('tests')
        0

        Removing a directory that does not exist, will still succeed,
        since the assumption is you don't want it there.
        >>> remove_dir('foobar')
        0

        Attempting to remove a file, will fail though.
        >>> remove_dir('CHANGES.rst')

    """
    try:
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))
    except OSError as err:
        if err.errno == errno.ENOENT:
            return 0
        return 1
    return 0


def remove_file(filepath):
    """Removes a file from the specified cookiecutter project directory.

    Args:
        filepath (str): The relative path of the file within the cookiecutter project directory to remove.

    Returns:
        int. Status code of success or failure.
             0 is success, 1 is failure.

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
        >>> remove_file('CHANGES.rst')
        0

        Attempting to remove a file that doesn't exist, will still succeed,
        since the assumption is you don't want it there.
        >>> remove_file('foobar')
        0

		Attempting to remove a directory fails.
        >>> remove_file('tests')
        1

    """
    try:
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    except OSError as err:
        if err.errno == errno.ENOENT:
            return 0
        return 1
    return 0


def rename_path(filepath, newpath):
    """Renames a file or directory in the specified cookiecutter project directory.

    Args:
        filepath (str): The relative path of the file within the cookiecutter project directory to rename.
        newpath (str): The relative path of the file within the cookiecutter project directory to rename it to.

    Returns:
        int. Status code of success or failure.
             0 is success, 1 is failure.

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
		>>> rename_path('CHANGES.rst', 'CHANGES.md')
	    0

        Rename a directory.
        >>> rename_path('docs', 'generated_docs')
        0

        Attempting to rename a file or directory that doesn't exist, fails.
        >>> rename_path('foo', 'bar')
        1

    """
    try:
        os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, newpath))
    except OSError as err:
        return 1
    return 0


def cleanup():
    """Cleanup files and directories based on cookiecutter options."""
    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        if remove_dir(os.path.join('{{ cookiecutter.project_slug }}', 'cmds')):
            sys.stderr.write('Failed to remove cmds dir.\n')
        if remove_dir(os.path.join('tests', 'cmds')):
            sys.stderr.write('Failed to remove tests/cmds dir.\n')

    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        if remove_file('LICENSE'):
            sys.stderr.write('Failed to remove LICENSE file.\n')

    if '{{ cookiecutter.use_git }}' == 'yes':
        if rename_path('git', '.git'):
            sys.stderr.write('Failed to rename git to .git.\n')
    else:
        if remove_dir('git'):
            sys.stderr.write('Failed to remove git dir.\n')
    return


if __name__ == "__main__":
    cleanup()
