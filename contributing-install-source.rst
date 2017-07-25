Install from source
*******************

Install from source (Debian 7, 8 / Ubuntu 16.04)
===============================================

With Nginx & MySQL
------------------

Prerequisites
+++++++++++++

::

 apt-get install curl git-core patch build-essential bison zlib1g-dev libssl-dev libxml2-dev libxml2-dev sqlite3 libsqlite3-dev autotools-dev libxslt1-dev libyaml-0-2 autoconf automake libreadline6-dev libyaml-dev libtool libgmp-dev libgdbm-dev libncurses5-dev pkg-config libffi-dev libmysqlclient-dev mysql-server nginx gawk

Add User
++++++++

::

 useradd zammad -m -d /opt/zammad -s /bin/bash
 echo "export RAILS_ENV=production" >> /opt/zammad/.bashrc


Create MySQL user zammad (for Debian: upgrade MySQL to v5.6+ before, see: http://dev.mysql.com/downloads/repo/apt/)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

 mysql --defaults-extra-file=/etc/mysql/debian.cnf -e "CREATE USER 'zammad'@'localhost' IDENTIFIED BY 'Your_Pass_Word!'; GRANT ALL PRIVILEGES ON zammad_prod.* TO 'zammad'@'localhost'; FLUSH PRIVILEGES;"

Get Zammad
++++++++++

::

 su zammad
 cd ~
 curl -O https://ftp.zammad.com/zammad-latest.tar.gz
 tar -xzf zammad-latest.tar.gz
 exit

Create Nginx Config
+++++++++++++++++++

::

 cp /opt/zammad/contrib/nginx/zammad.conf /etc/nginx/sites-available/zammad.conf

* change servername "localhost" to your domain if your're not testing localy

::

 vi /etc/nginx/sites-available/zammad.conf

::

 ln -s /etc/nginx/sites-available/zammad.conf /etc/nginx/sites-enabled/zammad.conf

Install environnment
++++++++++++++++++++

::

 su zammad
 cd ~
 gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
 curl -L https://get.rvm.io | bash -s stable
 source /opt/zammad/.rvm/scripts/rvm
 echo "source /opt/zammad/.rvm/scripts/rvm" >> /opt/zammad/.bashrc
 echo "rvm --default use 2.3.1" >> /opt/zammad/.bashrc
 rvm install 2.3.1
 gem install bundler

Install Zammad
++++++++++++++

::

 bundle install --without test development postgres
 cp config/database.yml.pkgr config/database.yml

* insert mysql user, pass & change adapter to mysql2

::

 vi config/database.yml

::

 rake db:create
 rake db:migrate
 rake db:seed
 rake assets:precompile

Start Zammad
++++++++++++

::

 rails s -p 3000 &>> log/zammad.log &
 script/websocket-server.rb start &>> log/zammad.log &
 script/scheduler.rb start &>> log/zammad.log &

Restart nginx as root
+++++++++++++++++++++

::

 exit
 systemctl restart nginx

Go to http://localhost and you'll see:
++++++++++++++++++++++++++++++++++++++

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.


Install from source (Mac OS 10.8)
=================================

Prerequisites
-------------

* Install Xcode from the App Store, open it -> Xcode menu > Preferences > Downloads -> install command line tools

::

 curl -L https://get.rvm.io | bash -s stable --ruby
 source ~/.rvm/scripts/rvm
 start new shell -> ruby -v

Get Zammad
----------

::

 test -d ~/zammad/ || mkdir ~/zammad
 cd ~/zammad/
 curl -L -O https://ftp.zammad.com/zammad-latest.tar.bz2 | tar -xj


Install Zammad
--------------

::

 cd zammad-latest
 bundle install
 sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib # if needed!
 rake db:create
 rake db:migrate
 rake db:seed


Database connect
----------------

::

 cd zammad-latest
 cp config/database.yml.dist config/database.yml
 rake db:create
 rake db:migrate
 rake db:seed

Start Zammad
------------

::

 puma -p 3000 # application web server
 script/websocket-server.rb start # non blocking websocket server
 script/scheduler.rb start # generate overviews on demand, just send changed data to browser


Visit Zammad in your browser
----------------------------

* http://localhost:3000/#getting_started

