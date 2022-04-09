Install from source
*******************

.. toctree::
   :hidden:

   source/macos

.. note::

   The source installation is the most difficult installation type of Zammad. 
   If you're not too experienced with Linux and all that, you may want to use 
   another installation type:

      * :doc:`/install/package`
      * :doc:`/install/docker-compose`

   | **Administrative note**
   | Please note that we only use ``sudo`` after direct user changes. 
     In all other situations you can expect ``root`` being in charge.

.. hint::

   **🔎 Looking for MacOS hints?**
   You can find outdated documentation :doc:`here </install/source/macos>`.

Prerequisites
=============

Software dependencies
---------------------

Please ensure that you already provided mentioned 
:doc:`Software requirements </prerequisites/software>`.

Also ensure to provide your database server and web server at this point.

.. include:: /install/includes/prerequisites.rst

Add user
--------

.. code-block:: sh

   $ useradd zammad -m -d /opt/zammad -s /bin/bash
   $ groupadd zammad

Installation
============

Step 1: Get the source
----------------------

.. note::

   Not all distributions ship ``wget`` and ``tar`` by default, you may need to 
   install it manually.

.. include:: /install/source/include-get-the-source.rst

.. _source_dependency_installation:

Step 2: Install dependencies
----------------------------

..
   About this section: The RVM installation part uses definition list instead 
   of field lists intentionally. It's supposed to safe width for better readability.

.. note:: 

   | **Below commands do neither include the database server nor the web server.** 
   | We do cover important web server related stuff within :doc:`/getting-started/configure-webserver`.


Zammad requires specific ruby versions. Adapt the commands below if you install 
older versions. A list of required versions can be found on the 
:doc:`Software requirements </prerequisites/software>` page.

.. tabs::

   .. tab:: Ubuntu

      Install Node.js
         .. include:: /install/includes/nodejs/ubuntu.rst

      Install RVM
         .. code-block:: sh

            $ apt install curl git patch build-essential bison zlib1g-dev libssl-dev libxml2-dev libxml2-dev autotools-dev\ 
              libxslt1-dev libyaml-0-2 autoconf automake libreadline-dev libyaml-dev libtool libgmp-dev libgdbm-dev libncurses5-dev\ 
              pkg-config libffi-dev libimlib2-dev gawk libsqlite3-dev sqlite3 software-properties-common

            $ apt-add-repository -y ppa:rael-gc/rvm
            $ apt update
            $ apt install rvm

      Set relevant Environment variables
         .. include:: source/include-environment.rst

      Install Ruby Environment
         .. include:: source/include-rvm-install-ruby.rst
  
   .. tab:: Debian

      Install Node.js
         .. include:: /install/includes/nodejs/debian.rst

      Install RVM
         .. code-block:: sh

            $ apt install curl git patch build-essential bison zlib1g-dev libssl-dev libxml2-dev libxml2-dev autotools-dev\ 
              libxslt1-dev libyaml-0-2 autoconf automake libreadline-dev libyaml-dev libtool libgmp-dev libgdbm-dev libncurses5-dev\ 
              pkg-config libffi-dev libimlib2-dev gawk libsqlite3-dev sqlite3

            $ gpg --keyserver keyserver.ubuntu.com --recv-keys\ 
              409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
            $ curl -L https://get.rvm.io | bash -s stable

      Set relevant Environment variables
         .. include:: source/include-environment.rst

      Install Ruby Environment
         .. include:: source/include-rvm-install-ruby.rst

   .. tab:: CentOS

      Install Node.js
         .. include:: /install/includes/nodejs/centos.rst

      Install RVM
         .. code-block:: sh

            $ yum install epel-release
            $ yum install patch autoconf automake bison bzip2 gcc-c++ libffi-devel libtool make patch readline-devel ruby sqlite-devel\
              zlib-devel glibc-headers glibc-devel openssl-devel git imlib2 imlib2-devel

            $ gpg --keyserver keyserver.ubuntu.com --recv-keys\ 
              409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
            $ curl -L https://get.rvm.io | bash -s stable

      Set relevant Environment variables
         .. include:: source/include-environment.rst

      Install Ruby Environment
         .. include:: source/include-rvm-install-ruby.rst

   .. tab:: OpenSuSE

      Install Node.js
         .. include:: /install/includes/nodejs/suse.rst

      Install RVM
         .. code-block:: sh

            $ zypper install patch autoconf automake bison bzip2 gcc-c++ libffi-devel libtool make patch readline-devel sqlite3-devel\ 
              sqlite3 zlib-devel glibc-devel openssl-devel git imlib2 imlib2-devel gdbm-devel libyaml-devel

            $ gpg --keyserver keyserver.ubuntu.com --recv-keys\ 
              409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
            $ curl -L https://get.rvm.io | bash -s stable

      Set relevant Environment variables
         .. include:: source/include-environment.rst

      Install Ruby Environment
         .. include:: source/include-rvm-install-ruby.rst

   .. tab:: other

      Other systems than above mentioned are out of scope of this documentation. 
      Please check the `rvm documentation <https://rvm.io/rvm/install>`_ on how 
      to install rvm on your system. 

      Please also ensure to install ``nodejs``.

      After that install the specific required ruby version.

