#! /bin/bash

apt-get install -y libapache2-mod-wsgi-py3
a2enmod wsgi

apt-get install -y python3-venv

python3 -m venv env_blog

source env_blog/bin/activate && python3 -m pip install -r requirements.txt && deactivate

chown -R www-data:www-data .

echo "Please configure your Appache site, then reload."
