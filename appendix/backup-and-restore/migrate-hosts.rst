Migrate Zammad to New Host
**************************

This is just a description of basic steps to perform a migration to a new host.
Your environment may be different so you should consider this as a
reference point only. If anything goes wrong, please consult the
`Zammad Community <https://community.zammad.org/c/trouble-running-zammad-this-is-your-place/5>`_ or consider
`paid support options <https://zammad.com/en/services/professional-services>`_.

The steps described on this page are an addition to
:doc:`backing up </appendix/backup-and-restore/backup>` and
:doc:`restoring </appendix/backup-and-restore/restore>`.
They're not meant to stand alone - we'll link and
note this in the relevant parts.

.. hint::

   Migrating from Zammad SaaS? Skip to *step 7*. For restoration, you've
   received an attachment dump! 🤓

Step 1: Note down your environmental adjustments
   This mainly affects :ref:`performance-tuning` via environment variables and
   will be important after restoring.

Step 2: Install Zammad on the destination host
   For the easiest restoration path possible, please install the same version
   like your origin instance. You could also consider updating the old instance
   before migrating.

   Have a look at the installation instructions:

      * :doc:`Package Installation </install/package>`
      * :doc:`Install with Docker </install/docker-compose>`

Step 3: Activate maintenance mode
   This ends all agent and customer sessions.
   See :admin-docs:`here </system/maintenance.html>` how to activate it.

Step 4: Disable your communication channels
   The restore script starts Zammad automatically, this may help to avoid data
   loss and inconsistencies.

Step 5: Stop and disable Zammad
   Make sure that no data will be changed *before* backing up.

   .. code-block:: sh

      $ systemctl disable zammad
      $ systemctl stop zammad

Step 6: Backup
   Follow the :doc:`backup section </appendix/backup-and-restore/backup>` to
   create your backup.

   Remember if you've created a full filesystem dump or only backed up
   your data. This will be important for the restoration.

   If you want to go the easiest way, consider only dumping your
   data. Learn more on our
   :doc:`configuration page </appendix/backup-and-restore/configuration>`.

Step 7: Transfer your backup files
   Save your backup files in a directory and provide the path to the ``config``
   file. See
   :doc:`backup configuration </appendix/backup-and-restore/configuration>`
   how to adjust the config file to your needs.

Step 8: Restore your backup
   Follow the steps **1 to 3** of our
   :doc:`restoration page </appendix/backup-and-restore/restore>` to restore
   the backup on the new host.

   .. include:: /appendix/backup-and-restore/restore-warning-old-dumps.include.rst

   **Important:**

   Stop Zammad after the restoration has finished.


Step 9: Run required maintenance tasks after restoring
   After successful restoration, please continue below depending if you've
   only backed up your data or have a full filesystem dump.

   .. tabs::

      .. tab:: Data dump (recommended)

         Step 9.1: Clear the cache
            .. include:: /appendix/backup-and-restore/clear-the-cache.include.rst

      .. tab:: Full filesystem dump

         .. note::

            This step is only needed, if one of the following points is met:

               * The source and destination Zammad versions are not the same
               * The Zammad installation is not a source code installation
               * The Zammad backup is not an export from our hosted setup

            Full dumps for source code installations are not covered, however,
            basically the same below applies to you: You have to ensure that
            the environments and application files are overwritten with the new /
            correct version.

            Zammad files are distribution and version specific!

         .. tip::

            Skip steps **9.1**, and **9.2**, and **9.3** if you do not have the
            last possible Zammad version installed. However, make sure to run
            the next steps in the following order: **step 12**,
            then **step 10**, then **step 11**.

         Step 9.1: Uninstall and reinstall Zammad without resolving dependencies
            **Debian, Ubuntu**

            .. code-block:: sh

               $ dpkg -r --force-depends zammad
               $ apt install zammad

            **OpenSUSE**

            .. code-block:: sh

               $ zypper remove -R zammad
               $ zypper install zammad

            .. hint::

               You're unsure if above is really required and a mere reinstall
               would be enough? If you run a dedicated install command on for
               Zammad and receive the following, you absolutely have to run
               above to fix your installation.

                  .. code-block:: sh

                     $ root@zammad:/# apt-get update && apt install zammad
                       Reading package lists... Done
                       Building dependency tree
                       Reading state information... Done
                       zammad is already the newest version (x.x.x-xxxxxx.xxxxxx.xxx).
                       0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

         Step 9.2: Clear the cache
            .. include:: /appendix/backup-and-restore/clear-the-cache.include.rst

         Step 9.3: Ensure Zammad is running
            .. code-block:: sh

               $ systemctl status zammad
               # If Zammad is not running, run below
               $ systemctl start zammad

   .. hint:: Migrated from Zammad SaaS or switching provider?

      Please make sure that your :admin-docs:`notification </channels/email/accounts/email-notification.html>`
      and :admin-docs:`FQDN </settings/system/base.html>` configuration is
      correct.

Step 10: Apply missing environmental settings
   .. include:: /appendix/backup-and-restore/add-missing-environment.include.rst

Step 11: Re-enable channels and deactivate maintenance mode
   Set the previous deactivated channels back to active if you're sure
   everything was successful. At this point Zammad will start to
   *change data*!

   After verifying the functionality of your channels, allow your agents and
   customers to log in again by disabling the
   :admin-docs:`maintenance mode </system/maintenance.html>`.

Step 12 (optional): Update Zammad to latest possible version
   In case the backup source was not on the latest possible version, please
   update your Zammad installation now.

   In case your installed version is fairly old, please note the
   upgrade path notes on our :doc:`updating zammad </install/update>` page.

If you experience issues during restoration, please consult
:doc:`/appendix/backup-and-restore/troubleshooting`.