Install on Ubuntu via DEB
*************************

.. note:: We currently support Ubuntu 16.04 LTS, 18.04 LTS & 20.04 LTS.

Prerequisites
=============

.. include:: /install/includes/prerequisites.rst

.. include:: /install/includes/setup-locales.rst

Add Repository and install Zammad
=================================

.. include:: /install/includes/repo_ubuntu.rst

Now you can install the Zammad package.

.. code-block:: sh

   $ sudo apt-get update
   $ sudo apt-get install zammad

.. include:: /install/includes/adjust-webserver-configuration.rst

.. include:: /install/includes/manage-services.rst