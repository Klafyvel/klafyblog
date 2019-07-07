#! /bin/env python3
# Inspired by : https://github.com/carlos-jenkins/python-github-webhooks/blob/master/webhooks.py

import os

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))
import logging
import hmac
from hashlib import sha1
import json
from subprocess import Popen, PIPE
from configparser import ConfigParser
from pathlib import Path

import netaddr
import requests
import bottle
from bottle import route, run, abort, HTTPResponse, request

DEBUG = False

from logging.handlers import RotatingFileHandler

# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger()
# on met le niveau du logger à DEBUG, comme ça il écrit tout
logger.setLevel(logging.DEBUG)

# création d'un formateur qui va ajouter le temps, le niveau
# de chaque message quand on écrira un message dans le log
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
# créé précédement et on ajoute ce handler au logger
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

def get_whitelist():
    return netaddr.IPSet(
        map(
            netaddr.IPNetwork,
            requests.get("https://api.github.com/meta").json()["hooks"],
        )
    )


@route("/", method='POST')
def index():
    source_addr = netaddr.IPAddress(request.environ.get("REMOTE_ADDR"))
    logging.debug("Got ip address %s", str(source_addr))
    if source_addr not in get_whitelist():
        abort(403)
    logging.debug("Ip address is whitelisted.")
    header_signature = request.headers.get("X-Hub-Signature")
    if header_signature is None:
        abort(403)
    logging.debug("Request has header signature.")
    sha_name, signature = header_signature.split("=")
    if sha_name != "sha1":
        abort(501)
    logging.debug("Request has good sha name.")

    current_dir = Path(__file__).parent.absolute()

    config = ConfigParser()
    config.read(current_dir / "webhooks.conf")

    mac = hmac.new(str(config["BLOG"]["secret"]).encode("utf8"), msg=request.body.read(), digestmod="sha1")
    if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
        abort(403)
    logging.debug("Request has good secret.")

    event = request.headers.get("X-GitHub-Event", "ping")

    if event not in ["ping", "push"]:
        abord(501)
    logging.debug("Request has good event.")

    if event == "ping":
        return json.dumps({"msg": "pong"})
    try:
        payload = request.json
    except Exception as e:
        logging.warning("Request parsing failed : %s", e)
        abort(400)

    if payload["ref"] != "refs/heads/master":
        return HTTPResponse(body="Fine.", status=200)

    logging.info("Now updating git repository.")
    with Popen(
        ["/usr/bin/git", "-C", str(current_dir), "pull", "--force"], stdout=PIPE
    ) as proc:
        logging.debug(proc.stdout.read())
    logging.info("Done.")

    logging.info("Generating the files")
    with Popen(["/usr/bin/make", "html"], stdout=PIPE) as proc:
        logging.debug(proc.stdout.read())
    logging.info("Done.")

    return HTTPResponse(body="Fine.", status=200)


if DEBUG:
    run(host="localhost", port=6666)
else:
    application = bottle.default_app()
