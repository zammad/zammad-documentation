Install on Suse via RPM
***********************

Currently we support SLES 12 and Opensuse 42.2

Add Zammad RPM repo and install
===============================

::

 sudo rpm --import https://rpm.packager.io/key
 sudo zypper addrepo "https://rpm.packager.io/gh/zammad/zammad/sles12/stable" "zammad"
 sudo zypper install zammad


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

 sudo systemctl zammad-wew status
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

