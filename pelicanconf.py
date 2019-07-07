#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

import pelican_render_math

AUTHOR = "Klafyvel"
SITENAME = "KlafyBlog"
SITEURL = "https://klafyvel.me/blog/"

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("My personnal page", "https://klafyvel.me/"),
    ("Pelican", "http://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("My Twitter account", "https://twitter.com/Klafyvel"),
    ("My Github account", "https://github.com/Klafyvel"),
)

DEFAULT_METADATA = {"status": "draft"}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins"]
PLUGINS = [pelican_render_math, "decent_images"]
RESPONSIVE_IMAGES = True
