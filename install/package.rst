Install from package
********************

.. note:: Please ensure to meet Zammads :doc:`/prerequisites/software` requirements before hand.

Prerequisites
=============

Additional software dependencies
--------------------------------

In addition to already mentioned :ref:`Package dependencies <package_dependencies>`, 
some operating systems may require additional packages if not already installed.

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh
      
         $ apt install wget apt-transport-https gnupg

   .. tab:: CentOS

      .. code-block:: sh

         $ yum install wget epel-release

.. include:: /install/includes/prerequisites.rst

Add Repository and install Zammad
=================================

.. hint:: 

   If you want to use MySQL instead of PostgreSQL, it's usually enough to have 
   the MySQL server installed on your system already. Some installation 
   managers can't differentiate and still install Zammad with PostgreSQL. In 
   that case, you'll have to adapt manually (out of scope of this documentation).

Add Repository
   .. tabs::

      .. tab:: Ubuntu

         Install Repository Key
            .. code-block:: sh

               $ wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -

         Ubuntu 16.04
            .. code-block:: sh

               $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/16.04.repo

         Ubuntu 18.04
            .. code-block:: sh

               $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/18.04.repo

         Ubuntu 20.04
            .. code-block:: sh

               $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/20.04.repo

      .. tab:: Debian

         Install Repository Key
            .. code-block:: sh

               $ wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -

         Debian 9
            .. code-block:: sh

               $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/debian/9.repo

         Debian 10
            .. code-block:: sh

               $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/debian/10.repo

      .. tab:: CentOS

         Install Repository Key
            .. code-block:: sh

               $ rpm --import https://dl.packager.io/srv/zammad/zammad/key

         RHEL 7 / CentOS 7
            .. code-block:: sh

               $ sudo wget -O /etc/yum.repos.d/zammad.repo \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/el/7.repo

         RHEL 8 / CentOS 8
            .. code-block:: sh

               $ sudo wget -O /etc/yum.repos.d/zammad.repo \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/el/8.repo

      .. tab:: OpenSUSE / SLES

         Install Repository Key
            .. code-block:: sh

               $ rpm --import https://dl.packager.io/srv/zammad/zammad/key

         SLES 12 / openSUSE 42.x
            .. code-block:: sh

               $ sudo wget -O /etc/zypp/repos.d/zammad.repo \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/sles/12.repo

Install Zammad
   .. tabs::

      .. tab:: Ubuntu / Debian

         .. code-block:: sh

            $ sudo apt-get update
            $ sudo apt-get install zammad

      .. tab:: CentOS

         .. code-block:: sh

            $ sudo yum install zammad

         Due to a `issue <https://github.com/crohr/pkgr/issues/165>`_ with 
         packager.io on CentOS 8 you'll need to correct file permissions for 
         public files.

         .. code-block:: sh

            chown -R 644 /opt/zammad/public/
            chmod -R +x /opt/zammad/public/

      .. tab:: OpenSUSE / SLES

         .. code-block:: sh
         
            $ sudo zypper ref
            $ sudo zypper install zammad

.. include:: /install/includes/firewall-and-selinux.rst

.. include:: /install/includes/manage-services.rst

.. include:: /install/includes/next-steps.rst
