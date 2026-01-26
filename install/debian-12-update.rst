:orphan:

Update Instructions Debian 12 > 13
==================================

In case you want to update Debian 12 to Debian 13 on Zammad's host machine,
you need to take additional steps due to changes in the package hosting.
In case you just want to install Zammad on Debian 13, please follow the
instructions in :doc:`package`.

.. warning::

   - Debian 13 is supported starting with Zammad 7.
   - The steps below are to give you an orientation about the basic steps for an
     update process of a standard Debian 12 system. You should first and
     foremost follow Debian's official update instructions.

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

Update Debian
-------------

Follow Debian's
`instructions to update your system from Debian 12 to Debian 13 <https://www.debian.org/releases/trixie/release-notes/upgrading.en.html>`_.

- Add new sources in /etc/apt/sources.list.d/debian.sources
- Remove /etc/apt/sources.list & /etc/apt/sources.list.d/zammad.list 
- Update Debian with apt update & apt full-upgrade
- Don't update PostgreSQL
- Apt autoremove
- Reboot

Add New Zammad Repository
-------------------------

After updating your Debian system, you need to switch to the new Zammad
repository. Follow the installation guide.

