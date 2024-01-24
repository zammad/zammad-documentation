Create Backup
*************

Preparation
===========

Before running your first backup, please have a look at the
:doc:`/appendix/backup-and-restore/configuration` to set it up correctly.

Backup
======

In general, running a Zammad backup is as simple as running:

.. code-block:: sh

   $ /opt/zammad/contrib/backup/zammad_backup.sh

Please make sure to test the backup function manually with the user
you're planning to backup first. This ensures that your backup really
is running as expected.

The backup process should look like this one:

.. code-block:: sh

   # Zammad backup started - Fri Jan 21 17:53:44 CET 2022!

   creating file backup...
    ... as full dump
   creating postgresql backup...
   Ensuring dump permissions ...

   # Zammad backuped successfully - Fri Jan 21 17:53:57 CET 2022!

*Sample backup process with default*
:doc:`settings </appendix/backup-and-restore/configuration>`.

Additional Information
======================

* The backup script can be either run as ``zammad`` or ``root`` user.
* Stopping Zammad is not required (but suggested) technically. It may be
  required in your case!
* Keep in mind that a running Zammad instance keeps changing data which may
  be an issue during long backup runs

.. hint::

   **😖 Having trouble backing up?**

   Have a look at the
   :doc:`troubleshooting section </appendix/backup-and-restore/troubleshooting>`
   to address your issues.
