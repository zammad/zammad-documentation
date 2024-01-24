Backup configuration
********************

Before you can run either a backup or restoration, the scripts requires you
to provide a configuration file. We're shipping a ``config.dist`` within the
``/opt/zammad/contrib/backup`` directory which you can simply rename.

To do so run the following commands as either ``root`` or ``zammad`` user.

.. code-block:: sh

   $ cd /opt/zammad/contrib/backup/
   $ mv config.dist config

If below default values are not working for you or your installation in general,
this is the best moment to adjust the configuration file as needed.

After this you'll be ready to continue with either
:doc:`creating your first backup </appendix/backup-and-restore/backup>` or
:doc:`restoring an existing backup </appendix/backup-and-restore/backup>`.

``BACKUP_DIR``
   Default: ``/var/tmp/zammad_backup``

   Tell the backup script where to write your backup files to.

   Ensure that the user you're going to use for backing up Zammad
   (either ``root`` or ``zammad`` by default) has enough permissions
   to write into the target directory structure.

   In case the directory is not available yet, the backup script will attempt
   to create the directory.

   Make also sure to have enough space available on the backup location.
   Zammad always creates full backups. While we do compress backups,
   expect worst case ratios of 1 (no compression at all) depending
   on your attachments!

``HOLD_DAYS``
   Default: ``10``

   How many days should the backup script keep old backups?
   This value contains 60 minutes grace period (so e.g. 10 days plus 1 hour)
   for safety reasons.

   Old backups are removed *before* creating the actual (current) backup.

   **Example:**

   * ``0`` will keep the last 25 hours worth of backup
   * ``-1`` will always remove all available backups
     (aka only keep current backup)

``FULL_FS_DUMP``
   Default: ``yes`` (accepts: ``yes`` or ``no``)

   Setting this option to ``no`` allows you to only backup usage data without
   any environmental files from your old host. This allows you to backup your
   Zammad database together with the attachments you've stored within the file
   system.

   Please refer :admin-docs:`Storage Settings </settings/system/storage.html>`
   to learn how to change the storage location of your attachments.

   If you can't decide, our clear suggestion is setting this to ``no``.

``DEBUG``
   Default: ``no`` (accepts: ``yes`` or ``no``)

   Having issues and want to fiddle around? Setting this option to ``yes`` may
   help you with this. It contains useful debug messages at strategic points.

   .. warning::

      This option potentially returns **sensitive** information to standard
      out! *Do not* use this option in productive environments or ensure
      to turn it *off after testing*.
