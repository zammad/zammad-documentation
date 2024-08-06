Restore
*******

Important Information
=====================

.. _restore_zammad:

Please read the following information carefully before starting to restore
your data.

- This section is **not** about **migrating from one host to another**.
  You can find instructions about this topic
  :doc:`here </appendix/backup-and-restore/migrate-hosts>`.
- This documentation page expects a fully installed Zammad version
- It also expects you to restore Zammad on the same host and Zammad version
- The restoration process **stops & restarts** Zammad. Therefore you have to
  run the restore script with appropriate permissions (e.g. as ``root``).

   * This is **mandatory** for *package installations*
   * On *source code installations*, this does not work because of different
     environments. You could load it beforehand as root user to have
     access to Zammad specific commands.
   * If both approaches above do not fit your case, consider
     adjusting the backup and restore scripts to your need in an
     independent directory. You're working out of script and
     documentation scope!

* PostgreSQL based installations will drop and re-create the database!
  MySQL / MariaDB based installations restore on the existing database.
* You require at least twice the backed up Zammad instance size of free
  storage. If you have the dump only, factor 3 could be a good number.

Restore
=======

Step 1: Copy your backup files to a fitting location (if needed)
   Ensure that the user you're using for restoration is allowed to read
   the backup files - writing is required for ``/opt/zammad/``.

   The Zammad backup consists of two files. They are named like this:

   .. code-block:: sh

      <timestamp>_zammad_db.psql.gz
      <timestamp>_zammad_files.tar.gz

   There are also two symlinks in your backup directory pointing to the
   newest backup created.

   .. code-block:: sh

      latest_zammad_db.psql.gz
      latest_zammad_files.tar.gz

Step 2: Configure the backup script (if needed)
   On new installation this is required. At least you have to provide a directory
   where your backups are stored.
   Please consult :doc:`/appendix/backup-and-restore/configuration` for more
   information.

Step 3: Run the restore
   .. include:: /appendix/backup-and-restore/restore-warning-old-dumps.include.rst

   Restoration works in two possible ways, depending on how interactive
   you want to go.

   .. tabs::

      .. tab:: Interactive restoration (recommended)

         .. code-block:: sh

            $ /opt/zammad/contrib/backup/zammad_restore.sh

         Provide the requested information to the script and wait for the
         restore process to finish. Depending on the size of your backup and
         host performance, this may take some time.

      .. tab:: Non-interactive restoration

         .. warning::

            Only use the following option if you know what you're doing!
            The following command will overwrite existing data without further
            prompts!

         .. code-block:: sh

            # When called with a timestamp argument (matching the backups filename),
            # Zammad will proceed immediately to restoring the specified backup.
            $ /opt/zammad/contrib/backup/zammad_restore.sh 20170507121848

   The restore operation should look like this:

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

Step 4: Re-install Zammad if restoring a full filesystem restore
   The backup script optionally back up the whole filesystem of Zammad.

   If your filesystem dump contains attachments only (the tar will contain
   a ``storage`` folder *only*) skip this step!

   For a better overview, please see:
   :doc:`step 9 of our migration path </appendix/backup-and-restore/migrate-hosts>`.

Step 5: Apply missing environmental settings
   .. include:: /appendix/backup-and-restore/add-missing-environment.include.rst

If you are facing issues, consider reading our
:doc:`troubleshooting section </appendix/backup-and-restore/troubleshooting>`.