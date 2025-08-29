From Freshdesk
==============

Limitations
-----------

Please note below Freshdesk specific limitations.
These are additional limitations to the
:ref:`general ones listed <migration_limitations>`.

   * Differential migrations are **not** supported!
     The general suggestion is to run a test import before to learn
     how long the migration is going to take.
   * **Important:** Please note that migration speed highly depends on your
     Freshdesk plan (API rate limits apply).
   * Due to API limitations Zammad will not show the total number of objects
     to import, but instead correct them in steps of ``100``.
   * Your Freshdesk plan has to provide API support. This may not apply to all
     available plans.
   * User passwords are not migrated and will require the user to use the
     :admin-docs:`password reset link </settings/security/base.html#lost-password>`
     on the login page.

Prerequisites
-------------

Zammad requires API access which is why you'll need to `create an API key`_
for the migration. The migrator will request your Freshdesk subdomain and
API key.

.. warning::

  Ensure to retrieve the API key with a **full administrator** account.
  Less privileged users will end in a broken migration.

.. _create an API key:
  https://support.freshdesk.com/support/solutions/articles/215517-how-to-find-your-api-key

Importing Freshdesk Data
------------------------

Generally you have two options on how to migrate data.
If you have a fairly big instance with a lot of data, you may want to
consider using the console over the browser version.

