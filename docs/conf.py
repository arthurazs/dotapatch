#!/usr/bin/env python3
# coding: utf-8
# dotapatch documentation build configuration file, created by
# sphinx-quickstart on Thu Jan  4 11:19:55 2018.

from os.path import abspath
from sys import path

import sphinx_rtd_theme

path.insert(0, abspath('..'))

needs_sphinx = '1.6.5'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'dotapatch'
copyright = '2016, Arthur Zopellaro'
author = 'Arthur Zopellaro'

version = '2.4'
release = '2.4'

pygments_style = 'sphinx'

intersphinx_mapping = {'https://docs.python.org/3': None}

htmlhelp_basename = 'dotapatchdoc'

latex_documents = [
    (master_doc, 'dotapatch.tex', 'dotapatch Documentation',
     'Arthur Zopellaro', 'manual'),
]

man_pages = [
    (master_doc, 'dotapatch', 'dotapatch Documentation',
     [author], 1)
]

exclude_patterns = []

language = None

gettext_compact = False

texinfo_documents = [
    (master_doc, 'dotapatch', 'dotapatch Documentation',
     author, 'dotapatch', 'Parses Dota 2 text patches to html format.',
     'Miscellaneous'),
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
    'logo_only': True,
    'display_version': False
}
