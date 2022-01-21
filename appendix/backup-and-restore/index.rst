Backup and Restore
******************

Zammad comes with a collection of scripts for easy backup & restore for default
installations. These scripts are located within ``/opt/zammad/contrib/backup``.

.. note:: **⚖️ Important things to note before hand**

   These scripts do not come with any warranty and may not work in your
   specific use case. This depends on the configuration and installation type
   of your instance.

   You should always regularly test and review the functionality!
   If the script functionality or scope is not working for your cases,
   feel free to copy these to a independent location and adjust the scripts
   as needed.

Getting Started
===============

.. toctree::
   :hidden:

   configuration
   backup
   restore
   troubleshooting
   little-helpers

Before you continue, please also note the listed limitations to save your
precious time.

:doc:`🔨 Adjust script settings </appendix/backup-and-restore/configuration>`
   Learn more about configuration options for backup and restore to see
   scopes better.

:doc:`🗃️ Create Backups </appendix/backup-and-restore/backup>`
   How to create full dumps of your Zammad installation.

:doc:`🗄️ Restore Backups </appendix/backup-and-restore/restore>`
   Update went berserk and you need to go back? How to restore your instance on
   a new or the same host.

:doc:`🔥 Troubleshooting </appendix/backup-and-restore/troubleshooting>`
   Things hit the fan? This page might help you out of that pit.

:doc:`🤝 Helper scripts </appendix/backup-and-restore/little-helpers>`
   These scripts may be helpful if Backup & Restore does not work as expected.
   However note that these are potentially destructive.

Limitations
===========

Please note the following limitations which may affect script functionality
or availability.

   * Restoration via script on docker based installations may not work and
     is out of scope of this documentation as of now
   * Backup & Restore is only available for PostgreSQL and MySQL / MariaDB like
     installations
   * Switching / Converting database installations *is not* possible

        .. note::

           If you require support with migrating your MySQL / MariaDB installation
           into a PostgreSQL installation, you can contact `Zammads sales team`_
           for commercial support.

   * Starting with Zammad 5.0 the scripts *require* user & password
     authentication. This is supported by most of our installation types
   * Backup & Restore is always a full dump of everything (no incrementals)
   * Restoring or backing up specific information (e.g. Tickets, Users, ...)
     is not supported
   * Environmental settings (like e.g. :doc:`/appendix/configure-env-vars`) are
     not backed up and thus require you to manually set them on a new host
   * Restoration into a *older* Zammad version is not possible nor supported
   * *Do not* attempt to restore backup files from custom scripts with the
     provided scripts by Zammad. This is most likely subject to fail or bring
     issues you may discover too late.

.. _Zammads sales team: https://zammad.com/en/company/contact
