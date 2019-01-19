{% if cookiecutter.module_version == '10.0'  %}
# -*- coding: utf-8 -*-
{% endif %}
# Copyright <{{ cookiecutter.year }}> {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
# License {{ cookiecutter.open_source_license }}
{
    "name": "Module name",
    "summary": "{{ cookiecutter.module_short_description|default('Simple module') }}",
    "version": "{{ cookiecutter.module_version }}.1.0.0",
    "development_status": "{{ cookiecutter.development_status }}",
    "category": "Uncategorized",
    "website": "{{ cookiecutter.website }}",
    "author": "<{{ cookiecutter.author }}>",
    "maintainers": ["{{ cookiecutter.github_username }}"],
    "license": "{{ cookiecutter.open_source_license }}",
    "application": {%- if cookiecutter.is_application == 'yes' -%} True {% else %} False {% endif %},
    "installable": True,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    # "post_load": "post_load",
    # "uninstall_hook": "uninstall_hook",
    "depends": ["{{ cookiecutter.deps.split(',')|default('base')}}"],
    "data": [
        "security/security_{{ cookiecutter.main_module }}.xml",
        "security/ir.model.access.csv",
        "templates/assets.xml",
        "views/view_report.xml",
        "views/view_{{ cookiecutter.main_module }}.xml",
        "wizards/view_wizard.xml",
    ],
}
