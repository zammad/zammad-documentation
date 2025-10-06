From Zendesk
============

Limitations
-----------

Please note below Zendesk specific limitations.
These are additional limitations to the
:ref:`general ones listed <migration_limitations>`.

   * Differential migrations are **not** supported!
     The general suggestion is to run a test import before to learn
     how long the migration is going to take.
   * **Important:** Please note that migration speed highly depends on your
     Zendesk plan (API rate limits apply).
   * Your Zendesk plan has to provide API support. This may not apply to all
     available plans.
   * User passwords are not migrated and will require the user to use the
     :admin-docs:`password reset link </settings/security/base.html#lost-password>`
     on the login page.
   * Objects with cyrillic strings can't be migrated. Make sure to rename them
     before starting the migration.

Prerequisites
-------------

Zammad requires API access which is why you'll need to `create an API key`_
for the migration. The migrator will request your Zendesk-URL, email address and
API key.

.. warning::

  Ensure to retrieve the API key with a **full administrator** account.
  Less privileged users will end in a broken migration.

.. _create an API key:
  https://support.zendesk.com/hc/en-us/articles/4408889192858-Generating-a-new-API-token

Importing Zendesk Data
----------------------

Generally you have two options on how to migrate data.
If you have a fairly big instance with a lot of data, you may want to
consider using the console over the browser version.

.. tabs::

   .. tab:: Via browser

      After installing Zammad and configuring your
      :doc:`webserver </getting-started/configure-webserver>`, navigate to your
      Zammad's FQDN in your browser and follow the migration wizard.

      Depending on the number of users, tickets and Zendesk plan this may take
      some while.

      .. figure:: /images/migration/zendesk/import-via-ui.gif
         :alt: Migration process of Zendesk via UI

      .. note:: **😖 Scheduler got interrupted**

         .. figure:: /images/migration/zendesk/scheduler-interrupted.png

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

            >> subdomain = '{zendesk url}'

         .. code-block:: irb

            >> email = '{zendesk admin email address}'

         .. code-block:: irb

            >> token = '{zendesk token}'

         Update Zammad settings for Zendesk import:

         .. code-block:: irb

            >> Setting.set('import_zendesk_endpoint', "https://#{subdomain}/api/v2")

         .. code-block:: irb

            >> Setting.set('import_zendesk_endpoint_username', email)

         .. code-block:: irb

            >> Setting.set('import_zendesk_endpoint_key', token)

         .. code-block:: irb

            >> Setting.set('import_backend', 'zendesk')

         .. code-block:: irb

            >> Setting.set('import_mode', true)

      Dry run
         If you want to know if your configuration works in a dry run,
         run the following command:

         .. code-block:: irb

            >> Sequencer.process('Import::Zendesk::ConnectionTest')

      Start the migration
         To start the actual migration, run the following commands:

         .. code-block:: irb

            >> job = ImportJob.create(name: 'Import::Zendesk')

         .. code-block:: irb

            >> AsyncImportJob.perform_later(job)

      Check status
         Running the following command in a Rails console will provide
         detailed state information of your migration.

         .. code-block:: irb

            >> pp ImportJob.find_by(name: 'Import::Zendesk')

         To give you an idea how the migration job state looks like, you can
         use below tabs. As long as ``finished_at`` is ``nil``, the process
         is still running.

         .. tabs::

            .. tab:: Freshly started import

               .. code-block:: text
                  :class: no-copybutton

                  #<ImportJob:0x0000000008274310
                     id: 1,
                     name: "Import::Zendesk",
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
                  :class: no-copybutton

                  #<ImportJob:0x000055ba3d9dbbb8
                     id: 1,
                     name: "Import::Zendesk",
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
                  :class: no-copybutton

                  #<ImportJob:0x0000561da0def350
                     id: 1,
                     name: "Import::Zendesk",
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

After successfully migrating your Zendesk instance,
continue with :doc:`/getting-started/first-steps`.

.. include:: /migration/includes/restarting-from-scratch.include.rst
