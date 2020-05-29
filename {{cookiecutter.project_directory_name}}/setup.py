#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import ast
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('{{ cookiecutter.project_slug }}/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name='{{ cookiecutter.project_slug }}',
    version=version,
    author='{{ cookiecutter.author_name }}',
    description='{{ cookiecutter.project_description }}',
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
{%- if cookiecutter.license in license_classifiers %}
    license="{{ cookiecutter.license }}",
{%- endif %}
    dependency_links=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
{%- if cookiecutter.license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.license] }}',
{%- endif %}
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: {{ cookiecutter.python_version }}',
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    platforms='any',
    setup_requires=[
{%- if cookiecutter.project_type|lower == 'library' %}
        'pytest-runner',
{%- endif %}
    ],
    install_requires=[
{%- if cookiecutter.project_type|lower == 'library' %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
        'click',
{%- endif %}
{%- endif %}
    ],
    tests_require=[
{%- if cookiecutter.project_type|lower == 'library' %}
        'pytest',
        'pytest-cov',
{%- endif %}
    ],
    entry_points={
{%- if cookiecutter.command_line_interface|lower == 'click' %}
        'console_scripts': [
            '{{ cookiecutter.project_cli_command }} = {{ cookiecutter.project_slug }}.cmds.cli:{{ cookiecutter.project_slug }}'
        ]
{%- endif %}
    }
)
