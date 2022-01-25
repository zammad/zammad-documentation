Restore
*******

.. code-block:: sh

   # Zammad restore started - Fri Jan 21 17:54:13 CET 2022!

   The restore will delete your current database!
   Be sure to have a backup available!

   Please ensure to have twice the storage of the uncompressed backup size!


   Note that the restoration USUALLY requires root permissions as services are stopped!


   Enter 'yes' if you want to proceed!
   Restore?: yes
   Enter file date to restore:
   20220120124714
   20220121175344
   File date: 20220121175344
   Enter db date to restore:
   20220120124714
   20220121175344
   DB date: 20220121175344
   # Stopping Zammad
   # Checking requirements
   # ... Dropping current database zammad
   Dropped database 'zammad'
   # ... Creating database zammad for owner zammad
   CREATE DATABASE
   # Restoring PostgreSQL DB
   # Restoring Files
   # Ensuring correct file permissions ...
   # Clearing Cache ...
   # Starting Zammad

   # Zammad restored successfully - Fri Jan 21 17:54:34 CET 2022!

*Sample backup process.*

--------------------------------------------------------------------------------

.. _restore_zammad:

.. hint:: **♻️ Migrating from host to host...?**

   Please refer :doc:`/appendix/backup-and-restore/migrate-hosts` for more
   additional information you may want to consider during a migration.

.. warning::

   | **This documentation page expects a fully installed Zammad version**.
   | It also expects you to restore Zammad on the same host and version!

Before restoring your backup, please note the following:

   * The restoration process **stops & restarts** the Zammad service.
     This means you usually have to run the restoration script as ``root`` user.

        .. note::

           - This is **mandatory** for package installations
           - On Source code installation this does not work because of different
             environments - you could load it before hand as root user to have
             access to Zammad specific commands.
           - If both approaches above do not fit for your case, consider
             adjusting the backup and restore scripts to your need in an
             independent directory. You're working out of script and
             documentation scope!

   * PostgreSQL based installations will drop and re-create the database!
     MySQL / MariaDB based installations restore on the existing database.
   * You require at least twice the backed up Zammad instance size of free
     storage. If you have the dump only, factor 3 *could* be a good number.

Step 1: Copy your backup files to a fitting location (if needed)
   This basically is a given usually if you run a normal restore.
   Ensure that the user you're using for restoration is allowed to read
   the backup files - writing is required for ``/opt/zammad/``.

      .. hint:: **🤔 So many files, what's my backup files?**

         The Zammad backup consists of two files. This is their format:

            .. code-block:: sh

               <timestamp>_zammad_db.psql.gz
               <timestamp>_zammad_files.tar.gz

         There's also two symlinks in your backup directory showing to the
         newest backup created.

Step 2: Configure the backup script (if needed)
   | On new installation it's required. For restoration this mainly affects the
     backup file location.
   | Please consult
     :doc:`/appendix/backup-and-restore/configuration` for more.

Step 3: Run the restore
   Restoration works via two possible ways, depending on how interactive
   you want to go.

   .. tabs::

      .. tab:: Interactive restoration (recommended)

         .. code-block:: sh

            $ /opt/zammad/contrib/backup/zammad_restore.sh

         Provide the requested information to the script wait for the
         restoration to finish. Depending on the size of your backup and
         host performance this may take some time.

      .. tab:: Non-interactive restoration

         .. warning::

            Only use the following option if you know what you're doing!
            The following command will overwrite existing data without further
            prompts!

         .. code-block:: sh

            # When called with a timestamp argument (matching the backups filename),
            # Zammad will proceed immediately to restoring the specified backup.
            $ /opt/zammad/contrib/backup/zammad_restore.sh 20170507121848

   .. hint::

      **😖 Having trouble restoring?**

      Have a look at the
      :doc:`troubleshooting section </appendix/backup-and-restore/troubleshooting>`
      to address your issues.

Step 4: Re-install Zammad if restoring a full filesystem restore
   Zammads backup scripts backup the whole filesystem of Zammad.
   This is mainly for backward compatibility but not a hard requirement.

   If your filesystem dump contains attachments only (the tar will contain
   a ``storage`` folder *only*) skip this step!

   For a better overview, please see: **XXXXX**.

Step 5: Apply missing environmental settings
   .. note::

      This does not apply to Docker images, as the following settings should
      be applied upon every start automatically.

   If you've set any environmental settings like higher web concurrency
   due to required :ref:`performance_tuning`, please re-apply your settings now.

   If not already done, please install Elasticsearch now (if you want to use it).
   Follow :ref:`configure_zammad_with_elasticsearch` to reconfigure your
   installation for Elasticsearch use and rebuild the search index.

You are now ready to continue your work.
The rebuild of your search index can safely run during your work, but will
cause a degraded search performance and may lead to temporarily not found
data.
