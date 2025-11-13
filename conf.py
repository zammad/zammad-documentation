import sys
import os
import time

import sphinx_rtd_theme

html_logo = "images/zammad_logo_70x61@2x.png"
html_favicon = "images/favicon.ico"
project = u'Zammad System Documentation'
copyright = u'%s, Zammad' % time.strftime("%Y")
author = u'Zammad'

source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'html', 'doctrees']
extensions = [
   'versionwarning.extension',
   'sphinx_tabs.tabs',
   'sphinx.ext.extlinks',
   'sphinx_copybutton',
]

locale_dirs = ['locale/']
gettext_compact = False
language = "en"

html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_css_files = [
   'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
   'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
   'theme/theme_overrides.css'
]

html_js_files = [
   'theme/zammad_overrides.js',
]

# thanks to https://blog.deimos.fr/2014/10/02/sphinxdoc-and-readthedocs-theme-tricks-2/

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:

   # We're running outside of readthedocs and expect the compiled version to match the Git branch.
   git_branch = os.environ.get('ZAMMAD_DOCS_GIT_BRANCH', None)

   if git_branch == 'main':
      branch = 'latest'
   else:
      branch = 'pre-release'

else:

   # Get current version we're on for possible version warning
   rtd_version = os.environ.get('READTHEDOCS_VERSION')

   # If we're **not on latest**, we'll display a deprecation warning.
   if rtd_version == 'latest':
      branch = rtd_version
   elif rtd_version == 'pre-release':
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

# Provide aliases to common external documentation targets.
#   It supports automatic substitution for the current branch placeholders,
#   but always links to the English translation.
#
#   :admin-docs:`the administrator documentation </manage/users/index.html>`
#   :user-docs:`the user documentation </advanced/tabs.html>`
#
#   which may render the following links:
#
#   https://admin-docs.zammad.org/en/pre-release/manage/users/index.html
#   https://user-docs.zammad.org/en/latest/advanced/tabs.html
#
#   Note the need for including the file extension as part of the path
#   relative to the documentation root!
#
extlinks = {
   'admin-docs': (f'https://admin-docs.zammad.org/en/{branch}%s', ''),
   'user-docs': (f'https://user-docs.zammad.org/en/{branch}%s', ''),
}

copybutton_exclude = '.gp'
copybutton_line_continuation_character = '\\'

# Copy button can be disabled by adding the `:class: no-copybutton` to the code block.
copybutton_selector = 'div:not(.no-copybutton) > div.highlight > pre'
