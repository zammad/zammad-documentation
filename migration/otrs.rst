Migration from OTRS
===================

Limitations
-----------

Please note below OTRS specific limitations.
These are additional limitations to the :ref:`general ones listed <migration_limitations>`.

   * Password migration works for OTRS >= 3.3 only (on older instances, a
     password reset within Zammad will be required)
   * If you plan to import a differential migration after,
     do not change any data in Zammad!
   * Only customers of tickets are imported
   * Zammad expects your OTRS timestamps to be UTC and won't adjust them
   * If you plan to import a differential after, **do not** change any data in Zammad!

   .. note::

      Supported OTRS versions: **3.1** up to **6.x**

Prerequisites
-------------

Step 1: Install Znuny4OTRS-Repo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a dependency of the OTRS migration plugin. Install the version that
matches your OTRS version:

- `OTRS 6 repository <https://ftp.zammad.com/otrs-migrator-plugins/Znuny4OTRS-Repo-6.0.76.opm>`_
- `OTRS 5 repository <https://ftp.zammad.com/otrs-migrator-plugins/Znuny4OTRS-Repo-5.0.56.opm>`_
- `OTRS 4 repository <https://ftp.zammad.com/otrs-migrator-plugins/Znuny4OTRS-Repo-4.0.25.opm>`_
- `OTRS 3 repository <https://ftp.zammad.com/otrs-migrator-plugins/Znuny4OTRS-Repo-3.3.2.opm>`_

Step 2: Install OTRS Migration Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the version that matches your OTRS version:

- `OTRS 6 plugin <https://ftp.zammad.com/otrs-migrator-plugins/Znuny4OTRS-ZammadMigrator-6.0.7.opm>`_
- `OTRS 5 plugin <https://ftp.zammad.com/otrs-migrator-plugins/Znuny4OTRS-ZammadMigrator-5.0.4.opm>`_
- `OTRS 4 plugin <https://ftp.zammad.com/otrs-migrator-plugins/Znuny4OTRS-ZammadMigrator-4.1.12.opm>`_
- `OTRS 3 plugin <https://ftp.zammad.com/otrs-migrator-plugins/Znuny4OTRS-ZammadMigrator-3.0.33.opm>`_

.. hint::

   In some cases restarting your webserver may help to solve internal server errors.

Importing OTRS Data
-------------------

.. tabs::

   .. tab:: Via browser

      .. note::

         If your OTRS installation is rather huge, you might want to consider
         using the command line version of this feature. This also applies if
         you experience timeouts during the migration or if you want to
         re-import again.

      After installing Zammad and configuring your
      :doc:`webserver </getting-started/configure-webserver>`, navigate to your
      Zammad's FQDN in your Browser and follow the migration wizard.

      Depending on the size of your OTRS installation this may take a while.
      You can get an idea of this process in the
      `migrator video on vimeo <https://vimeo.com/187752786>`_ .

   .. tab:: Via console

      .. include:: /migration/includes/rails-console-migrator-hint.include.rst

      Set import mode
         Stop all internal Zammad processes and set Zammad to import mode (no
         events are fired, e.g. notifications, sending emails, etc.).

         .. code-block:: irb

            >> Setting.set('import_mode', true)

      Start the migration
         Ensure to replace the values in ``{}`` brackets with your values.

         .. code-block:: irb

            >> Setting.set('import_otrs_endpoint', 'https://{your instance}/otrs/public.pl?Action=ZammadMigrator')

         .. code-block:: irb

            >> Setting.set('import_otrs_endpoint_key', '{xxx}')

         .. code-block:: irb

            >> Import::OTRS.start

      .. include:: /migration/includes/commands-after-migration.include.rst

After successfully migrating your OTRS installation, continue with :doc:`/getting-started/first-steps`.

Importing a Differential
------------------------

.. note::

   This is only possible after finishing an earlier OTRS import successfully.

In some cases it might be desirable to update the already imported data from OTRS.
This is possible with the following commands.

Run a differential import
   Ensure to replace the values in ``{}`` brackets with your values.

   .. code-block:: irb

      >> Setting.set('import_otrs_endpoint', 'http://{your instance}/otrs/public.pl?Action=ZammadMigrator')

   .. code-block:: irb

      >> Setting.set('import_otrs_endpoint_key', '{xxx}')

   .. code-block:: irb

      >> Setting.set('import_mode', true)

   .. code-block:: irb

      >> Setting.set('system_init_done', false)

   .. code-block:: irb

      >> Import::OTRS.diff_worker

.. include:: /migration/includes/commands-after-migration.include.rst

All changes that occurred after your first migration should now also be available
within your Zammad installation.

.. include:: /migration/includes/restarting-from-scratch.include.rst
