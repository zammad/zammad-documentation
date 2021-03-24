Install from source on MacOS
****************************

.. note:: **🙀 Outdated documentation**

   Sorry, but this documentation part is outdated. 
   We decided not to remove this part to provide at least hints for MacOS.

   Please feel welcome to provide a pull request if you find spare time!

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
