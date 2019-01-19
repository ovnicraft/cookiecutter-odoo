import os
import re
import shutil


if "{{ cookiecutter.has_models }}" == "yes":
    os.mkdir("models")

if "{{ cookiecutter.has_wizards }}" == "yes":
    os.mkdir("wizards")

if "{{ cookiecutter.has_reports }}" == "yes":
    os.mkdir("reports")

if "{{ cookiecutter.has_controller}}" == "yes":
    os.mkdir("controllers")
