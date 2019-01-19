{% if cookiecutter.module_version == '10.0'  %}
# -*- coding: utf-8 -*-
{% endif %}

from odoo import api, fields, models

class {{ cookiecutter.main_module|upper}}(models.Model):
    pass
