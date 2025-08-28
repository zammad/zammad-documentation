Updating Zammad
===============

.. include:: /install/includes/hosted-services.rst

Before updating Zammad, we strongly recommend to take a look at our
`release notes`_. You can find information about features and fixes as well as
technical remarks and breaking changes.

Be aware that you **should not** skip major Zammad versions while updating.
That means, for example, your upgrade path from version 2.4 to 5.1 (assuming
this is the current stable) would be:
``2.4`` → ``3.0`` → ``4.0`` → ``5.0`` → ``latest stable (5.1)``

If you don't have time for updating all the time, please consider
using `Zammad hosting`_ for your and your customers' safety.

.. _release notes: https://zammad.com/en/releases
.. _Zammad hosting: https://zammad.com/en/pricing

.. tabs::

   .. tab:: Package Installation

      Step 1: Ensure dependencies
         Before proceeding, double-check that your system environment matches
         :doc:`Zammad's requirements </prerequisites/software>`.

      Step 2: Stop Zammad
         .. code-block:: console

            $ systemctl stop zammad

      Step 3: Backup Zammad
         See :doc:`/appendix/backup-and-restore/index` for more information.

      Step 4: Update Zammad
         .. note::
            If you update your complete system and there are updates for Zammad
            **and** your database server, this could lead to errors because your
            database may not be online again when Zammad is updated.

            In such a case, you might want to exclude Zammad from updating
            temporarily as you can see in the commands below.

         .. tabs::

            .. tab:: Ubuntu / Debian

               .. code-block:: console

                  $ apt update
                  $ apt-mark hold zammad           # disable updates for Zammad
                  $ apt upgrade                    # update all packages except Zammad
                  $ apt-mark unhold zammad         # re-enable updates for Zammad
                  $ apt upgrade                    # update Zammad

            .. tab:: OpenSUSE / SLES

               .. code-block:: console

                  $ zypper refresh
                  $ zypper addlock zammad          # disable updates for Zammad
                  $ zypper update                  # update all packages except Zammad
                  $ zypper removelock zammad       # re-enable updates for Zammad
                  $ zypper update                  # update Zammad


            .. tab:: CentOS / RHEL

               .. code-block:: console

                  $ yum check-update
                  $ yum upgrade --exclude zammad   # update all packages except Zammad
                  $ yum upgrade                    # update Zammad

            The package comes with maintenance scripts that will run regular
            tasks during updates for you. However, you should **always** have
            a look at the outputs these helper scripts generate. Ignoring said
            output may lead to incomplete updates that may corrupt data or
            lead to issues.

      Step 5: Additional steps
         Check release notes
            If not already done, check our `release notes`_ if extra steps are
            necessary and perform them, if applicable.

         Updating Elasticsearch
            Updating Elasticsearch may be relevant, too. Make sure to have a
            supported version of Elasticsearch installed (see
            :ref:`software prerequisites <prerequisites_elasticsearch>` for
            supported versions).

            If you have to update Elasticsearch, please have a look at their
            `documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_
            and follow the instructions.

            In case your are using plugins for Elasticsearch, make sure they are
            updated as well (note: starting with Elasticsearch 8, the
            ingest-attachment is no longer a plugin, it's now included in
            Elasticsearch).

      Step 6: Rebuild Elasticsearch index (optional)
         Only needed if the release note tells you to rebuild the Elasticsearch
         index.

         .. code-block:: console

            $ zammad run rake zammad:searchindex:rebuild

            # Optionally, you can specify a number of CPU cores which are used for
            # rebuilding the searchindex, as in the following example with 8 cores:
            $ zammad run rake zammad:searchindex:rebuild[8]

      Step 7: Log into Zammad
         Yes, that's it!

   .. tab:: Docker Installation

      .. hint::

         Docker-Compose stack updates may require extra steps or introduce breaking changes. Always check the
         `docker compose release notes <https://github.com/zammad/zammad-docker-compose/releases>`_
         for updating instructions first.

      Updating Portainer based Installations
         In your Zammad stack, click on **Pull and redeploy**, activate
         **Re-pull image and redeploy** and click on **Update**.

         .. figure:: /images/install/docker-compose/portainer/portainer-stack-update.png
            :alt: Screenshot showing stack details with highlighted "Pull and redeploy" button and modal dialog.

      Updating Docker-Compose based Installations
         .. code-block:: console

            $ cd zammad-docker-compose
            $ git pull
            $ docker-compose pull
            $ docker-compose up -d

      Rebuild Elasticsearch index (optional)
         Only needed if the release note tells you to rebuild the Elasticsearch
         index.

         **Docker compose:**

         .. code-block:: console

            $ docker compose run --rm zammad-railsserver rails r rake zammad:searchindex:rebuild

            # Optionally, you can specify a number of CPU cores which are used for
            # rebuilding the searchindex, as in the following example with 8 cores:
            $ docker compose run --rm zammad-railsserver rails r rake zammad:searchindex:rebuild[8]

         **Portainer:**

         Open the :ref:`console via Portainer's GUI <docker-run-commands>`
         (but use the entrypoint ``bash-via-entrypoint: /docker-entrypoint.sh /bin/bash``
         instead) and run:

         .. code-block:: console

            $ rake zammad:searchindex:rebuild

            # Optionally, you can specify a number of CPU cores which are used for
            # rebuilding the searchindex, as in the following example with 8 cores:
            $ rake zammad:searchindex:rebuild[8]