| After installing bundler, rake and rails we'll need to install all required gems. 
| The command depends on the database server you are using.

.. tabs::

   .. tab:: PostgreSQL (recommended)

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

                  $ zypper install postgresql-devel postgresql-server-devel

      Install Gems for Zammad
         .. code-block:: sh

            $ su - zammad
            $ bundle config set without "test development mysql"
            $ bundle install

            # CentOS 7 users - above command might fail, run the following
            # command and repeat above bundle install.
            # Adjust pg_config path according to your environment
            $ gem install pg -v '0.21.0' -- --with-pg-config=/usr/pgsql-13/bin/pg_config

   .. tab:: MySQL / MariaDB

      Install MySQL/MariaDB Dependencies
         .. tabs::

            .. tab:: Ubuntu / Debian

               .. code-block:: sh

                  $ apt install libmariadb-dev

            .. tab:: CentOS

               .. code-block:: sh

                  $ yum install mariadb-devel

            .. tab:: OpenSuSE

               .. code-block:: sh

                  $ zypper install libmariadb-devel

      Create database
         While that's basically an easy step, you may want to create your
         database as follows to minimize potential issues.

         Below commands need adjustments to fit your environment.
         Choose a safe password.

         .. code-block:: sh

            $ mysql
            > create user 'zammad'@'localhost' identified by 'changeme';
            > CREATE DATABASE zammad DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
            > GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, DROP, ALTER, CREATE TEMPORARY TABLES,\ 
              LOCK TABLES ON zammad.* TO 'zammad'@'localhost';


      Install Gems for Zammad
         .. code-block:: sh

            $ su - zammad
            $ bundle set config without "test development postgres"
            $ bundle install

Step 3: Configure database settings
-----------------------------------

.. tip::

   **🤓 For easiest usage ...**

   If you provide your Zammad user with database creation permission, you can 
   run the step 4 without adjustment. If you don't want that, you'll have to 
   create the database manually.

.. code-block:: sh

   $ cp config/database/database.yml config/database.yml
   $ vi config/database.yml

Here's a sample configuration to give you an idea on how your configuration 
file could look like. Please also have a look at 
:doc:`/appendix/configure-database-server` for deeper details.

.. tabs::

   .. tab:: PostgreSQL

      .. code-block::

         production:
           adapter: postgresql
           database: zammad
           pool: 50
           timeout: 5000
           encoding: utf8
           username: zammad
           password: changeme

      .. hint:: 

         You can remove the ``password`` line if you enable socket based 
         authentication!

   .. tab:: MySQL / MariaDB

      .. code-block::

         production:
           adapter: mysql2
           database: zammad
           pool: 50
           timeout: 5000
           encoding: utf8
           username: zammad
           password: changeme

   .. hint:: 

      If you want to use an existing database server that's not on the same 
      machine, you can also use ``host`` and ``port`` to set that up.

   .. include:: /install/source/include-chmod-database-yml.rst

Step 4: Initialize your database
--------------------------------

.. warning::

   Ensure to do this as ``zammad`` user in your Zammad directory!

.. code-block:: sh

   $ su - zammad
   $ rake db:create      # SKIP IF you already created zammads database (see tip of step 3)
   $ rake db:migrate
   $ rake db:seed

Step 5: Pre compile all Zammad assets
-------------------------------------

.. code-block:: sh

   $ rake assets:precompile

Step 6: Start Zammad or install as service
------------------------------------------

.. note::

   Run the following commands as ``root``.

You can start all services by hand or use systemd to start / stop Zammad.

.. tabs::

   .. tab:: systemd (recommended)

      .. code-block:: sh

         $ cd /opt/zammad/script/systemd
         $ ./install-zammad-systemd-services.sh

   .. tab:: the manual way

      .. note:: 

        This method is not suitable for production use - you should avoid it.

      .. code-block:: sh

         $ rails s -p 3000 # application web server
         $ script/websocket-server.rb start # non blocking websocket server
         $ script/scheduler.rb start # generate overviews on demand, just send changed data to browser

.. include:: /install/includes/firewall-and-selinux.rst

.. include:: /install/includes/next-steps.rst
