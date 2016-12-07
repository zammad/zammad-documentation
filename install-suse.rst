Install on SUSE via RPM
***********************

Currently we support SLES 12 and OpenSUSE 42.2

Install dependencies
====================

On SLES12
---------

::

 sudo zypper addrepo "http://nginx.org/packages/sles/12" "nginx"


Add Zammad RPM repo and install
===============================

::

 sudo rpm --import https://rpm.packager.io/key
 sudo zypper addrepo "https://rpm.packager.io/gh/zammad/zammad/sles12/stable" "zammad"
 sudo zypper install zammad



Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.

Note: Make sure that the firewall is not blocking port 80 (configure firewall via "yast firewall" or stop it via "systemctl stop SuSEfirewall2").


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
 sudo systemctl zammad-worker
 sudo systemctl restart zammad-worker

Only websocket server
---------------------

::

 sudo systemctl status zammad-websocket
 sudo systemctl stop zammad-websocket
 sudo systemctl start zammad-websocket
 sudo systemctl restart zammad-websocket

