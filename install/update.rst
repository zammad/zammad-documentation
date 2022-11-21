Updating Zammad
***************

.. note::

   🙈 Better safe than sorry
      Before updating to a new version, please have a look into the
      `release notes`_. These will provide further information on new
      feature and fixes, but also technical remarks that may be relevant
      during an upgrade!

   🤓 What about Zammad upgrade paths...?
      In general we do not encourage you to skip Zammad versions or have
      long update cycles. Zammad potentially stores very sensitive information
      (personal information) which is why updating is very important.

      If you don't have time for updating all the time
      (nobody got time for that, right?), please consider using `Zammad hosting`_
      for your and your customers safety.

      In case you couldn't update for a longer time, please ensure to at least
      update from **mayor to mayor** version. Big version jumps *may* work but
      usually go terribly wrong. As example, expecting the current stable
      version of Zammad being 5.1 and your instance being on Zammad 2.4, your
      path would look like so:
      ``2.4`` → ``3.0`` → ``4.0`` → ``5.0`` → ``latest stable (5.1)``

.. _release notes: https://zammad.com/en/releases
.. _Zammad hosting: https://zammad.com/en/pricing

.. tabs::

   .. tab:: Package

      Step 1: Ensure dependencies
         Before proceeding, double-check that your system environment matches
         :doc:`Zammad’s requirements </prerequisites/software>`.

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

         .. warning::

            The package comes with maintenance scripts that will run regular
            tasks during updates for you.

            | **However**
            | Do not run Zammad updates unattended and **always** have a look
              on the outputs these helper scripts generate. Ignoring said
              output may lead to incomplete updates that may corrupt data or
              lead to issues you find *way too late*.

      Step 6: Run required extra steps
         Extra steps needed for updates are mentioned in our release news.

         `Updating Elasticsearch`_ may be relevant in this step.

      Step 7: Log into Zammad
         Yes, that's it!

   .. tab:: Source

      .. danger::

         Zammad's former ``scheduler.rb`` script has changed and is now called
         ``background-worker.rb``. Please ensure to reinstall the service - see
         :ref:`source-install-systemd-reference`!

      Step 1: Ensure dependencies
         Before proceeding, double-check that your system environment matches
         :doc:`Zammad’s requirements </prerequisites/software>`.

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

                  .. include:: /tmp/mysql-deprication-note.rst

                  .. include:: /tmp/mysql-deprication-link.rst

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

      Step 8: Start Zammad services
         Start the application server, web socket server and scheduler.

      Step 9: Log into Zammad
         Yes, that's it!

   .. tab:: Docker Compose

      .. warning::

         ⚠️ **Updates may require extra steps or introduce breaking changes.**

         Always check the
         `upgrade notes <https://github.com/zammad/zammad-docker-compose#upgrading>`_
         first.

      .. note:: **🙀 Incomplete documentation**

         Sorry, but this documentation part is outdated.
         We will rework this part later, but can't tell when yet.

         Please feel welcome to provide a pull request if you find spare time!

      .. code-block:: sh

         $ docker-compose stop
         $ git pull
         $ docker-compose pull
         $ docker-compose up


      Start Zammad building Docker images locally with development branch

      * GIT_BRANCH=develop docker-compose -f docker-compose-build.yml up

      Recreate locally built images

      * GIT_BRANCH=develop docker-compose -f docker-compose-build.yml build --no-cache


      Open shell in running Zammad image

      * docker-compose exec zammad /bin/bash

      Port compatibility error

      * The nginx container may have compatibility problems with other machines or services pointing to port 0.0.0.0:80. So to fix this, we'll just have to modify the file `docker-compose.override.yml` and select different ports


Updating Elasticsearch
======================

.. warning::

   Updating Elasticsearch **does not** automatically update it's plugins!
   This usually isn't an issue if Zammad is being updated right after
   Elasticsearch.

If you want to upgrade your elasticsearch installation, please take a look at the
`elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_
as it will have the most current information for you.

If, for whatever reason, you need to rebuild your search index after upgrading,
use:

.. code-block:: sh

   $ zammad run rake zammad:searchindex:rebuild

.. hint:: **🤓 Zammad 5.2 comes with changes**

   As of Zammad 5.2 the reindex command has changed!
   You will still be able to use the old method until Zammad 6, however, will
   receive a deprecation warning.

.. warning::

   This step may fail if Zammad is under heavy load: Elasticsearch locks the
   indices from deletion if you're pumping in new data, like receiving a new
   ticket. (This only applies to single-node deployments, not clusters.)

   If it does, try killing Zammad first::

      $ systemctl stop zammad
      $ zammad run rake zammad:searchindex:rebuild
      $ systemctl start zammad
