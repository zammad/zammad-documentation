Migrate Zammad to new host
**************************

🙅‍♀️ This is a proof of concept, not a full how to. Your environment may be different.
   Please note that the steps described on this page are an addition to
   :doc:`backing up </appendix/backup-and-restore/backup>` and
   :doc:`restoration </appendix/backup-and-restore/restore>`.

   They're not meant to stand alone - we'll link and
   note this at the relevant parts.

   If anything goes wrong, please consult the `Zammad Community`_ or consider
   `paid support options`_.

.. _Zammad Community:
   https://community.zammad.org/c/trouble-running-zammad-this-is-your-place/5

.. _paid support options:
   https://zammad.com/en/services/professional-services

--------------------------------------------------------------------------------

.. hint::

   Migrating from Zammad SaaS? Skip to *step 7*.

Step 1: Note down your environmental adjustments
   This mainly affects :ref:`performance tuning settings <performance_tuning>`.
   This will be important after restoring.

Step 2: Install Zammad on the destination host
   For the easiest restoration path possible, please install the same version
   like your origin instance. You could also consider updating the old instance
   before migrating.

   Choose beetween these installation types:
      * :doc:`package </install/package>`
      * :doc:`source code </install/package>`
      * :doc:`docker-compose </install/docker-compose>`

           .. warning::

              Restoration & Migration on docker based installation may differ.
              While the steps are the same on most parts, it is not covered by
              this documentation!

Step 3: Activate maintenance mode
   This ends agents and customers sessions.
   `Learn more about the maintenance mode in Zammad`_.

.. _Learn more about the maintenance mode in Zammad:
   https://admin-docs.zammad.org/en/latest/system/maintenance.html

Step 4: Disable your communication channels
   This is just a safety measurement. As our restore scripts starts Zammad
   automatically, this may help if something is not in a correct state.

Step 5: Stop and disable Zammad
   Make sure to no longer have Zammad change data *before* backing up.

   .. code-block:: sh

      $ systemctl disable zammad
      $ systemctl stop zammad

   .. note::

      This does not apply to docker based environments.

Step 6: Backup!
   Follow our documentation part for
   :doc:`backup creation </appendix/backup-and-restore/backup>`.

   .. hint::

      Note down if you've created a full filesystem dump or only backed up
      your attachments. This will be important for the restoration.

      If you want to go with the easiest way, consider only dumping your
      attachments. Learn more on our
      :doc:`configuration page </appendix/backup-and-restore/configuration>`.

Step 7: Transfer your backup files
   You'll find the backup location within the ``config`` file on the backup
   directory (`/opt/zammad/contrib/backup`). Make sure to adjust the backup configuration on the destination
   host according to our
   :doc:`configuration page </appendix/backup-and-restore/configuration>`
   to provide the correct backup file directory.

   Provide the file location you transferred the backup files to.

Step 8: Restore your backup
   Follow the steps **1 to 3** of our
   :doc:`restoration page </appendix/backup-and-restore/restore>` to restore
   the backup on the new host.

      .. warning:: 

         If you're running a source code installation, install the same version
         before hand. This reduces environment fiddlings *a lot*.

         If you don't want that, you can find a version list on the
         :doc:`/prerequisites/software` page.

      .. include:: /appendix/backup-and-restore/restore-warning-old-dumps.include.rst

   Important
      Stop Zammad after the restoration has finished.

      If you experience issues during restoration, please consult
      :doc:`/appendix/backup-and-restore/troubleshooting`.

Step 9: Run required maintenance tasks after restoring
   After successful restoration, please continue below depending if you've
   only backed up your attachments or had a full filesystem dump.


      .. tip:: Migrating from Zammad SaaS? You've received an attachment dump! 🤓

   .. tabs::

      .. tab:: Attachment dump (recommended)

         .. include:: /appendix/backup-and-restore/console-command-note.include.rst

         Step 9.1: Clear the cache
            .. include:: /appendix/backup-and-restore/clear-the-cache.include.rst

      .. tab:: Full filesystem dump

         .. tip::

            Skip steps **9.1**, and **9.2**, and **9.3** if you do not have the
            last possible Zammad version installed. However, make sure to run
            the next steps in the following order: **step 12**,
            then **step 10**, then **step 11**.

         .. note::

            This step is only needed, if one of the following points is met:
               * The source and destination Zammad-Version are not the same
               * The Zammad-installation is not a source code installation²
               * The Zammad-Backup is not an Export from Hosted-Setup

            Full-Dumps for source code installations are not covered, however,
            basically the same below applies to you: You have to ensure that
            the environments and application files are overwritten with the new /
            correct version.

            Zammad files are distribution and version specific!

         Step 9.1: Uninstall and reinstall Zammad without resolving dependencies
            Debian, Ubuntu
               .. code-block:: sh

                  $ dpkg -r --force-depends zammad
                  $ apt install zammad

            OpenSUSE
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
            .. include:: /appendix/backup-and-restore/console-command-note.include.rst
            .. include:: /appendix/backup-and-restore/clear-the-cache.include.rst

         Step 9.3: Ensure Zammad is running
            .. code-block:: sh

               $ systemctl status zammad
               # If Zammad is not running, run below
               $ systemctl start zammad

Step 10: Apply missing environmental settings
   .. note::

      This does not apply to Docker images, as the following settings should
      be applied upon every start automatically.

.. include:: /appendix/backup-and-restore/add-missing-environment.include.rst

Step 11: Re-enable Channels and deactivate maintenance mode
   Set the previous deactivated channels back to active if you're sure
   everything was successful. At this point Zammad will start to
   *change data*!

   After verifying the functionality of your channels, allow your agents and
   customers back in by disabling the maintenance mode.

   `Learn more about the maintenance mode in Zammad`_.

   .. hint:: *Migrated from Zammad SaaS or switching providers?*

      Please make sure that your `notification`_ and `FQDN`_ configuration
      is still correct. Other wise you may have unexpected issues like not
      receiving notifications or non functional authentications (3rd party).

.. _notification:
   https://admin-docs.zammad.org/en/latest/channels/email/accounts/email-notification.html

.. _FQDN:
   https://admin-docs.zammad.org/en/latest/settings/system/base.html

Step 12 (optional): Update Zammad to latest possible version
   In case the backup source was not on the latest possible version, please
   update your Zammad installation now.

   In case your installed version is fairly old, please note the
   upgrade path notes on our :doc:`updating zammad </install/update>` page.
