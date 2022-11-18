Migrate to PostgreSQL server
****************************

Support for MySQL/MariaDB will be dropped in Zammad 7.0 upwards. Make sure to
migrate your existing instance of Zammad to PostgreSQL before that update.

The following guide will provide you with a rough direction through that
migration process.

.. warning:: **Proof of concept ahead**

   As the technical details may differ from system to system, this guide
   comes without any warranty. Please proceed at your own risk. In doubt
   please refer to the documentation of the tools used.
   

Preparation
===========

#. Stop Zammad: ``systemctl stop zammad``
#. Create a backup of your instance.


Install PostgreSQL
------------------

Install PostgreSQL
   .. tabs::

      .. tab:: Ubuntu / Debian

         .. code-block:: sh

            $ apt update
            $ apt install postgresql postgresql-contrib
            $ systemctl start postgresql
            $ systemctl enable postgresql

      .. tab:: CentOS

         .. code-block:: sh

            # CentOS 7
            $ yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
            $ yum install postgresql13-server postgresql13-contrib
            $ postgresql13-setup initdb
            $ systemctl start postgresql13
            $ systemctl enable postgresql13

            # CentOS 8
            $ yum install postgresql-server postgresql-contrib
            $ postgresql-setup initdb
            $ systemctl start postgresql
            $ systemctl enable postgresql

      .. tab:: OpenSUSE / SLES

         .. code-block:: sh

            $ zypper refresh
            $ zypper install postgresql postgresql-server postgresql-contrib
            $ systemctl start postgresql
            $ systemctl enable postgresql

Only for Zammad source installations
   The following steps are only relevant if you installed Zammad from source:

   .. include:: /install/includes/postgres-dependencies.rst

Please also have a look at :doc:`/appendix/configure-database-server`.

  
Database Credentials
--------------------

Get the credentials Zammad is currently using to access your MySQL/MariaDB
database from ``config/database.yml``. You will need them later.

Now adjust the configuration file to fill in the credentials for your new
PostgreSQL server. Use ``postgresql`` as ``adapter``.


.. include:: /install/includes/postgres-permissions.rst


Create empty database
---------------------

Now you need to create an empty database in PostgreSQL.

.. tabs::

   .. tab:: Source installation
      
	  .. code-block:: sh
	     
		 $ su - zammad
		 $ rake db:create
		 
   .. tab:: Package installation
  
      .. code-block:: sh
	     
	  	 $ zammad run rake db:create


Install pgloader
================

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



Create command file
-------------------

Create a command file for pgloader for example in ``/tmp/pgloader-command``:

.. code-block:: cfg


   LOAD DATABASE
		FROM mysql://zammad:mysql_password@localhost/zammad
		INTO pgsql://zammad:pgsql_password@localhost/zammad

   ALTER SCHEMA 'zammad' RENAME TO 'public'

   WITH BATCH CONCURRENCY = 1;

If your database names and/or database usernames are different from ``zammad``
adjust accordingly. And don't forget to replace ``mysql_password`` and
``psql_password``.
   
   
Migration with pgloader
=======================

Dry run
  You can check your configuration by running pgloader in a dry run first:

  .. code-block:: sh

     $ pgloader --dry-run /tmp/pgloader-command

Actual run
   Once you are ready and setup you can start the migration from MySQL/MariaDB
   to PostgreSQL:

   .. code-block:: sh

      $ pgloader --verbose /tmp/pgloader-command
   
   
Finishing
=========

After the migration has completed, you'll better clear some cache files:

.. tabs::

   .. tab:: Source installation
      
	  .. code-block:: sh
	     
		 $ su - zammad
		 $ rails r 'Rails.cache.clear'
		 
		 # Run as root
		 $ systemctl start zammad
		 
   .. tab:: Package installation
  
      .. code-block:: sh
	     
	  	 $ zammad run rails r 'Rails.cache.clear'
		 $ systemctl start zammad