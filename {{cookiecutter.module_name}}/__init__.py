{% if cookiecutter.has_models == 'yes'  %}
from . import models
{% endif %}
{% if cookiecutter.has_wizards == 'yes'  %}
from . import wizards
{% endif %}
{% if cookiecutter.has_reports == 'yes'  %}
from . import reports
{% endif %}
