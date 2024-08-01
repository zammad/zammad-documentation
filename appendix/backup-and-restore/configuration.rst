Backup Configuration
********************

Before you can run either a backup or restoration, the scripts requires
to provide a configuration file. We're shipping a ``config.dist`` within the
``/opt/zammad/contrib/backup`` directory which you can simply rename.

To do so run the following commands as either ``root`` or ``zammad`` user.

.. code-block:: sh

   $ cd /opt/zammad/contrib/backup/
   $ mv config.dist config

Adjust the values according to your needs. See the explanation of each
parameter in the table below.

.. list-table::
  :widths: 15, 25, 60
  :header-rows: 1

  * - Parameter
    - Default
    - Description
  * - ``BACKUP_DIR``
    - ``/var/tmp/zammad_backup``
    - Location where the script writes the backup files to.

      The directory will be created if not existing. Make sure you have
      enough space because the script writes full dumps.
  * - ``HOLD_DAYS``
    - ``10``
    - Define how many days the backup script should keep old backups.
      This value contains a 60 minutes grace period (e.g. 10 days plus 1 hour)
      for safety reasons.

      Old backups are removed *before* creating the current backup.

      **Examples:**

      * ``1`` will keep backups of the last 25 hours
      * ``-1`` will remove all available backups (except the current one)
  * - ``FULL_FS_DUMP``
    - ``yes``
    - If set to ``yes``, the backup includes also application files.

      If set to ``no``, the backup only includes usage data.

      In any case, it includes the Zammad database and the attachments, if you
      :admin-docs:`stored them in the file system </settings/system/storage.html>`.

      If you are in doubt, set this to ``no``.
  * - ``DEBUG``
    - ``no``
    - Setting this option to ``yes`` will output useful debug messages.

      .. warning::

         This option potentially returns **sensitive** information to standard
         out! *Do not* use this option in productive environments or ensure
         to turn it *off after testing*.



After this you'll be ready to continue with either
:doc:`creating your first backup </appendix/backup-and-restore/backup>` or
:doc:`restoring an existing backup </appendix/backup-and-restore/backup>`.