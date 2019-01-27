import os
import re
import shutil


if "{{ cookiecutter.has_models }}" == "no":
    shutil.rmtree("models")

if "{{ cookiecutter.has_wizards }}" == "yes":
    os.mkdir("wizards")

if "{{ cookiecutter.has_reports }}" == "yes":
    os.mkdir("reports")

if "{{ cookiecutter.has_controller}}" == "yes":
    os.mkdir("controllers")
