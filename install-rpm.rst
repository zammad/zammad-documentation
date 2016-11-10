Install with RPM
****************

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
 baseurl=https://rpm.packager.io/gh/zammad/zammad/centos7/package-1.0
 enabled=1" | sudo tee /etc/yum.repos.d/zammad.repo


CentOS6
-------

::

 echo "[zammad]
 name=Repository for zammad/zammad application.
 baseurl=https://rpm.packager.io/gh/zammad/zammad/centos6/package-1.0
 enabled=1" | sudo tee /etc/yum.repos.d/zammad.repo

::

 sudo yum install zammad


Configure your databases
========================

The example uses PostgreSQL (we also support MySQL/MariaDB).

Get a fresh database server up and running:
-------------------------------------------

::

 sudo postgresql-setup initdb
 sudo systemctl start postgresql.service
 sudo systemctl enable postgresql.service
 sudo -u postgres createuser --interactive
 sudo -u postgres createuser -d zammad


Check config for database connection in /opt/zammad/config/database.yml
-----------------------------------------------------------------------

::

 production:
   adapter: postgresql
   database: zammad_production
   pool: 50
   timeout: 5000
   encoding: utf8
   username: zammad
   password:


Initialize your database
========================

::

 sudo zammad run rake db:create
 sudo zammad run rake db:migrate
 sudo zammad run rake db:seed


Start Zammad services:
======================

Generate init scripts for your platform and start Zammad services:
------------------------------------------------------------------

::

 sudo zammad scale web=1 worker=1 websocket=1

Start Zammad services at boot:
------------------------------

::

 sudo chkconfig zammad on

You can manage the Zammad services manually:
--------------------------------------------

::

 sudo service zammad status
 sudo service zammad stop
 sudo service zammad start
 sudo service zammad restart

only web application server
---------------------------

::

 sudo service zammad-web status
 sudo service zammad-web stop
 sudo service zammad-web start
 sudo service zammad-web restart

only worker process
-------------------

::

 sudo service zammad-worker status
 sudo service zammad-worker stop
 sudo service zammad-worker start
 sudo service zammad-worker restart

only websocket server
---------------------

::

 sudo service zammad-websocket status
 sudo service zammad-websocket stop
 sudo service zammad-websocket start
 sudo service zammad-websocket restart


Go to http://localhost:3000 and you'll see:
===========================================

* "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.
