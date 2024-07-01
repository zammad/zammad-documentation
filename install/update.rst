Updating Zammad
===============

Before updating Zammad, we strongly recommend to take a look at our
`release notes`_. You can find information about features and fixes as well as
technical remarks and breaking changes.

Be aware that you **should not** skip major Zammad versions while updating.
That means, for example, your upgrade path from version 2.4 to 5.1 (assuming
this is the current stable) would be:
``2.4`` → ``3.0`` → ``4.0`` → ``5.0`` → ``latest stable (5.1)``

If you don't have time for updating all the time, please consider
using `Zammad hosting`_ for your and your customer's safety.

.. _release notes: https://zammad.com/en/releases
.. _Zammad hosting: https://zammad.com/en/pricing

.. tabs::

   .. tab:: Package

      Step 1: Ensure dependencies
         Before proceeding, double-check that your system environment matches
         :doc:`Zammad's requirements </prerequisites/software>`.

      Step 2: Stop Zammad
         .. code-block:: sh

            $ systemctl stop zammad

      Step 3: Backup Zammad
         See :doc:`/appendix/backup-and-restore/index` for more information.

      Step 4: Clear Zammad cache
         .. code-block:: sh

            $ zammad run rails r "Rails.cache.clear"

      Step 5: Update Zammad
         .. tabs::

            .. tab:: Ubuntu / Debian

               .. code-block:: sh

                  $ apt update
                  $ apt upgrade

            .. tab:: CentOS

               .. code-block:: sh

                  $ yum update zammad

            .. tab:: OpenSUSE / SLES

               .. code-block:: sh

                  $ zypper ref
                  $ zypper up

            The package comes with maintenance scripts that will run regular
            tasks during updates for you. However, you should **always** have
            a look on the outputs these helper scripts generate. Ignoring said
            output may lead to incomplete updates that may corrupt data or
            lead to issues.

      Step 6: Additional steps
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

            If you are using plugins for Elasticsearch, make sure they are
            updated as well (note: starting with Elasticsearch 8, the
            ingest-attachment is no longer a plugin, it's now included in
            Elasticsearch).

      Step 7: Log into Zammad
         Yes, that's it!

   .. tab:: Source

      .. danger::

         Zammad's former ``scheduler.rb`` script has changed and is now called
         ``background-worker.rb``. Please ensure to reinstall the service - see
         :ref:`source-install-systemd-reference`!

      Step 1: Ensure dependencies
         Before proceeding, double-check that your system environment matches
         :doc:`Zammad's requirements </prerequisites/software>`.

         .. tip:: **🤓 Ruby version changed?**

            Please see
            :ref:`Installation part of source code installation <source_dependency_installation>`

      Step 2: Stop Zammad and Clear Zammad cache
         Before you continue, stop your Zammad processes.

         .. code-block:: sh

            $ rails r "Rails.cache.clear"

      Step 3: Download Zammad to your system
         .. include:: /install/source/include-get-the-source.rst

         .. include:: /install/source/include-chmod-database-yml.rst

      Step 4: Install Gems
         .. code-block:: sh

            $ su - zammad
            $ cd /opt/zammad
            $ gem install bundler

         .. tabs::

            .. tab:: PostgreSQL

               .. code-block:: sh

                  $ bundle install --without test development mysql

            .. tab:: MySQL / MariaDB

               .. code-block:: sh

                  $ bundle install --without test development postgres

               .. danger::

                  .. include:: /appendix/includes/mysql-deprication-note.rst

      Step 5: Stop Zammad services
         Stop the application server, websocket server and scheduler.

      Step 6: Upgrade your database
         .. code-block:: sh

            $ su - zammad
            $ rake db:migrate
            $ rake assets:precompile

      Step 7: Synchronize Zammad's translation files
         .. code-block:: sh

            $ su - zammad # ignore if you haven't exited the Zammad user
            $ rails r "Locale.sync"
            $ rails r "Translation.sync"

      Step 8: Check if Elasticseach update is necessary
            Make sure to have a
            supported version of Elasticsearch installed (see
            :ref:`software prerequisites <prerequisites_elasticsearch>` for
            supported versions).

            If you have to update Elasticsearch, please have a look at their
            `documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_
            and follow the instructions.

            If you are using plugins for Elasticsearch, make sure they are
            updated as well (note: starting with Elasticsearch 8, the
            ingest-attachment is no longer a plugin, it's now included in
            Elasticsearch).

      Step 9: Start Zammad services
         Start the application server, web socket server and scheduler.

      Step 10: Log into Zammad
         Yes, that's it!

   .. tab:: Docker

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
         .. code-block:: sh

            $ cd zammad-docker-compose
            $ git pull
            $ docker-compose pull
            $ docker-compose up -d

