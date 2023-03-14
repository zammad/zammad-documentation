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
extensions = ['versionwarning.extension', 'sphinx_tabs.tabs']

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

   # We're running outside of readthedocs and expect the compiled version to 
   # be a pre release
   branch = 'pre-release'

else:
   # Override default css to get a larger width for ReadTheDoc build
   html_css_files = [
      'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
      'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
      'theme/theme_overrides.css'
   ]

   html_js_files = [
      'theme/zammad_overrides.js',
   ]

   # Get current version we're on for possible version warning
   version = os.environ.get('READTHEDOCS_VERSION')

   # If we're **not on latest**, we'll display a deprecation warning.
   if version == 'latest':
      branch = version
   elif version == 'pre-release':
      branch = "pre-release"
   else:
      branch = "old-version"

# Default definitions for this documentations version warnings if applicable
# https://sphinx-version-warning.readthedocs.io/en/latest/configuration.html
versionwarning_project_slug = "zammad-documentation"
versionwarning_admonition_type = "warning"
versionwarning_project_version = branch
versionwarning_body_selector = "div.document"

versionwarning_messages = {
   "pre-release": (
      "You're viewing a <strong>pre-release</strong> version of this "
      "documentation! If you want to see the stable, current version of "
      "this documentation, please see "
      '<a href="https://docs.zammad.org/en/latest/" '
      'title="current documentation version">here</a>.'
   ),
   "old-version": (
      "You're viewing a <strong>deprecated</strong> version of Zammad's "
      "documentation. If you're still running that version, please consider "
      '<a href="https://docs.zammad.org/en/latest/install/update.html" '
      'title="Updating Zammad">Updating Zammad</a> asap.'
   ),
}
