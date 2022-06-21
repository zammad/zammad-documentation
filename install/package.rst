Install from package
********************

.. note::

   | Please ensure to meet Zammads :doc:`/prerequisites/software` requirements
     before hand.
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

   .. tab:: CentOS

      .. code-block:: sh

         $ yum install wget epel-release

         # CentOS 7
         $ yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

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

               $ curl -fsSL https://dl.packager.io/srv/zammad/zammad/key | \
                 gpg --dearmor | tee /etc/apt/trusted.gpg.d/pkgr-zammad.gpg> /dev/null

            Ubuntu 16.04
               .. code-block:: sh

                  $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu 16.04 main"| \
                    tee /etc/apt/sources.list.d/zammad.list > /dev/null

            Ubuntu 18.04
               .. code-block:: sh

                  $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu 18.04 main"| \
                    tee /etc/apt/sources.list.d/zammad.list > /dev/null

            Ubuntu 20.04
               .. code-block:: sh

                  $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/ubuntu 20.04 main"| \
                    tee /etc/apt/sources.list.d/zammad.list > /dev/null

      .. tab:: Debian

         Install Repository Key
            .. code-block:: sh

               $ curl -fsSL https://dl.packager.io/srv/zammad/zammad/key | \
                 gpg --dearmor | tee /etc/apt/trusted.gpg.d/pkgr-zammad.gpg> /dev/null

            Debian 9
               .. code-block:: sh

                  $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/debian 9 main"| \
                    tee /etc/apt/sources.list.d/zammad.list > /dev/null

            Debian 10
               .. code-block:: sh

                  $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/debian 10 main"| \
                    tee /etc/apt/sources.list.d/zammad.list > /dev/null

            Debian 11
               .. code-block:: sh

                  $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/pkgr-zammad.gpg] https://dl.packager.io/srv/deb/zammad/zammad/stable/debian 11 main"| \
                    tee /etc/apt/sources.list.d/zammad.list > /dev/null

      .. tab:: CentOS

         Install Repository Key
            .. code-block:: sh

               $ rpm --import https://dl.packager.io/srv/zammad/zammad/key

            RHEL 7 / CentOS 7
               .. code-block:: sh

                  $ wget -O /etc/yum.repos.d/zammad.repo \
                  https://dl.packager.io/srv/zammad/zammad/stable/installer/el/7.repo

            RHEL 8 / CentOS 8
               .. code-block:: sh

                  $ wget -O /etc/yum.repos.d/zammad.repo \
                  https://dl.packager.io/srv/zammad/zammad/stable/installer/el/8.repo

      .. tab:: OpenSUSE / SLES

         Remove obsolete Let's Encrypt CA
            .. code-block:: sh

               $ rm /usr/share/pki/trust/DST_Root_CA_X3.pem
               $ update-ca-certificates

         Install Repository Key
            .. code-block:: sh

               $ rpm --import https://dl.packager.io/srv/zammad/zammad/key

         SLES 12 / openSUSE 42.x
            .. code-block:: sh

               $ wget -O /etc/zypp/repos.d/zammad.repo \
               https://dl.packager.io/srv/zammad/zammad/stable/installer/sles/12.repo

Install Zammad
   .. tabs::

      .. tab:: Ubuntu / Debian

         .. code-block:: sh

            $ apt update
            $ apt install zammad

      .. tab:: CentOS

         .. code-block:: sh

            # CentOS 7
            $ yum install postgresql14-server
            $ postgresql-14-setup initdb
            $ systemctl start postgresql-14
            $ systemctl enable postgresql-14

            # general
            $ yum install zammad

         Due to an `issue <https://github.com/crohr/pkgr/issues/165>`_ with
         packager.io on CentOS 8 you'll need to correct file permissions for
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
