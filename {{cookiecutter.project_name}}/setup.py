#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import ast
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('{{ cookiecutter.project_slug }}/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))


setup(
    name='{{ cookiecutter.project_slug }}',
    version=version,
    author='{{ cookiecutter.author_name }}',
    description='{{ cookiecutter.project_description }}',
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    dependency_links=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    platforms='any',
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
    {% if cookiecutter.command_line_interface|lower != 'no' %}'Click',{% endif %}
    ],
    tests_require=[
        'mock',
        'pytest',
        'pytest-cov',
    ],
    entry_points={
    {% if cookiecutter.command_line_interface|lower != 'no' %}
        'console_scripts': [
            '{{ cookiecutter.project_cli_command }} = {{ cookiecutter.project_slug }}.cmds.cli:{{ cookiecutter.project_slug }}'
        ]
    {% endif %}
    }
)
