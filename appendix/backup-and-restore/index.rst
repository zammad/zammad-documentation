Backup and Restore
******************

.. toctree::
   :hidden:

   configuration
   backup
   restore
   migrate-hosts
   troubleshooting
   little-helpers

Zammad ships scripts for backup & restore in package installations which you
can use for your backup strategy.

.. warning::

   These scripts do not come with any warranty and may not work in your
   specific use case. This depends on the configuration and installation type
   of your instance.

   You should always regularly test and review the functionality!
   If the script functionality or scope is not working for your cases,
   feel free to copy these to a independent location and adjust the scripts
   as needed.

Getting Started
===============

These scripts are located in ``/opt/zammad/contrib/backup``. The following files
might be important for you:

- Backup configuration file: ``config.dist``
- Script for backing up your data: ``zammad_backup.sh``
- Script for restoring your data: ``zammad_restore.sh``

Head over to the next section for a simple backup configuration. In
:ref:`advanced_backup`, you can find links to sub pages with a more
detailed explanation of the scripts.

Basic Backup Setup
------------------

#. Rename/copy the ``config.dist`` file to ``config``.
#. Change default parameters in  the ``config`` file if needed. Learn more
   about the configuration options
   :doc:`here </appendix/backup-and-restore/configuration>`.
#. Execute ``/opt/zammad/contrib/backup/zammad_backup.sh``.


.. _advanced_backup:

Advanced Setup and Restore
--------------------------

:doc:`Adjust script settings </appendix/backup-and-restore/configuration>`
   Learn more about configuration options for backup and restore to see
   scopes better.

:doc:`Create Backups </appendix/backup-and-restore/backup>`
   How to create full dumps of your Zammad installation.

:doc:`Restore Backups </appendix/backup-and-restore/restore>`
   Update went wrong and you need to go back? How to restore your instance on
   a new or the same host.

Additional Information
----------------------

:doc:`Migrating to new hosts </appendix/backup-and-restore/migrate-hosts>`
   This is a general summary on how to best migrate Zammad from host to host.
   We'll reference to backup creation and restoration as needed.

:doc:`Troubleshooting </appendix/backup-and-restore/troubleshooting>`
   Things hit the fan? This page might help you out of that pit.

:doc:`Helper scripts </appendix/backup-and-restore/little-helpers>`
   These scripts may be helpful if Backup & Restore does not work as expected.
   However note that these are potentially destructive.

Limitations
===========

Please note the following limitations which may affect script functionality
or availability:

   * These scripts won't work on container and source code based installations.
   * It only works for PostgreSQL installations.
   * The backup is always a full dump (no incremental backup).
   * Partial backup and restore (e.g. only specific data like tickets, users)
     is not possible.
   * Switching database system **is not** possible. See
     :doc:`here </appendix/migrate-to-postgresql>` how to manually switch
     databases.
   * System settings (like
     :doc:`environment variables </appendix/configure-env-vars>`) are
     not backed up.
   * Restore to an older Zammad version is not possible.
   * **Do not** restore backup files from custom scripts with the
     provided scripts by Zammad. This might cause problems.

