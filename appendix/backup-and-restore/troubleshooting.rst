Troubleshooting Backup & Restore
********************************

You can find some common problems below. If your issue is not listed, feel
free to consult the
`Zammad Community <https://community.zammad.org/c/trouble-running-zammad-this-is-your-place/5>`_
for technical assistance.

Exit Codes
==========

Our backup & restore scripts come with exit codes to help you finding a
solution. However, we do not guarantee a complete error handling.

Beside the exit codes, there are also error messages returned to standard out.

.. list-table::
   :widths: 10 80
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
       requirements, login data being invalid or "broken‟ database dumps.
   * - ``3``
     - There were issues with file / folder permissions.

Common Problems
===============

``password authentication failed`` or ``peer authentication failed``
   This indicates that the password of your Zammad DB user is either different
   from your ``database.yml`` or the wrong database server may be contacted.

   If your Zammad instance is running, it can be caused by falling back to
   socket connection which is why you didn't notice.

   **What to do?**

   Ensure that the provided user credentials are correct. You can also
   consider to use the :ref:`reset_db_password` script, you can find in the
   backup directory.

``Ident authentication failed for user``
   This indicates your database server does require ``ident`` authentication.
   That authentication method is not supported by our scripts.

   **What to do?**


   Check the ``pg_hba.conf`` of your PostgreSQL-Server and adjust it if needed.

   Usually, authentication can be allowed like this:

   Adjust the example to your needs:

   .. code-block:: text

      host    all             all             127.0.0.1/32            md5
      host    all             all             ::1/128                 md5

   Please consult the official `PostgreSQL documentation`_ for this, as this
   is out of our documentation scope.

.. _PostgreSQL documentation: https://www.postgresql.org/docs/

``WARNING: You don't seem to have any attachments in the file system!``
   This indicate that your instance currently does not save attachments to
   file system.

   This warning will be shown once before creating an empty directory to allow
   the backup process to continue successfully.

   Read more how to check and adjust the
   :admin-docs:`storage settings </settings/system/storage.html>`.

