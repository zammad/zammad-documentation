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

   .. group-tab:: Ubuntu

      .. code-block:: console

         $ sudo apt install curl apt-transport-https gnupg

   .. group-tab:: Debian

      .. code-block:: console

         $ sudo apt install curl apt-transport-https gnupg

   .. group-tab:: OpenSUSE / SLES

      OpenSUSE doesn't require any additional steps here!

      SLES 15 requires additional repositories to be
      activated. To do so, run the following commands.

      .. code-block:: console

         $ sudo SUSEConnect --product sle-module-desktop-applications/$(. /etc/os-release; echo $VERSION_ID)/$(uname -i)

      .. code-block:: console

         $ sudo SUSEConnect --product PackageHub/$(. /etc/os-release; echo $VERSION_ID)/$(uname -i)

   .. group-tab:: CentOS / RHEL

      .. code-block:: console

         $ sudo yum install wget epel-release

2. Install Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^

Elasticsearch is not a hard dependency of Zammad, but strongly recommended! It
needs to be installed before Zammad. Read on in the
:doc:`Elasticsearch section </install/elasticsearch>` first and continue
with the next step after you finished the installation of it.

3. Ensure Correct Locale
^^^^^^^^^^^^^^^^^^^^^^^^

To make Zammad work correctly, your system has to use the correct locales.

.. tabs::

   .. group-tab:: Ubuntu

      List your current locale settings:

      .. code-block:: console

         $ locale | grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: console

         $ sudo apt install locales

      .. code-block:: console

         $ sudo locale-gen en_US.UTF-8

      .. code-block:: console

         $ echo "LANG=en_US.UTF-8" > sudo /etc/default/locale

      After fixing it, make sure to check the output again for including
      ``<lang_code>.utf8``. A reboot may help if unsuccessful.

   .. group-tab:: Debian

      List your current locale settings:

      .. code-block:: console

         $ locale | grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: console

         $ sudo apt install locales

      .. code-block:: console

         $ sudo locale-gen en_US.UTF-8

      .. code-block:: console

         $ echo "LANG=en_US.UTF-8" > sudo /etc/default/locale

      After fixing it, make sure to check the output again for including
      ``<lang_code>.utf8``. A reboot may help if unsuccessful.

   .. group-tab:: OpenSUSE / SLES

      List your current locale settings:

      .. code-block:: console

         $ localectl status | grep LANG

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: console

         $ sudo localectl set-locale LANG=en_US.UTF-8

      After fixing it, make sure to check the output again for including
      ``<lang_code>.utf8``. A reboot may help if unsuccessful.

      .. hint::

         By default OpenSUSE uses ``POSIX`` as ``LANG`` value for the root
         user. Learn more about this within the `OpenSUSE documentation
         <https://doc.opensuse.org/documentation/leap/startup/html/book-opensuse-startup/cha-yast-lang.html#pro-yast-lang-additional>`_.

         This does not affect other users and thus can be ignored.

   .. group-tab:: CentOS / RHEL

      List your current locale settings:

      .. code-block:: console

         $ locale | grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: console

         $ sudo localectl set-locale LANG=en_US.UTF-8

      After fixing it, make sure to check the output again for including
      ``<lang_code>.utf8``. A reboot may help if unsuccessful.

Add Repository and Install Zammad
---------------------------------

.. hint:: Packager.io may not be accessible from IPv6-only environments, so make
   sure to consider this when performing the steps below.

Add Repository
^^^^^^^^^^^^^^

.. repo-start:

.. tabs::

   .. group-tab:: Ubuntu

      Add Repository Key
         .. code-block:: console

            $ sudo curl -fsSL "https://go.packager.io/srv/deb/zammad/zammad/gpg-key.gpg" \
                -o /usr/share/keyrings/zammad.gpg && sudo chmod 644 /usr/share/keyrings/zammad.gpg

      Ubuntu 22.04
         .. code-block:: console

            $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable/installer/ubuntu/22.04.list" \
                -o /etc/apt/sources.list.d/zammad.list

      Ubuntu 24.04
         .. code-block:: console

            $ sudo curl -fsSL  "https://go.packager.io/srv/zammad/zammad/stable/installer/ubuntu/24.04.list" \
                -o /etc/apt/sources.list.d/zammad.list

   .. group-tab:: Debian

      Add Repository Key
         .. code-block:: console

            $ sudo curl -fsSL "https://go.packager.io/srv/deb/zammad/zammad/gpg-key.gpg" \
                -o /usr/share/keyrings/zammad.gpg && sudo chmod 644 /usr/share/keyrings/zammad.gpg

      Add Repository (Debian 11)
         .. code-block:: console

            $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable/installer/debian/11.list" \
                -o /etc/apt/sources.list.d/zammad.list

      Add Repository (Debian 12)
         .. code-block:: console

            $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable/installer/debian/12.list" \
                -o /etc/apt/sources.list.d/zammad.list

      Add Repository (Debian 13)
         .. code-block:: console

            $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable/installer/debian/13.list" \
                -o /etc/apt/sources.list.d/zammad.list

   .. group-tab:: OpenSUSE / SLES

      openSUSE 15.x / SLES 15
         .. code-block:: console

            $ sudo curl -o /etc/zypp/repos.d/zammad.repo \
                "https://go.packager.io/srv/zammad/zammad/stable/installer/sles/15.repo"

   .. group-tab:: CentOS / RHEL

      Add Repository Key
         .. code-block:: console

            $ sudo rpm --import https://go.packager.io/srv/rpm/zammad/zammad/gpg-key.asc

      CentOS 9 / RHEL 9
         .. code-block:: console

            $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable/installer/el/9.repo" \
                -o /etc/yum.repos.d/zammad.repo

