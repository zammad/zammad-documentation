Install with DEB
****************

Currently we support Debian 8 & Ubuntu 16.04


Add Zammad DEB Repo and install
===============================

::

 wget -qO - https://deb.packager.io/key | sudo apt-key add -

Debian:
-------

::

 echo "deb https://deb.packager.io/gh/zammad/zammad jessie stable" | sudo tee /etc/apt/sources.list.d/zammad.list

Ubuntu:
-------

::

 echo "deb https://deb.packager.io/gh/zammad/zammad xenial stable" | sudo tee /etc/apt/sources.list.d/zammad.list

::

 sudo apt-get update
 sudo apt-get install zammad

Start Zammad services:
======================

::

 sudo systemctl zammad start

You can manage the Zammad services manually:
--------------------------------------------

::

 sudo systemctl zammad status
 sudo systemctl zammad stop
 sudo systemctl zammad start
 sudo systemctl zammad restart

only web application server
---------------------------

::

 sudo systemctl zammad-web status
 sudo systemctl zammad-web stop
 sudo systemctl zammad-web start
 sudo systemctl zammad-web restart

only worker process
-------------------

::

 sudo systemctl zammad-worker status
 sudo systemctl zammad-worker stop
 sudo systemctl zammad-worker start
 sudo systemctl zammad-worker restart

only websocket server
---------------------

::

 sudo systemctl zammad-websocket status
 sudo systemctl zammad-websocket stop
 sudo systemctl zammad-websocket start
 sudo systemctl zammad-websocket restart


Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.
