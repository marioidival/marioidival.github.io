#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
BASE = os.path.dirname(__file__)

AUTHOR = 'Mario Idival'
SITENAME = 'Mario Idival on Blog'
SITESUBTITLE = 'Não sou bom escrevendo'
# SITEURL = 'https://marioidival.github.io'
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'
DISQUS_SITENAME = u'marioidivalgithubio'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Home', '/'),
    ('Arquivos', '/archives.html'),
    ('Tags', '/tags.html'),
)

# Social widget
SOCIAL = (
    ('github', 'http://github.com/marioidival'),
    ('linkedin', u'http://pt.linkedin.com/in/marioidival'),
    ('twitter', 'http://www.twitter.com/marioidival'),
    ('facebook', 'http://www.facebook.com/marioidival'),
)

DEFAULT_PAGINATION = 10
THEME = 'themes/jesuislibre'

AUTHOR_IMG = 'https://avatars0.githubusercontent.com/u/1129263?v=2&s=460'
AUTHOR_LINK = 'https://marioidival.github.io'
AUTHOR_SUMMARY = """Mário Idival, 23 anos. Desenvolvedor Web focado no Back-end
    utilizando Python (Pyramid) com MongoDB atualmente."""

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = Tru
