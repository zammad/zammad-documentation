:orphan:

Update Instructions Debian 12 > 13
==================================

In case you want to update Debian 12 to Debian 13 on Zammad's host machine,
you need to take additional steps due to changes in the package hosting.
In case you just want to install (and not update) Zammad on Debian 13, please
follow the instructions in :doc:`package`.

.. warning::

   - Debian 13 is supported starting with Zammad 7.
   - The steps below are to give you an orientation about the basic steps for an
     update process of a standard Debian 12 system. You should first and
     foremost follow Debian's
     `official update instruction <https://www.debian.org/releases/trixie/release-notes/upgrading.en.html>`_.

Stop Zammad
-----------

First, stop the Zammad services to prevent any data changes during the update:

.. code-block:: console

   $ sudo systemctl stop zammad

Backup
------

Before you start, make sure to have a working backup of your Zammad
installation. Please refer to :doc:`/appendix/backup-and-restore/backup` for
more information.

Add New Sources
---------------

Debian 13
^^^^^^^^^

Add new sources to ``/etc/apt/sources.list.d/debian.sources``:

.. code-block:: console

   $ printf "Types: deb
   URIs: https://deb.debian.org/debian
   Suites: trixie trixie-updates
   Components: main non-free-firmware
   Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

   Types: deb
   URIs: https://security.debian.org/debian-security
   Suites: trixie-security
   Components: main non-free-firmware
   Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg"
   sudo tee /etc/apt/sources.list.d/debian.sources > /dev/null

Zammad
^^^^^^

Add repository key:

.. code-block:: console

   $ curl -fsSL https://go.packager.io/srv/deb/zammad/zammad/gpg-key.asc | \
      gpg --dearmor | sudo tee /usr/share/keyrings/zammad.gpg> /dev/null \
      && sudo chmod 644 /usr/share/keyrings/zammad.gpg

Add repository:

.. code-block:: console

   $ curl -fsSL https://go.packager.io/srv/zammad/zammad/stable/installer/debian/13.list \
   -o /etc/apt/sources.list.d/zammad.list

Remove Old Source
-----------------

Remove Debian 12 sources from ``/etc/apt/sources.list``:

.. code-block:: console

   $ sudo rm /etc/apt/sources.list

Remove Zammad sources from ``/etc/apt/sources.list.d/zammad.list``:

.. code-block:: console

   $ sudo rm /etc/apt/sources.list.d/zammad.list

Remove Zammad repository signing key:

.. code-block:: console

   $ sudo rm /etc/apt/keyrings/pkgr-zammad.gpg

Update
------

.. code-block:: console

   $ sudo apt update

.. code-block:: console

   $ sudo apt full-upgrade

.. code-block:: console

   $ sudo apt autoremove

Start Zammad
------------

In case Zammad does not start automatically, start the services manually:

.. code-block:: console

   $ sudo systemctl start zammad
