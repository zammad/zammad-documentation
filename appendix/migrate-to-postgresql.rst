Migrate to PostgreSQL server
****************************

.. include:: /appendix/includes/mysql-deprication-note.rst

The following guide will provide you with a rough direction through that
migration process.

.. warning:: **Proof of concept ahead**

   As the technical details may differ from system to system, this guide
   comes without any warranty. Please proceed at your own risk. In doubt
   please refer to the documentation of the tools used.


Preparation
===========

#. Stop Zammad:

   .. code-block:: sh

      $ systemctl stop zammad

#. Create a backup of your instance.


Install PostgreSQL
------------------

.. include:: /install/includes/postgres-installation.rst

Please also have a look at :doc:`/appendix/configure-database-server`.

.. tabs::

   .. tab:: Package installation

      Nothing to do, continue with the next step. 🎉

   .. tab:: Source code installations

      .. include:: /install/includes/postgres-dependencies.rst


Install pgloader
----------------

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh

         $ apt update
         $ apt install pgloader

   .. tab:: CentOS

      .. code-block:: sh

         $ yum install -y https://download.postgresql.org/pub/repos/yum/common/redhat/rhel-7-x86_64/pgloader-3.6.2-1.rhel7.x86_64.rpm

   .. tab:: OpenSUSE / SLES

      .. code-block:: sh

         $ zypper refresh
         $ zypper install pgloader


Create pgloader command file
----------------------------

Create a command file for pgloader with:

.. tabs::

   .. tab:: Package installation

      .. code-block:: sh

         $ zammad run rake zammad:db:pgloader > /tmp/pgloader-command

   .. tab:: Source installation

      .. code-block:: sh

         $ su - zammad
         $ rake zammad:db:pgloader > /tmp/pgloader-command


Afterwards, you need to tweak the created file with the correct URL
of the target PostgreSQL server.

.. code-block:: cfg

   -- Adjust the PostgreSQL URL below to correct value before executing this command file.
   INTO pgsql://zammad:pgsql_password@localhost/zammad


You will at least need to replace ``psql_password`` placeholder in the provided
example.

Verify the rest of the MySQL credentials in the command file, they should reflect the
configuration of your current environment.


Database Credentials
--------------------

Adjust the configuration file to fill in the credentials for your new
PostgreSQL server. Use ``postgresql`` as ``adapter``.


.. include:: /install/includes/postgres-permissions.rst


Create empty database
---------------------

Now you need to create an empty database in PostgreSQL.

.. tabs::

   .. tab:: Package installation

      .. code-block:: sh

         $ zammad run rake db:create

   .. tab:: Source installation

      .. code-block:: sh

         $ su - zammad
         $ rake db:create


Migrate
=======

.. tabs::

   .. tab:: Dry run

      You can check your configuration by running pgloader in a dry run first:

      .. code-block:: sh

         $ pgloader --dry-run /tmp/pgloader-command

   .. tab:: Actual run

      Once you are ready and setup you can start the actual migration:

      .. code-block:: sh

         $ pgloader --verbose /tmp/pgloader-command


Finishing
=========

After the migration has completed, you'll better clear some cache files:

.. tabs::

   .. tab:: Package installation

      .. code-block:: sh

         $ zammad run rails r 'Rails.cache.clear'
         $ systemctl start zammad

   .. tab:: Source installation

      .. code-block:: sh

         $ su - zammad
         $ rails r 'Rails.cache.clear'

         # Run as root
         $ systemctl start zammad
