Install on Ubuntu via DEB
*************************

Prerequisites
=============

Be sure to use an UTF-8 locale or PostgreSQL will not install.


Setup Elasticsearch
-------------------

https://docs.zammad.org/en/latest/install-elasticsearch.html#ubuntu-18-04


Check locale
------------

::

 locale

If there is nothing with UTF-8 in the name shown like "LANG=en_US.UTF-8" you have to set a new locale.

Set locale
----------

::

 apt-get install apt-transport-https locales sudo wget
 locale-gen en_US.UTF-8
 echo "LANG=en_US.UTF-8" > /etc/default/locale


Add Zammad DEB Repo and install
===============================

::

 wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
 sudo wget -O /etc/apt/sources.list.d/zammad.list \
   https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/18.04.repo
 sudo apt-get update
 sudo apt-get install zammad

Note: You might need to apt-get install wget apt-transport-https for the above instructions to work.


Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.


Change your webserver configuration (non localhost connections):
=================

Add your fully qualified domain name or public IP to server name directive in your web server configuration and restart your web server.
The installer will give you a hint where Zammad's web server config file is located.

nginx
--------

*/etc/nginx/sites-enabled/zammad.conf*

::

 server {
     listen 80;

     # replace 'localhost' with your fqdn if you want to use zammad from remote
     server_name localhost;


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
