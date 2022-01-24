Troubleshooting Backup & Restore
********************************

Errors have been made, possibly they can be corrected through.

Exit codes
==========

Backup & Restore script come with exit codes to help you within possible
autonomous handling. However, we do not guarantee a complete error handling.

Beside the exit codes, there's also error messages returned to standard out.

.. list-table:: Exit code list
   :widths: 25 75
   :header-rows: 1

   * - Code
     - Description / Situation
   * - ``0``
     - The script finished successfully (or the error is not handled).
   * - ``1``
     - This is a general error. Most often used for script aborts due to
       incorrect information provided or information missing.
   * - ``2``
     - There was an error with database handling.
       This usually either happens if your database server does not meet script
       requirements, login data being invalid or „broken‟ database dumps.
   * - ``3``
     - There were issues with file / folder permissions.

Classics
========

Here's some classics you may encounter.

.. hint:: **🥸 Your issue is not listed...?**

   Please consult the `Zammad Community`_ for technical assistance.

``password authentication failed`` -or- ``peer authentication failed``
   This indicates that the password of your Zammad DB user is either different
   from your ``database.yml`` or the wrong database server may be contacted.

   „But my Zammad instance is running, how can it be wrong?‟
      Zammad may fall back to socket connection which is why you didn't notice.

   What to do ...
      * Ensure that the provided user credentials are correct

           .. tip:: **🤓 Lazy users can use our helper**

              In the backup directory you'll find a :ref:`reset_db_password`.

``Ident authentication failed for user``
   This indicates your database server does require ``ident`` authentication.
   That authentication method is not supported by our scripts.

   What to do ...
      Check ``pg_hba.conf`` of your PostgreSQL-Server and adjust it if needed.

      Usually authentication can be allowed like so:

      .. code-block:: sh

         # THIS IS A SAMPLE AND MAY NOT FIT YOUR ENVIRONMENT
         host    all             all             127.0.0.1/32            md5
         host    all             all             ::1/128                 md5

      Please consult the offical `PostgreSQL documentation`_ for this, as this
      is out of our documentation scope.

.. _PostgreSQL documentation: https://www.postgresql.org/docs/

``WARNING: You don't seem to have any attachments in the file system!``
   This indicate you've set ``FULL_FS_DUMP`` to ``no`` but your instance
   currently does not save attachments to file system.

   This warning will be shown once before creating an empty directory to allow
   the backup process to continue successfully.

   If you believe that this is an error, please see `Storage Settings`_.
   In case the issue posts, please consult the `Zammad Community`_.

.. _Storage Settings:
   https://admin-docs.zammad.org/en/latest/settings/system/storage.html

.. _Zammad Community:
   https://community.zammad.org/c/trouble-running-zammad-this-is-your-place/5
