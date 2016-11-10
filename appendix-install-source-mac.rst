Install from source for developers (Mac OS 10.8)
************************************************

Prerequisites
=============

* Install Xcode from the App Store, open it -> Xcode menu > Preferences > Downloads -> install command line tools

::

 curl -L https://get.rvm.io | bash -s stable --ruby
 source ~/.rvm/scripts/rvm
 start new shell -> ruby -v

Get Zammad
==========

::

 test -d ~/zammad/ || mkdir ~/zammad
 cd ~/zammad/
 curl -L -O https://ftp.zammad.com/zammad-latest.tar.bz2 | tar -xj


Install Zammad
==============

::

 cd zammad-latest
 bundle install
 sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib # if needed!
 rake db:create
 rake db:migrate
 rake db:seed


Database connect
================

::

 cd zammad-latest
 cp config/database.yml.dist config/database.yml
 rake db:create
 rake db:migrate
 rake db:seed

Start Zammad
============

::

 puma -p 3000 # application web server
 script/websocket-server.rb start # non blocking websocket server
 script/scheduler.rb start # generate overviews on demand, just send changed data to browser


Visit Zammad in your browser page
=================================

* http://localhost:3000/#getting_started

