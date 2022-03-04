Migration from OTRS
********************

Limitations
===========

Please note below OTRS specific limitations. 
These are additional limitations to the :ref:`general ones listed <migration_limitations>`.

   * | Password migration works for OTRS >= 3.3 only
     | (on older instances a password reset within Zammad will be required)
   * If you plan to import a differential migration after, 
     do not change any data in Zammad!
   * Only customers of tickets are imported
   * Zammad expects your OTRS timestamps to be UTC and won't adjust them
   * If you plan to import a differential after, **do not** change any data in Zammad!

   .. note::

      Supported OTRS version: **3.1** up to **6.x**

Prerequisites
=============

Step 1: Install Znuny4OTRS-Repo
--------------------------------

This is a dependency of the OTRS migration plugin.

.. tabs::

   .. tab:: OTRS 6

      .. code-block::

         https://addons.znuny.com/api/addon_repos/public/1029/latest

   .. tab:: OTRS 5

      .. code-block::

         https://addons.znuny.com/api/addon_repos/public/615/latest

   .. tab:: OTRS 4

      .. code-block::

         https://addons.znuny.com/api/addon_repos/public/309/latest

   .. tab:: OTRS 3

      .. code-block::

         https://addons.znuny.com/api/addon_repos/public/142/latest

Step 2: Install OTRS migration plugin
--------------------------------------

.. tabs::

   .. tab:: OTRS 6

      .. code-block::

         https://addons.znuny.com/api/addon_repos/public/1085/latest

   .. tab:: OTRS 5

      .. code-block::

         https://addons.znuny.com/api/addon_repos/public/617/latest

   .. tab:: OTRS 4

      .. code-block::

         https://addons.znuny.com/api/addon_repos/public/383/latest

   .. tab:: OTRS 3

      .. code-block::

         https://addons.znuny.com/api/addon_repos/public/287/latest

.. hint::

   In some cases restarting your webserver may help to solve internal server errors.

Importing OTRS data
===================

.. tabs::

   .. tab:: via Browser

      .. note:: 

         If your OTRS installation is rather huge, you might want to consider using 
         the command line version of this feature. This also applies if you 
         experience Timeouts during the migration.

      After installing Zammad and configuring your 
      :doc:`webserver </getting-started/configure-webserver>`, navigate to your 
      Zammads FQDN in your Browser and follow the migration wizard.

      Depending on the size of your OTRS installation this may take a while. 

      You can get an idea of this process in the 
      `migrator video on vimeo <https://vimeo.com/187752786>`_ .

   .. tab:: via Console

      .. include:: /migration/rails-console-migrator-hint.include.rst

      If you miss this at the beginning or you want to re-import again you have 
      to use the command line at the moment.

      Stop all Zammad processes and switch Zammad to import mode (no events are 
      fired - e. g. notifications, sending emails, ...)

      Start the migration
         Ensure to replace `xxx` with your values.

         .. code-block:: ruby

            >> Setting.set('import_otrs_endpoint', 'https://xxx/otrs/public.pl?Action=ZammadMigrator')
            >> Setting.set('import_otrs_endpoint_key', 'xxx')
            >> Setting.set('import_mode', true)
            >> Import::OTRS.start

      .. include:: /migration/includes/commands-after-migration.include.rst

After successfully migrating your OTRS installation, continue with :doc:`/getting-started/first-steps`.

Importing a differential
========================

.. note:: 

   This is only possible after finishing an earlier OTRS import **successful**. 

In some cases it might be desirable to update the already imported data from OTRS. 
This is possible with the following commands.

Run a differential import
   .. code-block:: ruby

      >> Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
      >> Setting.set('import_otrs_endpoint_key', 'xxx')
      >> Setting.set('import_mode', true)
      >> Setting.set('system_init_done', false)
      >> Import::OTRS.diff_worker

.. include:: /migration/includes/commands-after-migration.include.rst

All changes that occurred after your first migration should now also be available 
within your Zammad installation.

.. include:: /migration/restarting-from-scratch.include.rst
