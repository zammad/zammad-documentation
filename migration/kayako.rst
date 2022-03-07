From Kayako
***********

Limitations
===========

Please note below Kayako specific limitations. 
These are additional limitations to the
:ref:`general ones listed <migration_limitations>`.

   * | Differential migrations are **not** supported!
     | The general suggestion is to run a test import before to learn
       how long the migration is going to take.
   * Selfhosted installations (Kayako classic) *are not* supported.
   * The following ticket field customizations are being ignored
     (affects "Scale" plan):

        * Custom ticket states,
        * Custom ticket priorities, and
        * Custom ticket types.

   * **Important:** Please note that migration speed highly depends on your
     Kayako plan (API rate limits apply).
   * User passwords are not migrated and will require the user to use the
     `password reset link`_ on the login page.

.. _password reset link:
   https://admin-docs.zammad.org/en/latest/settings/security/base.html#lost-password

   .. note::

      Your Kayako plan has to provide API support.
      This may not apply to all available plans.

Prerequisites
=============

Zammad requires API access which is why the migrator will request your
Kayako-URL, email address and password.

.. warning:: **🥸 To be or not to be**

  Ensure to provide an user account with **full administrative** permissions.
  Less privileged users will end in a broken migration.

Importing Kayako data
=====================

Generally you have two options on how to migrate data.
If you have a fairly big instance with a lot of data, you may want to
consider using the console over the browser version.

.. tabs::

   .. tab:: Via browser

      After installing Zammad and configuring your 
      :doc:`webserver </getting-started/configure-webserver>`, navigate to your 
      Zammads FQDN in your browser and follow the migration wizard.

      Depending on the number of users, tickets and Kayako plan this may take
      some while.

      .. figure:: /images/migration/kayako/import-via-ui.gif
         :alt: Migration process of Kayako via UI

      .. note:: **😖 Scheduler got interrupted**

         .. figure:: /images/migration/kayako/scheduler-interrupted.png

         If this message appears after providing your credentials, please be
         patient. The migration should start within 5 minutes.

         If you receive above message after the migration begun, please
         consider using the console approach instead and reset the
         installation.

   .. tab:: Via console

      .. include:: /migration/includes/rails-console-migrator-hint.include.rst

      To prepare the migration, run the following commands
         .. code-block:: ruby
            :force:

            # Set variables for easier settings
            $ subdomain = '{kayako subdomain}.kayako.com'
            $ email = '{kayako admin email address}'
            $ password = '{kayako admin password}'

            # Update Zammad settings for Kayako import
            $ Setting.set('import_kayako_endpoint', "https://#{subdomain}/api/v1")
            $ Setting.set('import_kayako_endpoint_username', email)
            $ Setting.set('import_kayako_endpoint_password', password)
            $ Setting.set('import_backend', 'kayako')
            $ Setting.set('import_mode', true)


         .. hint::

            Want to know if your configuration works before hand?
            Run the following command:

            .. code-block:: ruby

               Sequencer.process('Import::Kayako::ConnectionTest')

      To start the actual migration, run the following commands

         .. code-block:: ruby
            :force:

            # That the actual job
            $ job = ImportJob.create(name: 'Import::Kayako')
            $ AsyncImportJob.perform_later(job)

         .. tip::

            **🤓 Want to check the state of the migration?**

            Running the following command in a rails console will provide
            detailed state information of your migration.
      
            .. code-block:: ruby

               pp ImportJob.find_by(name: 'Import::Kayako')

            To give you an idea how the migration job state looks like, you can
            use below tabs. As long as ``finished_at`` is ``nil``, the process
            is still running.

            .. tabs::

               .. tab:: Freshly started import

                  .. code-block:: ruby

                     #<ImportJob:0x0000000008274310
                      id: 1,
                      name: "Import::Kayako",
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
                      name: "Import::Kayako",
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
                      name: "Import::Kayako",
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

After migration
===============

As the migration technically skips the getting started wizard, please
note that you want to adjust your `FQDN settings`_ (FQDN & HTTP-Type).

.. hint::

   **😖 How do I login?**

   Zammad provides admin access to the user whose login credentials you
   provided. Use the admins email address and password provided during the
   migration to login.

   All other users will have to use the password reset function or login methods
   like LDAP or one click logins.
   
.. _FQDN settings:
   https://admin-docs.zammad.org/en/latest/settings/system/base.html

After successfully migrating your Kayako instance, 
continue with :doc:`/getting-started/first-steps`.

.. include:: /migration/includes/restarting-from-scratch.include.rst
