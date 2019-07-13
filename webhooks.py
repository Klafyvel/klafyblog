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
import shutil

import netaddr
import requests
from bottle import route, run, abort, HTTPResponse

DEBUG = True


def get_whitelist():
    return netaddr.IPSet(
        map(
            netaddr.IPNetwork,
            requests.get("https://api.github.com/meta").json()["hooks"],
        )
    )


@route("/deploy")
def index(name):
    source_addr = nataddr.IPAddress(request.environ.get("REMOTE_ADDR"))
    if source_addr not in get_whitelist():
        abort(403)
    header_signature = request.headers.get("X-Hub-Signature")
    if header_signature is None:
        abort(403)
    sha_name, signature = header_signature.split("=")
    if sha_name != "sha1":
        abort(501)

    current_dir = Path(__file__).parent.absolute()

    config = ConfigParser()
    config.read(current_dir / "webhooks.conf")

    mac = hmac.new(
        str(config["secret"]).encode("utf8"), msg=request.body.read(), digestmod="sha1"
    )
    if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
        abort(403)

    event = request.headers.get("X-GitHub-Event", "ping")

    if event not in ["ping", "push"]:
        abord(501)

    if event == "ping":
        return json.dumps({"msg": "pong"})
    try:
        payload = request.get_json()
    except Exception:
        logging.warning("Request parsing failed")
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

    logging.info("Copying the files to %s", config["blog_location"])
    shutil.move(current_dir / "output", dst)
    logging.info("Done.")

    return HTTPResponse(body="Fine.", status=200)


if DEBUG:
    run(host="localhost", port=6666)
else:
    application = bottle.default_app()
