Backup & Restore (Package)
==========================

Zammad ships scripts for backup & restore in package installations which you
can use in your backup strategy.

.. warning::

   These scripts do not come with any warranty and may not work in your
   specific use case. This depends on the configuration and installation type
   of your instance.

   You should always regularly test and review the functionality!
   If the script functionality or scope is not working for your cases,
   feel free to copy these to a independent location and adjust the scripts
   as needed.

Getting Started
---------------

These scripts are located in ``/opt/zammad/contrib/backup``. The following files
might be important for you:

- Backup configuration file: ``config.dist``
- Script for backing up your data: ``zammad_backup.sh``
- Script for restoring your data: ``zammad_restore.sh``

Head over to the next section for a simple backup configuration. In
:ref:`advanced_backup`, you can find links to sub pages with a more
detailed explanation of the scripts.

Basic Backup Setup
^^^^^^^^^^^^^^^^^^

#. Rename/copy the ``config.dist`` file to ``config``.
#. Change default parameters in  the ``config`` file if needed. Learn more
   about the configuration options
   :doc:`here </appendix/backup-and-restore/configuration>`.
#. Optional: install ``pigz`` - if installed, ``pigz`` will be used by the
   scripts. (see: `pig-zee <https://zlib.net/pigz/>`_)
#. Execute ``/opt/zammad/contrib/backup/zammad_backup.sh``.


.. _advanced_backup:

Advanced Setup and Restore
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :hidden:

   configuration
   backup
   restore
   migrate-hosts
   troubleshooting
   little-helpers

Adjust script settings
   Learn more about configuration options for backup and restore
   :doc:`here </appendix/backup-and-restore/configuration>`.

Create Backups
   Learn how to create full dumps of your Zammad installation
   :doc:`here </appendix/backup-and-restore/backup>`.

Restore Backups
   Learn how to restore your instance on the same host
   :doc:`here </appendix/backup-and-restore/restore>`.

Additional Information
^^^^^^^^^^^^^^^^^^^^^^

Migrating to a new host
   :doc:`Here </appendix/backup-and-restore/migrate-hosts>` you can read how to
   migrate Zammad from one host to another host.

Troubleshooting
   If something went wrong,
   :doc:`this page </appendix/backup-and-restore/troubleshooting>` might help
   you out.

Helper scripts
   Maybe this is helpful for you if backup & restore does not work as expected.
   See :doc:`here </appendix/backup-and-restore/little-helpers>` for more
   information.

Limitations
-----------

Please note the following limitations which may affect script functionality
or availability:

   * These scripts won't work in container and source code based installations.
   * They only work for PostgreSQL installations.
   * The backup is always a full dump (no incremental backup).
   * Partial backup and restore (e.g. only specific data like tickets, users)
     is not possible.
   * Switching database system **is not** possible. See
     :doc:`here </appendix/migrate-to-postgresql>` how to manually switch
     databases.
   * System settings (like
     :doc:`environment variables </appendix/environment-variables>`) are
     not backed up.
   * Restore to an older Zammad version is not possible.
   * **Do not** restore backup files from custom scripts with the
     provided scripts by Zammad. This might cause problems.


