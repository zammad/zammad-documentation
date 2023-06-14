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

.. include:: /install/includes/postgres-installation.rst

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

   .. tab:: OpenSUSE

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

.. include:: /install/includes/postgres-dependencies.rst

Step 3: Configure database settings
-----------------------------------

.. include:: /install/includes/postgres-permissions.rst

.. code-block:: sh

   $ cp config/database/database.yml config/database.yml
   $ vi config/database.yml

Here's a sample configuration to give you an idea on how your configuration 
file could look like. Please also have a look at 
:doc:`/appendix/configure-database-server` for deeper details.

   .. code-block:: yaml

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

.. hint:: 

   If you want to use an existing database server that's not on the same 
   machine, you can also use ``host`` and ``port`` to set that up.

.. include:: /install/source/include-chmod-database-yml.rst

Step 4: Initialize your database
--------------------------------

.. warning::

   Ensure to do this as ``zammad`` user in your Zammad directory!

.. tip::

   **🤓 Avoid a restart ...**

   You can set the base URL of your Zammad installation by setting the
   ``ZAMMAD_HTTP_TYPE`` and ``ZAMMAD_FQDN`` environment variables before
   initializing the database (see below).

   .. code-block:: sh

      # Example for a base URL of https://zammad.example.com
      $ su - zammad
      $ export ZAMMAD_HTTP_TYPE=https
      $ export ZAMMAD_FQDN=zammad.example.com

.. code-block:: sh

   $ su - zammad
   $ rake db:create      # SKIP IF you already created zammads database (see tip of step 3)
   $ rake db:migrate
   $ rake db:seed
   # Synchronize translations
   $ rails r "Locale.sync"
   $ rails r "Translation.sync"

Step 5: Pre compile all Zammad assets
-------------------------------------

.. code-block:: sh

   $ rake assets:precompile

.. _source-install-systemd-reference:

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

      .. warning:: 

        This method is not suitable for production use - you should avoid it.

      .. code-block:: sh

         $ rails s -p 3000 # application web server
         $ script/websocket-server.rb start # non blocking websocket server
         $ script/background-worker.rb start # generate overviews on demand, just send changed data to browser

      .. danger::

         ⚠️ Zammads background worker *cannot* run in daemon mode!

.. include:: /install/includes/manage-services.rst

.. include:: /install/includes/firewall-and-selinux.rst

.. include:: /install/includes/next-steps.rst
