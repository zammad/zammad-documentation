Install on Debian via DEB
*************************

.. note:: Currently we support Debian 9 and 10. Debian 8 support has been dropped with Zammad 3.5.

Prerequisites
=============

.. include:: /install/includes/prerequisites.rst

.. include:: /install/includes/setup-locales.rst

Add Repository and install Zammad
=================================

.. include:: /install/includes/repo_debian.rst

Now you can install the Zammad package.

.. code-block:: sh

   $ sudo apt-get update
   $ sudo apt-get install zammad

.. include:: /install/includes/adjust-webserver-configuration.rst

.. include:: /install/includes/manage-services.rst