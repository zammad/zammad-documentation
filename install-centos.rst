Install on CentOS via RPM
*************************

Currently we support RHEL6/CentOS6 and RHEL7/CentOS7.


Add Zammad & epel-release RPM repos and install RPM
===================================================

::

 sudo yum install epel-release
 sudo rpm --import https://rpm.packager.io/key

CentOS7
-------

::

 echo "[zammad]
 name=Repository for zammad/zammad application.
 baseurl=https://rpm.packager.io/gh/zammad/zammad/centos7/stable
 enabled=1" | sudo tee /etc/yum.repos.d/zammad.repo

CentOS6
-------

::

 echo "[zammad]
 name=Repository for zammad/zammad application.
 baseurl=https://rpm.packager.io/gh/zammad/zammad/centos6/stable
 enabled=1" | sudo tee /etc/yum.repos.d/zammad.repo


Install Zammad
==============

::

 sudo yum install zammad


Go to http://localhost:3000 and you'll see:
===========================================

* "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.


You can manage the Zammad services manually:
===========================================

Zammad
------

::

 sudo service status zammad
 sudo service stop zammad
 sudo service start zammad
 sudo service restart zammad

Only web application server
---------------------------

::

 sudo service status zammad-wew
 sudo service stop zammad-web
 sudo service start zammad-web
 sudo service restart zammad-web

Only worker process
-------------------

::

 sudo service status zammad-worker
 sudo service stop zammad-worker
 sudo service zammad-worker
 sudo service restart zammad-worker

Only websocket server
---------------------

::

 sudo service status zammad-websocket
 sudo service stop zammad-websocket
 sudo service start zammad-websocket
 sudo service restart zammad-websocket


