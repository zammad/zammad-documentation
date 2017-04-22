Install on Debian via DEB
*************************

Currently we support Debian 8

Prerequisites
=============

Be sure to use an  UTF-8 locale or PostgreSQL will not install.

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

 wget -qO - https://deb.packager.io/key | sudo apt-key add -
 echo "deb https://deb.packager.io/gh/zammad/zammad jessie stable" | sudo tee /etc/apt/sources.list.d/zammad.list
 sudo apt-get update
 sudo apt-get install zammad


Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.


On remote server:
=================

Add your FQDN to servername directive in /etc/nginx/conf.d/zammad.conf and restart your webserver.


You can manage the Zammad services manually:
============================================

Zammad
------

::

 sudo systemctl status zammad
 sudo systemctl stop zammad
 sudo systemctl start zammad
 sudo systemctl restart zammad

only web application server
---------------------------

::

 sudo systemctl status zammad-web
 sudo systemctl stop zammad-web
 sudo systemctl start zammad-web
 sudo systemctl restart zammad-web

only worker process
-------------------

::

 sudo systemctl status zammad-worker
 sudo systemctl stop zammad-worker
 sudo systemctl start zammad-worker
 sudo systemctl restart zammad-worker

only websocket server
---------------------

::

 sudo systemctl status zammad-websocket
 sudo systemctl stop zammad-websocket
 sudo systemctl start zammad-websocket
 sudo systemctl restart zammad-websocket