.. repo-end:

Install Zammad
^^^^^^^^^^^^^^

.. tabs::

   .. group-tab:: Ubuntu

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install zammad

   .. group-tab:: Debian

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install zammad

   .. group-tab:: OpenSUSE / SLES

      .. code-block:: console

         $ sudo zypper refresh

      .. code-block:: console

         $ sudo zypper install zammad

   .. group-tab:: CentOS / RHEL

      .. code-block:: console

         $ sudo dnf update

      .. code-block:: console

         $ sudo dnf install zammad

Firewall & SELinux
------------------

Some parts of these steps may not apply to you, feel free to skip them!

SELinux
^^^^^^^
.. note::
   The commands below only work on Ubuntu, Debian and CentOS. If you use a
   different distribution, please have a look at their documentation.

Allow Nginx or Apache to access public files of Zammad and communicate:

.. code-block:: console

   $ sudo chcon -Rv --type=httpd_sys_content_t /opt/zammad/public/

.. code-block:: console

   $ sudo setsebool httpd_can_network_connect on -P

.. code-block:: console

   $ sudo semanage fcontext -a -t httpd_sys_content_t /opt/zammad/public/

.. code-block:: console

   $ sudo restorecon -Rv /opt/zammad/public/

.. code-block:: console

   $ sudo chmod -R a+r /opt/zammad/public/

Firewall
^^^^^^^^

Ensure to open ports ``80`` and ``443`` (TCP & UDP) beside of the ports you
need. Below you can find a few examples for different distributions.
If you are using a different distribution, please have a look at their
documentation.

Please note that the examples below only cover the distribution's default
firewall. It may not cover your case.

.. tabs::

   .. group-tab:: Ubuntu

      Open Port 80 and 443 on your Firewall:

      .. code-block:: console

         $ sudo ufw allow 80

      .. code-block:: console

         $ sudo ufw allow 443

      .. code-block:: console

         $ sudo ufw reload

   .. group-tab:: Debian

      .. warning::

         We're covering ``nftables`` in this part - iptables is discouraged
         starting from Debian 10 (Buster).
         Our example uses the ``input`` chain, yours may be a different one!

      Add the following lines to ``/etc/nftables.conf`` or your specific rule
      file. Ensure to add these lines to your input-chain.

      Open Port 80 and 443 for Zammad:

      .. code-block::

         $ sudo tcp dport { http, https } accept

      .. code-block::

         $ sudo udp dport { http, https } accept

      The result should look like the following. Keep in mind that your
      environment could require different / more rules.

      .. code-block:: text

         #!/usr/local/sbin/nft -f
         flush ruleset

         table inet filter {
            chain input {
               type filter hook input priority 0; policy drop;
               ct state established,related accept
               tcp dport ssh log accept
               tcp dport { http, https } accept
               udp dport { http, https } accept
            }

            chain forward {
               type filter hook forward priority 0; policy accept;
            }

            chain output {
               type filter hook output priority 0; policy accept;
            }
         }

      To load your new rules, simply run ``sudo systemctl reload nftables``.

   .. group-tab:: OpenSUSE / SLES

      Open Port 80 and 443 on your Firewall:

      .. code-block:: console

         $ sudo firewall-cmd --zone=public --add-service=http --permanent

      .. code-block:: console

         $ sudo firewall-cmd --zone=public --add-service=https --permanent

      .. code-block:: console

         $ sudo firewall-cmd --reload

   .. group-tab:: CentOS / RHEL

      Open Port 80 and 443 on your Firewall:

      .. code-block:: console

         $ sudo firewall-cmd --zone=public --add-service=http --permanent

      .. code-block:: console

         $ sudo firewall-cmd --zone=public --add-service=https --permanent

      .. code-block:: console

         $ sudo firewall-cmd --reload

Manage Services of Zammad
-------------------------

Zammad uses three services. These services can be managed individually or all at
once by using the parent **zammad**.

- **zammad**: includes the services below

  - **zammad-web**: internal puma server (relevant for displaying the web app)
  - **zammad-worker**: background worker - relevant for all delayed- and background jobs
  - **zammad-websocket**: websocket server for session related information

Manage the services with ``systemctl``'s commands ``start``, ``restart``,
``stop``, ``status``. Example to start Zammad with all sub-services:

.. code-block:: console

   $ sudo systemctl start zammad

To stop or restart a service or to check its status, adjust the command as
mentioned above.

Next Steps
----------

With this Zammad technically is ready to go.
However, you'll need to follow the following further steps to access
Zammad's Web-UI and getting started with it.

   #. :ref:`Connect Zammad with Elasticsearch <configure_zammad_with_elasticsearch>`
   #. :doc:`/getting-started/configure-webserver`
   #. :doc:`/getting-started/first-steps`
   #. You may also find Zammad's :doc:`/admin/console` commands useful

If you expect usage with 5 agents or more you may also want to consider the
following pages.

   * :doc:`/appendix/environment-variables`
   * :doc:`/appendix/configure-database-server`

