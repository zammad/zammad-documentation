Install on CentOS via RPM
*************************

Currently we support RHEL7 & CentOS7.


Add Zammad & epel-release RPM repos and install RPM
===================================================

::

 sudo yum install epel-release
 sudo rpm --import https://rpm.packager.io/key
 echo "[zammad]
 name=Repository for zammad/zammad application.
 baseurl=https://rpm.packager.io/gh/zammad/zammad/centos7/stable
 enabled=1" | sudo tee /etc/yum.repos.d/zammad.repo
 sudo yum install zammad


Go to http://localhost:3000 and you'll see:
===========================================

* "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.


You can manage the Zammad services manually:
===========================================

Zammad
------

::

 sudo service zammad status
 sudo service zammad stop
 sudo service zammad start
 sudo service zammad restart

Only web application server
---------------------------

::

 sudo service zammad-wew status
 sudo service zammad-web stop
 sudo service zammad-web start
 sudo service zammad-web restart

Only worker process
-------------------

::

 sudo service zammad-worker status
 sudo service zammad-worker stop
 sudo service zammad-worker start
 sudo service zammad-worker restart

Only websocket server
---------------------

::

 sudo service zammad-websocket status
 sudo service zammad-websocket stop
 sudo service zammad-websocket start
 sudo service zammad-websocket restart


