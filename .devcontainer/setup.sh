#!/bin/bash

set -euxo pipefail

# Install Python in the container
pip install Django==5.0.6

# Bootstraps the django codebase
rm -rf snapstagram || true # just in case it exist
django-admin startproject snapstagram

# Libraries needed by DRF
# As per https://www.django-rest-framework.org/#installation
pip3 install djangorestframework==3.15.2
pip3 install Markdown==3.6       # Markdown support for the browsable API.
pip3 install django-filter==24.2  # Filtering support
pip3 install pytz==2024.1           # Timezone support

# Additional libraries
# For Frontend JWT Authentication
pip install djangorestframework-simplejwt==5.3.1

pip freeze > snapstagram/requirements.txt

# Adding extra variables for the container
# Need export EMAIL_HOST=172.17.0.1
# to be added in ~/.bashrc or ~/.profile
# Add only if it doesn't exist
grep -qxF "export EMAIL_HOST" ~/.bashrc || echo "export EMAIL_HOST=172.17.0.1" >> ~/.bashrc
grep -qxF "export EMAIL_HOST" ~/.profile || echo "export EMAIL_HOST=172.17.0.1" >> ~/.profile
grep -qxF "export EMAIL_HOST" ~/.zshrc || echo "export EMAIL_HOST=172.17.0.1" >> ~/.zshrc
