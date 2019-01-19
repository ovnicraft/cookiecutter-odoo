{% if cookiecutter.has_models == 'yes' %}
from . import {{ cookiecutter.main_module }}
{% endif %}
