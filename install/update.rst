Updating Zammad
***************

.. note:: 

   Before updating to a new version, you may want to have a look into the 
   official `release notes <https://zammad.com/en/releases>`_. These will 
   provide further information on new feature and fixes, but also technical 
   remarks that may be relevant during an upgrade!

.. tabs::

   .. tab:: Package

      Step 1: Ensure dependencies
         Before proceeding, double-check that your system environment matches 
         :doc:`Zammad’s requirements </prerequisites/software>`.

      Step 2: Stop Zammad
         .. code-block:: sh

            $ systemctl stop zammad

      Step 3: Backup Zammad
         See :doc:`/appendix/backup-and-restore` for more information.

      Step 3: Clear Zammad cache
         .. code-block:: sh

            $ zammad run railsr "Cache.clear"

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

      Step 1: Ensure dependencies
         Before proceeding, double-check that your system environment matches 
         :doc:`Zammad’s requirements </prerequisites/software>`.

         .. tip:: **🤓 Ruby version changed?**

            Please see 
            :ref:`Installation part of source code installation <source_dependency_installation>`

      Step 2: Stop Zammad and Clear Zammad cache
         Before you continue, stop your Zammad processes.

         .. code-block:: sh

            $ rails r "Cache.clear"

      Step 3: Download Zammad to your system
         .. include:: /install/source/include-get-the-source.rst

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

      Step 5: Stop Zammad services
         Stop the application server, websocket server and scheduler.

      Step 6: Upgrade your database
         .. code-block:: sh

            $ su - zammad
            $ rake db:migrate
            $ rake assets:precompile

      Step 7: Start Zammad services
         Start the application server, web socket server and scheduler.

      Step 8: Log into Zammad
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

   $ zammad run rake searchindex:rebuild

.. warning:: 

   This step may fail if Zammad is under heavy load: Elasticsearch locks the 
   indices from deletion if you're pumping in new data, like receiving a new 
   ticket. (This only applies to single-node deployments, not clusters.)
   
   If it does, try killing Zammad first::
   
      $ systemctl stop zammad
      $ zammad run rake searchindex:rebuild
      $ systemctl start zammad
