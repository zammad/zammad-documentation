From Freshdesk
**************

Limitations
===========

Please note below Freshdesk specific limitations. 
These are additional limitations to the
:ref:`general ones listed <migration_limitations>`.

   * | Differential migrations are **not** supported!
     | The general suggestion is to run a test import before to learn
       how long the migration is going to take.
   * **Important:** Please note that migration speed highly depends on your
     Freshdesk plan (API rate limits apply).
   * Due to API limitations Zammad will not show the total number of objects
     to import, but instead correct them in steps of ``100``.
   * User passwords are not migrated and will require the user to use the
     `password reset link`_ on the login page.

.. _password reset link:
   https://admin-docs.zammad.org/en/latest/settings/security/base.html#lost-password

   .. note::

      Your Freshdesk plan has to provide API support.
      This may not apply to all available plans.

Prerequisites
=============

Zammad requires API access which is why you'll need to `create an API key`_
for the migration. The migrator will request your Freshdesk subdomain and
API key.

.. warning:: **🥸 To be or not to be**

  Ensure to retrieve the API key with a **full administrator** account.
  Less privileged users will end in a broken migration.

.. _create an API key:
  https://support.freshdesk.com/support/solutions/articles/215517-how-to-find-your-api-key

Importing Freshdesk data
========================

Generally you have two options on how to migrate data.
If you have a fairly big instance with a lot of data, you may want to
consider using the console over the browser version.

.. tabs::

   .. tab:: Via browser

      After installing Zammad and configuring your 
      :doc:`webserver </getting-started/configure-webserver>`, navigate to your 
      Zammads FQDN in your browser and follow the migration wizard.

      Depending on the number of users, tickets and Freshdesk plan this may take
      some while.

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

      .. include:: /migration/rails-console-migrator-hint.include.rst

      To prepare the migration, run the following commands
         .. code-block:: ruby
            :force:

            # Set variables for easier settings
            $ subdomain = '{freshdesk subdomain}.freshdesk.com'
            $ token = '{freshdesk token}'

            # Update Zammad settings for freshdesk import
            $ Setting.set('import_freshdesk_endpoint', "https://#{subdomain}/api/v2")
            $ Setting.set('import_freshdesk_endpoint_key', token)
            $ Setting.set('import_backend', 'freshdesk')
            $ Setting.set('import_mode', true)


         .. hint::

            Want to know if your configuration works before hand?
            Run the following command:

            .. code-block:: ruby

               Sequencer.process('Import::Freshdesk::ConnectionTest')

      To start the actual migration, run the following commands

         .. code-block:: ruby
            :force:

            # That the actual job
            $ job = ImportJob.create(name: 'Import::Freshdesk')
            $ AsyncImportJob.perform_later(job)

         .. tip::

            **🤓 Want to check the state of the migration?**

            Running the following command in a rails console will provide
            detailed state information of your migration.
      
            .. code-block:: ruby

               pp ImportJob.find_by(name: 'Import::Freshdesk')

            To give you an idea how the migration job state looks like, you can
            use below tabs. As long as ``finished_at`` is ``nil``, the process is
            still running.

            .. tabs::

               .. tab:: Freshly started import

                  .. code-block:: ruby

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

                  .. code-block:: ruby

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

                  .. code-block:: ruby

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

      After the import has finished, run the following commands
         .. code-block:: ruby
            :force:

            $ Setting.set('import_mode', true)
            $ Setting.set('system_init_done', true)
            $ Cache.clear

After migration
===============

As the migration technically skips the getting started wizard, please
note that you want to adjust your `FQDN settings`_ (FQDN & HTTP-Type).

.. include:: /migration/how-to-login.include.rst
   
.. _FQDN settings:
   https://admin-docs.zammad.org/en/latest/settings/system/base.html

After successfully migrating your Freshdesk instance, 
continue with :doc:`/getting-started/first-steps`.

.. include:: /migration/restarting-from-scratch.include.rst
