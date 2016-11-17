Install on Ubuntu via DEB
*************************

Currently we support Ubuntu 16.04


Add Zammad DEB Repo and install
===============================

::

 wget -qO - https://deb.packager.io/key | sudo apt-key add -
 echo "deb https://deb.packager.io/gh/zammad/zammad xenial stable" | sudo tee /etc/apt/sources.list.d/zammad.list
 sudo apt update
 sudo apt install zammad


Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.


You can manage the Zammad services manually:
============================================

Zammad
------

::

 sudo systemctl zammad status
 sudo systemctl zammad stop
 sudo systemctl zammad start
 sudo systemctl zammad restart

Only web application server
---------------------------

::

 sudo systemctl zammad-web status
 sudo systemctl zammad-web stop
 sudo systemctl zammad-web start
 sudo systemctl zammad-web restart

Only worker process
-------------------

::

 sudo systemctl zammad-worker status
 sudo systemctl zammad-worker stop
 sudo systemctl zammad-worker start
 sudo systemctl zammad-worker restart

Only websocket server
---------------------

::

 sudo systemctl zammad-websocket status
 sudo systemctl zammad-websocket stop
 sudo systemctl zammad-websocket start
 sudo systemctl zammad-websocket restart


