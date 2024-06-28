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

# Populate the ~/.zsh_history with some commands, so users are getting some hints while in the workshop
cat <<EOF >> ~/.zsh_history
: 1719583423:0;cd snapstagram
: 1719583423:0;python manage.py migrate
: 1719583423:0;python manage.py runserver
: 1719583423:0;python manage.py createsuperuser
: 1719583423:0;python manage.py startapp post
: 1719583423:0;python manage.py makemigrations
: 1719583423:0;python manage.py test
EOF
