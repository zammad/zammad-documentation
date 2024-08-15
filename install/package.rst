Package Installation
====================

.. note::

   | Please ensure to meet Zammads :doc:`/prerequisites/software` requirements
     beforehand.
   | This page expects administrative permissions, this is why ``sudo`` is
     not used.

Prerequisites
-------------

Additional software dependencies
--------------------------------

1. Install Required Tools
^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to already mentioned :ref:`software dependencies <package_dependencies>`,
some operating systems may require additional packages if not already installed.

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh

         $ apt install curl apt-transport-https gnupg

   .. tab:: SLES 15

      The openSUSE Enterprise 15 variant requires additional repositories to be
      activated. To do so, run the following commands.

      .. code-block:: sh

         $ SUSEConnect --product sle-module-desktop-applications/$(. /etc/os-release; echo $VERSION_ID)/$(uname -i)
         $ SUSEConnect --product PackageHub/$(. /etc/os-release; echo $VERSION_ID)/$(uname -i)

   .. tab:: CentOS

      .. code-block:: sh

         $ yum install wget epel-release

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

         $ locale |grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ sudo apt install locales
         $ sudo locale-gen en_US.UTF-8
         $ echo "LANG=en_US.UTF-8" > sudo /etc/default/locale

   .. tab:: CentOS

      List your current locale settings.

      .. code-block:: sh

         $ locale |grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ sudo localectl set-locale LANG=en_US.utf8

   .. tab:: OpenSUSE / SLES

      List your current locale settings.

      .. code-block:: sh

         $ localectl status |grep "LC_CTYPE"

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ sudo localectl set-locale LC_CTYPE=en_US.UTF-8

      .. hint::

         By default OpenSUSE uses ``POSIX`` as ``LANG`` value for the root
         user. Learn more about this within the `OpenSUSE documentation
         <https://doc.opensuse.org/documentation/leap/startup/html/book-opensuse-startup/cha-yast-lang.html#pro-yast-lang-additional>`_.

         This does not affect other users and thus can be ignored.


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
                 gpg --dearmor | tee /etc/apt/trusted.gpg.d/pkgr-zammad.gpg> /dev/null

         Ubuntu 20.04
            .. code-block:: sh

               $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu 20.04 main"| \
                  tee /etc/apt/sources.list.d/zammad.list > /dev/null

         Ubuntu 22.04
            .. code-block:: sh

               $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu 22.04 main"| \
                  tee /etc/apt/sources.list.d/zammad.list > /dev/null

         Ubuntu 24.04
            .. code-block:: sh

               $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu 24.04 main"| \
                  tee /etc/apt/sources.list.d/zammad.list > /dev/null

      .. tab:: Debian

         Install Repository Key
            .. code-block:: sh

               $ curl -fsSL https://dl.packager.io/srv/zammad/zammad/key | \
                 gpg --dearmor | tee /etc/apt/trusted.gpg.d/pkgr-zammad.gpg> /dev/null

         Debian 11
            .. code-block:: sh

               $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/debian 11 main"| \
                  tee /etc/apt/sources.list.d/zammad.list > /dev/null

         Debian 12
            .. code-block:: sh

               $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/debian 12 main"| \
                  tee /etc/apt/sources.list.d/zammad.list > /dev/null

      .. tab:: CentOS

         Install Repository Key
            .. code-block:: sh

               $ rpm --import https://dl.packager.io/srv/zammad/zammad/key

         RHEL 8 / CentOS 8
            .. code-block:: sh

               $ wget -O /etc/yum.repos.d/zammad.repo \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/el/8.repo

         RHEL 9 / CentOS 9
            .. code-block:: sh

               $ wget -O /etc/yum.repos.d/zammad.repo \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/el/9.repo

      .. tab:: OpenSUSE / SLES

         Install Repository Key
            .. code-block:: sh

               $ rpm --import https://dl.packager.io/srv/zammad/zammad/key

         SLES 15 / openSUSE 15.x
            .. code-block:: sh

               $ wget -O /etc/zypp/repos.d/zammad.repo \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/sles/15.repo

Install Zammad
^^^^^^^^^^^^^^

   .. tabs::

      .. tab:: Ubuntu / Debian

         .. code-block:: sh

            $ apt update
            $ apt install zammad

      .. tab:: CentOS

         .. code-block:: sh

            # general
            $ yum install zammad

         Due to an `issue <https://github.com/crohr/pkgr/issues/165>`_ with
         packager.io on CentOS you'll need to correct file permissions for
         public files.

         .. code-block:: sh

            chmod -R 755 /opt/zammad/public/

      .. tab:: OpenSUSE / SLES

         .. code-block:: sh

            $ zypper ref
            $ zypper install zammad

.. include:: /install/includes/firewall-and-selinux.rst

.. include:: /install/includes/manage-services.rst

.. include:: /install/includes/next-steps.rst
