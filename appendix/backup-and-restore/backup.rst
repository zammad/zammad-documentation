Create Backup
*************

.. code-block:: sh

   # Zammad backup started - Fri Jan 21 17:53:44 CET 2022!

   creating file backup...
    ... as full dump
   creating postgresql backup...
   Ensuring dump permissions ...

   # Zammad backuped successfully - Fri Jan 21 17:53:57 CET 2022!

*Sample backup process with default*
:doc:`settings </appendix/backup-and-restore/configuration>`.

--------------------------------------------------------------------------------

.. note::

   🤓 Before running your first backup, please have a look at
   :doc:`/appendix/backup-and-restore/configuration`.

In general, running a Zammad backup is as simple as running

.. code-block:: sh

   $ /opt/zammad/contrib/backup/zammad_backup.sh

Please make sure to test the backup function manually with the user
you're planning the backup first. This ensures that your backup really
is running as expected.

Remarks
   | The backup script can be either run as ``zammad`` or ``root`` user.
   | Stopping Zammad is not required technically, but may be in your use case!
     (Keep in mind that a running Zammad instance keeps changing data which may
     be an issue during long backup runs)


.. hint::

   **😖 Having trouble backing up?**

   Have a look at the
   :doc:`troubleshooting section </appendix/backup-and-restore/troubleshooting>`
   to address your issues.
