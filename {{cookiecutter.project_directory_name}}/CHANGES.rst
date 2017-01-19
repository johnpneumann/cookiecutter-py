{% for n in range(cookiecutter.project_name|length) %}={% endfor %}==========
{{ cookiecutter.project_name }} changelog
{% for n in range(cookiecutter.project_name|length) %}={% endfor %}==========

This contains all major version changes.

{{ cookiecutter.version }}
{% for n in range(cookiecutter.version|length) %}-{% endfor %}

- Initial release
