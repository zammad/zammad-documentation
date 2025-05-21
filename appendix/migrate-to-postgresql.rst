Migrate to PostgreSQL Server
============================

The following guide will give you some hints for the migration from
MySQL/MariaDB to PostgreSQL. Starting with Zammad 7, the only supported database
server is PostgreSQL.

.. warning::

   - The commands on this page will only work with Zammad 5.3 or higher.
   - Make sure to migrate **before** upgrading to Zammad 7. An upgrade
     to Zammad 7 is not possible on a MySQL installation.
   - As the technical details may differ from system to system, this guide
     comes without any warranty. Please proceed at your own risk. In doubt,
     please refer to the documentation of the tools used.

Preparation
-----------

#. Stop Zammad:

   .. code-block:: sh

      $ systemctl stop zammad

#. Create a backup of your instance.

Install PostgreSQL
^^^^^^^^^^^^^^^^^^

.. include:: /install/includes/postgres-installation.rst

Please also have a look at :doc:`/appendix/configure-database-server`.

Install pgloader
^^^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh

         $ apt update
         $ apt install pgloader

   .. tab:: CentOS

      .. code-block:: sh

         $ yum install -y pgloader

   .. tab:: OpenSUSE / SLES

      .. code-block:: sh

         $ zypper refresh
         $ zypper install pgloader


Create pgloader Command File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a command file for pgloader with:

.. code-block:: sh

   $ zammad run rake zammad:db:pgloader > /tmp/pgloader-command

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
^^^^^^^^^^^^^^^^^^^^

Adjust the configuration file to fill in the credentials for your new
PostgreSQL server. Use ``postgresql`` as ``adapter``.


.. include:: /install/includes/postgres-permissions.rst

Create Empty Database
^^^^^^^^^^^^^^^^^^^^^

Now you need to create an empty database in PostgreSQL.

.. code-block:: sh

   $ zammad run rake db:create

Migrate
-------

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
---------

After the migration has completed, it is recommended to remove some cache files:

.. code-block:: sh

   $ zammad run rails r 'Rails.cache.clear'
   $ systemctl start zammad
