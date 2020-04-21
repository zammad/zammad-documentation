Install from source
*******************

Generic
=======

Setup Elasticsearch
-------------------

Elasticsearch is a dependency of Zammad and needs to be provided before installing Zammad.
Please take a look at the following page: :doc:`/install/elasticsearch` .


1. Install Zammad on your system
--------------------------------

You can directly download Zammad from https://ftp.zammad.com/ or use the direct URL to get the latest stable release via https://ftp.zammad.com/zammad-latest.tar.gz

.. code-block:: sh

   $ sudo useradd zammad -m -d /opt/zammad -s /bin/bash
   $ cd /opt
   $ sudo wget https://ftp.zammad.com/zammad-latest.tar.gz
   $ sudo tar -xzf zammad-latest.tar.gz -C zammad
   $ sudo su - zammad


2. Install all dependencies
---------------------------

Please note that a working ruby 2.5.5 environment is needed.

.. code-block:: sh

   zammad@host $ gem install bundler rake rails

For PostgreSQL (note, the option says "without ... mysql")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

   zammad@host $ bundle install --without test development mysql

For MySQL (note, the option says "without ... postgres")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

   zammad@host $ bundle install --without test development postgres


3. Configure your databases
---------------------------

.. code-block:: sh

   zammad@host $ cp config/database/database.yml config/database.yml
   zammad@host $ vi config/database.yml


4. Initialize your database
---------------------------

.. code-block:: sh

   zammad@host $ export RAILS_ENV=production
   zammad@host $ export RAILS_SERVE_STATIC_FILES=true
   zammad@host $ rake db:create
   zammad@host $ rake db:migrate
   zammad@host $ rake db:seed


5. Change directory to zammad (if needed) and start services:
-------------------------------------------------------------

.. code-block:: sh

   zammad@host $ rake assets:precompile

You can start all services by hand or use systemd to start / stop Zammad.

Starting all servers manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

   zammad@host $ rails s -p 3000 # application web server
   zammad@host $ script/websocket-server.rb start # non blocking websocket server
   zammad@host $ script/scheduler.rb start # generate overviews on demand, just send changed data to browser


Starting servers with Systemd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    zammad@host $ cd scripts/systemd
    zammad@host $ sudo ./install-zammad-systemd-services.sh


6. Go to http://localhost:3000 and you'll see:
----------------------------------------------

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.


Reset a Zammad installation (for a fresh start after testing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please note: this actions will delete all existing data! Dont use it on a production system.

.. code-block:: sh

   zammad@host $ sudo systemctl stop zammad
   zammad@host $ rake db:drop
   zammad@host $ rake db:create
   zammad@host $ rake db:migrate
   zammad@host $ rake db:seed
   zammad@host $ sudo systemctl start zammad




on Debian 7, 8 / Ubuntu 16.04 / Ubuntu 18.04 (with Nginx & MySQL)
=================================================================

Prerequisites
-------------

.. code-block:: sh

   $ apt-get update
   $ apt-get install curl git-core patch build-essential bison zlib1g-dev libssl-dev libxml2-dev libxml2-dev sqlite3 libsqlite3-dev autotools-dev libxslt1-dev libyaml-0-2 autoconf automake libreadline6-dev libyaml-dev libtool libgmp-dev libgdbm-dev libncurses5-dev pkg-config libffi-dev libmysqlclient-dev mysql-server nginx gawk libimlib2-dev

Add User
--------

.. code-block:: sh

   $ useradd zammad -m -d /opt/zammad -s /bin/bash
   $ echo "export RAILS_ENV=production" >> /opt/zammad/.bashrc


Create MySQL user zammad (for Debian: upgrade MySQL to v5.6+ before, see: http://dev.mysql.com/downloads/repo/apt/)
-------------------------------------------------------------------------------------------------------------------

.. code-block:: sh

   $ mysql --defaults-extra-file=/etc/mysql/debian.cnf -e "CREATE USER 'zammad'@'localhost' IDENTIFIED BY 'Your_Pass_Word'; GRANT ALL PRIVILEGES ON zammad_prod.* TO 'zammad'@'localhost'; FLUSH PRIVILEGES;"

Get Zammad
----------

.. code-block:: sh

   $ su - zammad
   $ curl -O https://ftp.zammad.com/zammad-latest.tar.gz
   $ tar -xzf zammad-latest.tar.gz
   $ rm zammad-latest.tar.gz


Install environnment
--------------------

.. code-block:: sh

   $ gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
   $ curl -L https://get.rvm.io | bash -s stable
   $ source /opt/zammad/.rvm/scripts/rvm
   $ echo "source /opt/zammad/.rvm/scripts/rvm" >> /opt/zammad/.bashrc
   $ echo "rvm --default use 2.5.5" >> /opt/zammad/.bashrc
   $ rvm install 2.5.5
   $ gem install bundler

Install Zammad
--------------

.. code-block:: sh

   $ bundle install --without test development postgres
   $ cp config/database/database.yml config/database.yml

* insert mysql user, pass & change adapter to mysql2 & change database to zammad_prod

.. code-block:: sh

   $ vi config/database.yml

.. code-block:: sh

   $ rake db:create
   $ rake db:migrate
   $ rake db:seed
   $ rake assets:precompile

Start Zammad
------------

.. code-block:: sh

   $ rails s -p 3000 &>> log/zammad.log &
   $ script/websocket-server.rb start &>> log/zammad.log &
   $ script/scheduler.rb start &>> log/zammad.log &



Create Nginx Config & restart Nginx
-----------------------------------

.. code-block:: sh

   $ exit
   $ cp /opt/zammad/contrib/nginx/zammad.conf /etc/nginx/sites-available/zammad.conf

* change servername "localhost" to your domain if your're not testing localy

.. code-block:: sh

   $ vi /etc/nginx/sites-available/zammad.conf
   $ ln -s /etc/nginx/sites-available/zammad.conf /etc/nginx/sites-enabled/zammad.conf
   $ systemctl restart nginx


Go to http://localhost and you'll see:
--------------------------------------

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.



on Mac OS 10.8
==============

Prerequisites
-------------

* Install Xcode from the App Store, open it -> Xcode menu > Preferences > Downloads -> install command line tools

.. code-block:: sh

   $ curl -L https://get.rvm.io | bash -s stable --ruby
   $ source ~/.rvm/scripts/rvm
   $ start new shell -> ruby -v

Get Zammad
----------

.. code-block:: sh

   $ test -d ~/zammad/ || mkdir ~/zammad
   $ cd ~/zammad/
   $ curl -L -O https://ftp.zammad.com/zammad-latest.tar.bz2 | tar -xj


Install Zammad
--------------

.. code-block:: sh

   $ cd zammad-latest
   $ bundle install
   $ sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib # if needed!
   $ rake db:create
   $ rake db:migrate
   $ rake db:seed


Database connect
----------------

.. code-block:: sh

   $ cd zammad-latest
   $ cp config/database/database.yml config/database.yml
   $ rake db:create
   $ rake db:migrate
   $ rake db:seed

Start Zammad
------------

.. code-block:: sh

   $ puma -p 3000 # application web server
   $ script/websocket-server.rb start # non blocking websocket server
   $ script/scheduler.rb start # generate overviews on demand, just send changed data to browser


Visit Zammad in your browser
----------------------------

* http://localhost:3000/#getting_started