.. tabs::

   .. tab:: Via browser

      After installing Zammad and configuring your
      :doc:`webserver </getting-started/configure-webserver>`, navigate to your
      Zammad's FQDN in your browser and follow the migration wizard.

      Depending on the number of users, tickets and Freshdesk plan, this may take
      some time.

      .. figure:: /images/migration/freshdesk/import-via-ui.gif
         :alt: Migration process of freshdesk via UI

      .. note:: **😖 Scheduler got interrupted**

         .. figure:: /images/migration/freshdesk/scheduler-interrupted.png

         If this message appears after providing your credentials, please be
         patient. The migration should start within 5 minutes.

         If you receive above message after the migration begun, please
         consider using the console approach instead and reset the
         installation.

   .. tab:: Via console

      .. include:: /migration/includes/rails-console-migrator-hint.include.rst

      Prepare the migration
         Set variables for easier configuration. Replace the values in ``{}``
         with your values:

         .. code-block:: irb

            >> subdomain = '{freshdesk subdomain}.freshdesk.com'

         .. code-block:: irb

            >> token = '{freshdesk token}'

         Update Zammad settings for freshdesk import:

         .. code-block:: irb

            >> Setting.set('import_freshdesk_endpoint', "https://#{subdomain}/api/v2")

         .. code-block:: irb

            >> Setting.set('import_freshdesk_endpoint_key', token)

         .. code-block:: irb

            >> Setting.set('import_backend', 'freshdesk')

         .. code-block:: irb

            >> Setting.set('import_mode', true)

      Dry run
         If you want to know if your configuration works in a dry run,
         run the following command:

         .. code-block:: irb

            >> Sequencer.process('Import::Freshdesk::ConnectionTest')

      Start the migration
         .. code-block:: irb

            >> job = ImportJob.create(name: 'Import::Freshdesk')

         .. code-block:: irb

            >> AsyncImportJob.perform_later(job)

      Check status
         Running the following command in a rails console will provide
         detailed state information of your migration.

         .. code-block:: irb

            >> pp ImportJob.find_by(name: 'Import::Freshdesk')

         To give you an idea how the migration job state looks like, you can
         use below tabs. As long as ``finished_at`` is ``nil``, the process is
         still running.

         .. tabs::

            .. tab:: Freshly started import

               .. code-block:: text

                  #<ImportJob:0x0000000008274310
                     id: 1,
                     name: "Import::Freshdesk",
                     dry_run: false,
                     payload: {},
                     result:
                     {"Organizations"=>
                        {"skipped"=>0,
                        "created"=>0,
                        "updated"=>0,
                        "unchanged"=>0,
                        "failed"=>0,
                        "deactivated"=>0,
                        "sum"=>0,
                        "total"=>100}},
                     started_at: Mon, 03 Jan 2022 18:41:51 UTC +00:00,
                     finished_at: nil,
                     created_at: Mon, 03 Jan 2022 18:41:16 UTC +00:00,
                     updated_at: Mon, 03 Jan 2022 18:43:32 UTC +00:00>

            .. tab:: Import half way

               .. code-block:: text

                  #<ImportJob:0x000055ba3d9dbbb8
                     id: 1,
                     name: "Import::Freshdesk",
                     dry_run: false,
                     payload: {},
                     result:
                     {"Groups"=>
                        {"skipped"=>0,
                        "created"=>3,
                        "updated"=>0,
                        "unchanged"=>0,
                        "failed"=>0,
                        "deactivated"=>0,
                        "sum"=>3,
                        "total"=>3},
                     "Organizations"=>
                        {"skipped"=>0,
                        "created"=>193,
                        "updated"=>1,
                        "unchanged"=>0,
                        "failed"=>0,
                        "deactivated"=>0,
                        "sum"=>194,
                        "total"=>194},
                     "Users"=>
                        {"skipped"=>0,
                        "created"=>3352,
                        "updated"=>0,
                        "unchanged"=>0,
                        "failed"=>0,
                        "deactivated"=>0,
                        "sum"=>3352,
                        "total"=>3352},
                     "Tickets"=>
                        {"skipped"=>0,
                        "created"=>987,
                        "updated"=>0,
                        "unchanged"=>0,
                        "failed"=>0,
                        "deactivated"=>0,
                        "sum"=>987,
                        "total"=>1000}},
                     started_at: Tue, 04 Jan 2022 11:37:38 UTC +00:00,
                     finished_at: nil,
                     created_at: Tue, 04 Jan 2022 11:37:36 UTC +00:00,
                     updated_at: Tue, 04 Jan 2022 12:12:52 UTC +00:00>

            .. tab:: Finished import

               .. code-block:: text

                  #<ImportJob:0x0000561da0def350
                     id: 1,
                     name: "Import::Freshdesk",
                     dry_run: false,
                     payload: {},
                     result:
                     {"Groups"=>
                        {"skipped"=>0,
                        "created"=>3,
                        "updated"=>0,
                        "unchanged"=>0,
                        "failed"=>0,
                        "deactivated"=>0,
                        "sum"=>3,
                        "total"=>3},
                     "Organizations"=>
                        {"skipped"=>0,
                        "created"=>193,
                        "updated"=>1,
                        "unchanged"=>0,
                        "failed"=>0,
                        "deactivated"=>0,
                        "sum"=>194,
                        "total"=>194},
                     "Users"=>
                        {"skipped"=>0,
                        "created"=>3352,
                        "updated"=>0,
                        "unchanged"=>0,
                        "failed"=>0,
                        "deactivated"=>0,
                        "sum"=>3352,
                        "total"=>3352},
                     "Tickets"=>
                        {"skipped"=>0,
                        "created"=>4714,
                        "updated"=>0,
                        "unchanged"=>0,
                        "failed"=>1,
                        "deactivated"=>0,
                        "sum"=>4715,
                        "total"=>4715}},
                     started_at: Tue, 04 Jan 2022 11:37:38 UTC +00:00,
                     finished_at: Tue, 04 Jan 2022 14:30:57 UTC +00:00,
                     created_at: Tue, 04 Jan 2022 11:37:36 UTC +00:00,
                     updated_at: Tue, 04 Jan 2022 14:30:57 UTC +00:00>

      .. include:: /migration/includes/commands-after-migration.include.rst

After Migration
---------------

As the migration technically skips the getting started wizard, please
note that you want to adjust your
:admin-docs:`FQDN settings </settings/system/base.html>` (FQDN & HTTP-Type).

.. include:: /migration/includes/how-to-login.include.rst

After successfully migrating your Freshdesk instance,
continue with :doc:`/getting-started/first-steps`.

.. include:: /migration/includes/restarting-from-scratch.include.rst
