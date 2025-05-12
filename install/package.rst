Install with Package Manager
============================

.. include:: /install/includes/hosted-services.rst

Prerequisites
-------------

Before performing the following steps, make sure to meet
Zammad's :doc:`software requirements </prerequisites/software>`.

1. Install Required Tools
^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to already mentioned :ref:`software dependencies <package_dependencies>`,
some operating systems may require additional packages if not already installed.

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh

         $ sudo apt install curl apt-transport-https gnupg

   .. tab:: OpenSUSE / SLES

      OpenSUSE doesn't require any additional steps here!

      SLES 15 requires additional repositories to be
      activated. To do so, run the following commands.

      .. code-block:: sh

         $ sudo SUSEConnect --product sle-module-desktop-applications/$(. /etc/os-release; echo $VERSION_ID)/$(uname -i)
         $ sudo SUSEConnect --product PackageHub/$(. /etc/os-release; echo $VERSION_ID)/$(uname -i)

   .. tab:: CentOS / RHEL

      .. code-block:: sh

         $ sudo yum install wget epel-release

2. Install Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^

Elasticsearch is not a hard dependency of Zammad, but strongly recommended! It
needs to be installed before Zammad. Please take a look at the
:doc:`instructions </install/elasticsearch>` first.

3. Ensure Correct Locale
^^^^^^^^^^^^^^^^^^^^^^^^

To make Zammad work correctly, your system has to use the correct locales.

.. tabs::

   .. tab:: Ubuntu / Debian

      List your current locale settings.

      .. code-block:: sh

         $ locale | grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ sudo apt install locales
         $ sudo locale-gen en_US.UTF-8
         $ echo "LANG=en_US.UTF-8" > sudo /etc/default/locale

      After fixing it, make sure to check the output again for including
      ``<lang_code>.utf8``. A reboot may help if unsuccessful.

   .. tab:: OpenSUSE / SLES

      List your current locale settings.

      .. code-block:: sh

         $ localectl status | grep LANG

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ sudo localectl set-locale LANG=en_US.UTF-8

      After fixing it, make sure to check the output again for including
      ``<lang_code>.utf8``. A reboot may help if unsuccessful.

      .. hint::

         By default OpenSUSE uses ``POSIX`` as ``LANG`` value for the root
         user. Learn more about this within the `OpenSUSE documentation
         <https://doc.opensuse.org/documentation/leap/startup/html/book-opensuse-startup/cha-yast-lang.html#pro-yast-lang-additional>`_.

         This does not affect other users and thus can be ignored.

   .. tab:: CentOS / RHEL

      List your current locale settings.

      .. code-block:: sh

         $ locale | grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ sudo localectl set-locale LANG=en_US.UTF-8

      After fixing it, make sure to check the output again for including
      ``<lang_code>.utf8``. A reboot may help if unsuccessful.

Add Repository and Install Zammad
---------------------------------

.. hint:: Packager.io may not be accessible from IPv6-only environments, so make
   sure to consider this when performing the steps below.

Add Repository
^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Ubuntu

      Install Repository Key
         .. code-block:: sh

            $ curl -fsSL https://dl.packager.io/srv/zammad/zammad/key | \
               gpg --dearmor | sudo tee /etc/apt/keyrings/pkgr-zammad.gpg> /dev/null

      Ubuntu 20.04
         .. code-block:: sh

            $ echo "deb [signed-by=/etc/apt/keyrings/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu 20.04 main"| \
               sudo tee /etc/apt/sources.list.d/zammad.list > /dev/null

      Ubuntu 22.04
         .. code-block:: sh

            $ echo "deb [signed-by=/etc/apt/keyrings/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu 22.04 main"| \
               sudo tee /etc/apt/sources.list.d/zammad.list > /dev/null



      Ubuntu 24.04
         .. hint:: Starting with Ubuntu 24.04, we provide the command to add the
            repository in the
            `deb822 format <https://repolib.readthedocs.io/en/latest/deb822-format.html>`_.

         .. code-block:: sh

            $ printf "Types: deb
              URIs: https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu
              Suites: 22.04
              Components: main
              Signed-By: /etc/apt/keyrings/pkgr-zammad.gpg" | \
              sudo tee /etc/apt/sources.list.d/zammad.sources > /dev/null

   .. tab:: Debian

      Install Repository Key
         .. code-block:: sh

            $ curl -fsSL https://dl.packager.io/srv/zammad/zammad/key | \
               gpg --dearmor | sudo tee /etc/apt/keyrings/pkgr-zammad.gpg> /dev/null

      Debian 11
         .. code-block:: sh

            $ echo "deb [signed-by=/etc/apt/keyrings/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/debian 11 main"| \
               sudo tee /etc/apt/sources.list.d/zammad.list > /dev/null

      Debian 12
         .. code-block:: sh

            $ echo "deb [signed-by=/etc/apt/keyrings/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/debian 12 main"| \
               sudo tee /etc/apt/sources.list.d/zammad.list > /dev/null

   .. tab:: OpenSUSE / SLES

      Install Repository Key
         .. code-block:: sh

            $ sudo rpm --import https://dl.packager.io/srv/zammad/zammad/key

      openSUSE 15.x / SLES 15
         .. code-block:: sh

            $ sudo wget -O /etc/zypp/repos.d/zammad.repo \
            https://dl.packager.io/srv/zammad/zammad/stable/installer/sles/15.repo


   .. tab:: CentOS / RHEL

      Install Repository Key
         .. code-block:: sh

            $ sudo rpm --import https://dl.packager.io/srv/zammad/zammad/key

      CentOS 8 / RHEL 8
         .. code-block:: sh

            $ sudo wget -O /etc/yum.repos.d/zammad.repo \
            https://dl.packager.io/srv/zammad/zammad/stable/installer/el/8.repo

      CentOS 9 / RHEL 9
         .. code-block:: sh

            $ sudo wget -O /etc/yum.repos.d/zammad.repo \
            https://dl.packager.io/srv/zammad/zammad/stable/installer/el/9.repo


Install Zammad
^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh

         $ sudo apt update
         $ sudo apt install zammad

   .. tab:: OpenSUSE / SLES

      .. code-block:: sh

         $ sudo zypper ref
         $ sudo zypper install zammad

   .. tab:: CentOS / RHEL

      .. code-block:: sh

         $ sudo yum install zammad

      Due to an `issue <https://github.com/crohr/pkgr/issues/165>`_ with
      packager.io on CentOS you'll need to correct file permissions for
      public files.

      .. code-block:: sh

         sudo chmod -R 755 /opt/zammad/public/

.. include:: /install/includes/firewall-and-selinux.rst

.. include:: /install/includes/manage-services.rst

.. include:: /install/includes/next-steps.rst
