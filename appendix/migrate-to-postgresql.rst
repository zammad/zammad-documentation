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

   .. tab:: Ubuntu / Debian

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install postgresql postgresql-contrib

      .. code-block:: console

         $ sudo systemctl start postgresql

      .. code-block:: console

         $ sudo systemctl enable postgresql

   .. tab:: CentOS

      .. code-block:: console

         $ sudo yum install postgresql-server postgresql-contrib

      .. code-block:: console

         $ sudo postgresql-setup initdb

      .. code-block:: console

         $ sudo systemctl start postgresql


      .. code-block:: console

         $ sudo systemctl enable postgresql

   .. tab:: OpenSUSE / SLES

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

Please also have a look at :doc:`/appendix/configure-database-server`.

Install pgloader
^^^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install pgloader

   .. tab:: CentOS

      .. code-block:: console

         $ sudo yum install -y pgloader

   .. tab:: OpenSUSE / SLES

      .. code-block:: console

         $ sudo zypper refresh

      .. code-block:: console

         $ sudo zypper install pgloader


Create pgloader Command File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a command file for pgloader with:

.. code-block:: console

   $ zammad run rake zammad:db:pgloader > /tmp/pgloader-command

Afterwards, you need to tweak the created file with the correct URL of the
target PostgreSQL server.

Adjust the PostgreSQL URL below to the correct value before executing this
command file:

.. code-block:: text

   pgsql://zammad:pgsql_password@localhost/zammad

You will at least need to replace ``psql_password`` placeholder in the provided
example.

Verify the rest of the MySQL credentials in the command file, they should reflect the
configuration of your current environment.

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

   .. tab:: Dry run

      You can check your configuration by running pgloader in a dry run first:

      .. code-block:: console

         $ pgloader --dry-run /tmp/pgloader-command

   .. tab:: Actual run

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
