Migrate to PostgreSQL server
****************************

.. danger::

   This guide is work in progress!


Support for MySQL/MariaDB will be dopped in Zammad 7.0 upwards. Make sure to
migrate your existing instance of Zammad to PostgreSQL before that update.

The following guide will provide you with a rough direction through that
migration process.

.. warning::

   As the technical details may differ from system to system, this guide
   comes without any warranty. Please proceed at your own risk. In doubt
   please refer to the documentation of the tools used.
   

Preperation
===========

#. Zammad should be updated to the latest version.
#. Stop Zammad: ``systemctl stop zammad``
#. Create a backup of your instance.


Install PostgreSQL
------------------

..
  TODO: This is duplicated content

Install PostgreSQL Dependencies

   .. tabs::

      .. tab:: Ubuntu / Debian

         .. code-block:: sh

            $ apt install libpq-dev

      .. tab:: CentOS

         .. code-block:: sh

            # CentOS 7
            $ yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
            $ yum install postgresql13-libs postgresql13-devel

            # CentOS 8
            $ yum install postgresql-libs postgresql-devel

      .. tab:: OpenSuSE

         .. code-block:: sh

            $ zypper install postgresql-devel
			

Install Gems for Zammad

  .. code-block:: sh

     $ su - zammad
     $ bundle config set without "test development mysql"
     $ bundle install

     # CentOS 7 users - above command might fail, run the following
     # command and repeat above bundle install.
     # Adjust pg_config path according to your environment
     $ gem install pg -v '0.21.0' -- --with-pg-config=/usr/pgsql-13/bin/pg_config


  
Database Credentials
====================

Get the credentials Zammad is currently using to access your MySQL/MariaDB
database from ``config/database.yml``. You will need them later.

Now adjust the configuration file to fill in the credentials for your new
PostgreSQL server. Use ``postgresql`` as ``adapter``.


Grant user permissions for PostgreSQL
-------------------------------------

If you want to use the ``db:create`` command to create an empty Zammad
database (see further down), you should grant the system user "zammad"
permission to do so. Otherwise you'll need to create the database yourself.

.. code-block:: sh
   
   $ sudo -u postgres psql
   
   $ ALTER USER zammad CREATEDB;
   $ EXIT;


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

The easiest way is with a Debian-style package manager.

   .. tabs::

      .. tab:: Debian-style packages

         .. code-block:: sh

            $ apt-get install pgloader

      .. tab:: Other
	  	 
		 Please refer to the official documentation:
		 https://pgloader.readthedocs.io/en/latest/install.html


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

After the migration has completed, you'll better clear some cache files
and reindex elasticsearch:

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