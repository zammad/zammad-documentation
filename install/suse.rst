Install on SUSE via RPM
***********************

.. note:: Currently we only support SLES 12 and OpenSUSE with versions 42.2 and 42.3

Prerequisites
=============

.. include:: /install/includes/prerequisites.rst

nginx on SLES12
---------------

You may need to add a nginx repository if the existing repositories don't 
provide the package.

.. code-block:: sh

   $ sudo zypper addrepo "http://nginx.org/packages/sles/12" "nginx"

Add Repository and install Zammad
=================================

.. include:: /install/includes/repo_sles.rst

Now you can install the Zammad package.

.. code-block:: sh

   $ sudo zypper install zammad

.. include:: /install/includes/adjust-webserver-configuration.rst

.. include:: /install/includes/manage-services.rst