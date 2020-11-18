import sys
import os
import time

import sphinx_rtd_theme

html_logo = "images/zammad_logo_70x61.png"
html_favicon = "images/favicon.ico"
project = u'Zammad'
copyright = u'%s, Zammad' % time.strftime("%Y")
author = u'Zammad'

source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'html', 'doctrees']
extensions = ['sphinx_tabs.tabs']

locale_dirs = ['locale/']
gettext_compact = False
language = "en"

html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# thanks to https://blog.deimos.fr/2014/10/02/sphinxdoc-and-readthedocs-theme-tricks-2/

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    # Override default css to get a larger width for local build
    def setup(app):
        app.add_js_file('theme/zammad_overrides.js')
        app.add_css_file('theme/theme_overrides.css')
else:
    # Override default css to get a larger width for ReadTheDoc build
    html_context = {
        'css_files': [
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/theme/theme_overrides.css'
        ],
        'js_files': [
            '_static/theme/zammad_overrides.js'
        ],
    }
