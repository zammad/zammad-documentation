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

   .. code-block:: console

      $ sudo systemctl stop zammad

#. Create a backup of your instance.

Install PostgreSQL
^^^^^^^^^^^^^^^^^^

.. tabs::

   .. group-tab:: Ubuntu / Debian

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install postgresql postgresql-contrib

      .. code-block:: console

         $ sudo systemctl start postgresql

      .. code-block:: console

         $ sudo systemctl enable postgresql

   .. group-tab:: CentOS

      .. code-block:: console

         $ sudo yum install postgresql-server postgresql-contrib

      .. code-block:: console

         $ sudo postgresql-setup initdb

      .. code-block:: console

         $ sudo systemctl start postgresql


      .. code-block:: console

         $ sudo systemctl enable postgresql

   .. group-tab:: OpenSUSE / SLES

      .. code-block:: console

         $ sudo zypper refresh

      .. code-block:: console

         $ sudo zypper install postgresql postgresql-server postgresql-contrib

      openSuSE 15 also requires:

      .. code-block:: console

         $ sudo zypper install postgresql-server-devel

      .. code-block:: console

         $ sudo systemctl start postgresql

      .. code-block:: console

         $ sudo systemctl enable postgresql

Install pgloader
^^^^^^^^^^^^^^^^

.. tabs::

   .. group-tab:: Ubuntu / Debian

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install pgloader

   .. group-tab:: CentOS

      .. code-block:: console

         $ sudo yum install -y pgloader

   .. group-tab:: OpenSUSE / SLES

      .. code-block:: console

         $ sudo zypper refresh

      .. code-block:: console

         $ sudo zypper install pgloader


Create pgloader Command File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a command file for pgloader:

.. code-block:: console

   $ zammad run rake zammad:db:pgloader > /tmp/pgloader-command

.. hint::

   In case you accidentally updated to Zammad 7 already, use the template below
   and add it to the ``/tmp/pgloader-command`` file:
   
   .. code-block:: psql
   
      LOAD DATABASE
        -- Adjust the MySQL URL below to correct value before executing this command file.
        FROM mysql://zammad:mysql_password@localhost/zammad
      
        -- Adjust the PostgreSQL URL below to correct value before executing this command file.
        INTO pgsql://zammad:pgsql_password@localhost/zammad
      
      ALTER SCHEMA 'zammad' RENAME TO 'public'
      
      AFTER LOAD DO
        $$ alter table smime_certificates alter column email_addresses type varchar[] using translate(email_addresses::varchar, '[]', '{}')::varchar[] $$,
        $$ alter table pgp_keys alter column email_addresses type varchar[] using translate(email_addresses::varchar, '[]', '{}')::varchar[] $$,
        $$ alter table public_links alter column screen type varchar[] using translate(screen::varchar, '[]', '{}')::varchar[] $$,
        $$ alter table checklists alter column sorted_item_ids type varchar[] using translate(sorted_item_ids::varchar, '[]', '{}')::varchar[] $$,
        $$ alter table checklist_templates alter column sorted_item_ids type varchar[] using translate(sorted_item_ids::varchar, '[]', '{}')::varchar[] $$
      
      WITH BATCH CONCURRENCY = 1
      SET timezone = 'UTC'
      SET client_timezone TO '00:00'
      ;

Afterwards, you need to tweak the created file with the correct URL of the
target PostgreSQL server and provide the correct credentials for the
MySQL/MariaDB source database.

.. code-block:: text

   pgsql://zammad:pgsql_password@localhost/zammad
   [...]
   mysql://zammad:mysql_password@localhost/zammad

Replace them with the correct values before continuing.

Please also have a look at :doc:`/appendix/configure-database-server` in case
you want to adjust your configuration.

Database Credentials
^^^^^^^^^^^^^^^^^^^^

Adjust the configuration file to fill in the credentials for your new
PostgreSQL server. Use ``postgresql`` as ``adapter``.

.. tip::

   **🤓 For easiest usage ...**

   If you provide your Zammad user with database creation permission, you can
   run ``db:create`` in the following section. If you don't want that, you'll
   have to create the database manually.

Create Empty Database
^^^^^^^^^^^^^^^^^^^^^

Now you need to create an empty database in PostgreSQL.

.. code-block:: console

   $ zammad run rake db:create

Migrate
-------

.. tabs::

   .. group-tab:: Dry run

      You can check your configuration by running pgloader in a dry run first:

      .. code-block:: console

         $ pgloader --dry-run /tmp/pgloader-command

   .. group-tab:: Actual run

      Once you are ready and setup you can start the actual migration:

      .. code-block:: console

         $ pgloader --verbose /tmp/pgloader-command

Finishing
---------

After the migration has completed, it is recommended to remove some cache files
and restart Zammad:

.. code-block:: console

   $ zammad run rails r 'Rails.cache.clear'

.. code-block:: console

   $ sudo systemctl start zammad
