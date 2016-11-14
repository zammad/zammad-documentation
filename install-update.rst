Updating Zammad
***************

Source update
=============

1. Download Zammad on your system
---------------------------------

You can directly download Zammad from https://ftp.zammad.com/ or use the direct url to get the latest stable release via https://ftp.zammad.com/zammad-latest.tar.gz

::

 root@shell> wget https://ftp.zammad.com/zammad-latest.tar.gz
 root@shell> cd /opt/
 root@shell> tar -xzf zammad-latest.tar.gz
 root@shell> chown -R zammad /opt/zammad
 root@shell> su - zammad

2. Install all dependencies
---------------------------

::

 zammad@shell> cd zammad
 zammad@shell> gem install bundler

# For PostgreSQL (note, the option says "without ... mysql")::
 zammad@shell> bundle install --without test development mysql

# For MySQL (note, the option says "without ... postgres")::
 zammad@shell> bundle install --without test development postgres

3. Stop zammad services
-----------------------

Stop the application server, websocket server and scheduler.

4. Upgrade your database
------------------------

::

 zammad@shell> export RAILS_ENV=production
 zammad@shell> export RAILS_SERVE_STATIC_FILES=true # only if you use no http reverse proxy
 zammad@shell> rake db:migrate

5. Start zammad services
------------------------

Start the application server, websocket server and scheduler.

6. Go and login to Zammad
-------------------------



DEB update
==========

::

 apt-get update
 apt-get upgrade



RPM update
==========

::

 yum update


