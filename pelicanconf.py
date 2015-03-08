#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
BASE = os.path.dirname(__file__)

AUTHOR = 'Mario Idival'
SITENAME = 'Mario Idival on Blog'
SITESUBTITLE = 'Não sou bom escrevendo'

if not os.environ.get("PELICAN_ON_DEV"):
    SITEURL = 'https://marioidival.github.io/'
else:
    SITEURL = "http://localhost:8000/"

PATH = 'content'
TIMEZONE = 'America/Recife'
DEFAULT_LANG = 'pt'
DISQUS_SITENAME = u'marioidivalgithubio'
EMAIL = "marioidival@gmail.com"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TWITTER_USERNAME = "marioidival"

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = False

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = False

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = False

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = False


# Blogroll
#LINKS = (
#    ('Home', '/'),
#    ('Arquivos', '/archives.html'),
#    ('Tags', '/tags.html'),
#)

# Social widget
SOCIAL = (
    ('github', 'http://github.com/marioidival'),
    ('linkedin', u'http://pt.linkedin.com/in/marioidival'),
    ('twitter', 'http://www.twitter.com/marioidival'),
    ('facebook', 'http://www.facebook.com/marioidival'),
)

DEFAULT_PAGINATION = 10
# THEME = 'themes/jesuislibre'
THEME = "built-texts/"

AUTHOR_IMG = 'https://avatars0.githubusercontent.com/u/1129263?v=2&s=460'
COLOPHON = True
COLOPHON_TITLE = 'https://marioidival.github.io'
COLOPHON_CONTENT = """
    Mário Idival, 23 anos. Desenvolvedor Web focado no Back-end utilizando Python (Pyramid) com MongoDB atualmente.
"""

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
