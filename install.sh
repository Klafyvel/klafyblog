apt-get install libapache2-mod-wsgi
a2enmod wsgi

python3 -m pip install -r virtualenv

python3 -m venv env_blog

source env_blog/bin/activate

python3 -m pip install -r requirements

deactivate

echo "Please configure your Appache site, then reload."
