Install on Ubuntu via DEB
*************************

Currently we support Ubuntu 16.04


Prerequisites
=============

Be sure to use an UTF-8 locale or PostgreSQL will not install.

Check locale
------------

::

 locale

If there is nothing with UTF-8 in the name shown like "LANG=en_US.UTF-8" you have to set a new locale.

Set locale
----------

::

 apt-get install locales
 locale-gen en_US.UTF-8
 echo "LANG=en_US.UTF-8" > /etc/default/locale


Add Zammad DEB Repo and install
===============================

::

sudo apt-key adv --keyserver http://dl.packager.io/srv/zammad/zammad/key \
  --recv-keys 6257DF9972462F57A20FFB2AB6D583CCBD33EEB8
sudo wget -O /etc/apt/sources.list.d/zammad.list \
  https://dl.packager.io/srv/zammad/zammad/develop/installer/ubuntu/16.04.repo
apt-get install wget apt-transport-https
sudo apt-get update
sudo apt-get install zammad


Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.


On remote server:
=================

Add your fully qualified domain name or public IP to server name directive in your web server configuration and restart your web server.
The installer will give you a hint where Zammad's web server config file is located.


You can manage the Zammad services manually:
============================================

Zammad
------

::

 sudo systemctl status zammad
 sudo systemctl stop zammad
 sudo systemctl start zammad
 sudo systemctl restart zammad

Only web application server
---------------------------

::

 sudo systemctl status zammad-web
 sudo systemctl stop zammad-web
 sudo systemctl start zammad-web
 sudo systemctl restart zammad-web

Only worker process
-------------------

::

 sudo systemctl status zammad-worker
 sudo systemctl stop zammad-worker
 sudo systemctl start zammad-worker
 sudo systemctl restart zammad-worker

Only websocket server
---------------------

::

 sudo systemctl status zammad-websocket
 sudo systemctl stop zammad-websocket
 sudo systemctl start zammad-websocket
 sudo systemctl restart zammad-websocket
