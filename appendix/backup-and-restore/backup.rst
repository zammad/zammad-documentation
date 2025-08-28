Create Backup
*************

Preparation
===========

Before running your first backup, please have a look at the
:doc:`/appendix/backup-and-restore/configuration` to set it up correctly.

Backup
======

It is recommended to stop Zammad before running the backup.

To create a backup, execute the script ``zammad_backup.sh`` as ``root``
or ``zammad`` user:

.. code-block:: console

   $ /opt/zammad/contrib/backup/zammad_backup.sh

Please make sure to test the backup function manually with the user
you're planning to backup first. This ensures that your backup really
is running as expected.

The backup process should look like this one:

.. code-block:: console

   # Zammad backup started - Fri Jan 21 17:53:44 CET 2022!

   creating file backup...
    ... as full dump
   creating postgresql backup...
   Ensuring dump permissions ...

   # Zammad backuped successfully - Fri Jan 21 17:53:57 CET 2022!

If you are facing issues while backing up your data, you can have a look at
the :doc:`troubleshooting section </appendix/backup-and-restore/troubleshooting>`
to read about common issues.
