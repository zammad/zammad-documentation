Install from package
********************

.. note::

   | Please ensure to meet Zammads :doc:`/prerequisites/software` requirements
     beforehand.
   | This page expects administrative permissions, this is why ``sudo`` is
     not used.

Prerequisites
=============

Additional software dependencies
--------------------------------

In addition to already mentioned :ref:`Package dependencies <package_dependencies>`,
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

.. include:: /install/includes/prerequisites.rst

Add Repository and install Zammad
=================================

.. hint:: Packager.io may not be accessible from IPv6-only environments, so make
   sure to consider this when performing the steps below.

Add Repository
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
