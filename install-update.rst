Updating Zammad
***************

Source update
=============

**Note: Please backup your Zammad instance before update!**

1. Download Zammad on your system
---------------------------------

You can directly download Zammad from https://ftp.zammad.com/ or use the direct url to get the latest stable release via https://ftp.zammad.com/zammad-latest.tar.gz

::

 root@shell> wget https://ftp.zammad.com/zammad-latest.tar.gz
 root@shell> cd /opt/
 root@shell> tar -xzf zammad-latest.tar.gz
 root@shell> chown -R zammad /opt/zammad
 root@shell> su - zammad

2. Install all dependencies
---------------------------

::

 zammad@shell> cd zammad
 zammad@shell> gem install bundler

* For PostgreSQL (note, the option says "without ... mysql")::

 zammad@shell> bundle install --without test development mysql

* For MySQL (note, the option says "without ... postgres")::

 zammad@shell> bundle install --without test development postgres


3. Stop zammad services
-----------------------

Stop the application server, websocket server and scheduler.

4. Upgrade your database
------------------------

::

 zammad@shell> export RAILS_ENV=production
 zammad@shell> export RAILS_SERVE_STATIC_FILES=true # only if you use no http reverse proxy
 zammad@shell> rake db:migrate

5. Start zammad services
------------------------

Start the application server, websocket server and scheduler.

6. Go and login to Zammad
-------------------------



Update with RPM
===============

**Note: Please backup your Zammad instance before update!**

During development we reorganized our repo structure. Please update your /etc/yum.repos.d/zammad.repo with the
correct baseurl (see below).

1. Verify repo baseurl
----------------------

CentOS7
+++++++


::

 echo "[zammad]
 name=Repository for zammad/zammad application.
 baseurl=https://rpm.packager.io/gh/zammad/zammad/centos7/stable
 enabled=1" | sudo tee /etc/yum.repos.d/zammad.repo


2. Update Zammad
----------------

::

 shell> sudo yum update zammad


Note: The package will automatically execute maintanance task like database changes and Zammad restart.


3. Go and login to Zammad
-------------------------



Update with DEB
===============


**Note: Please backup your Zammad instance before update!**


During development we reorganized our repo structure. Please update your /etc/yum.repos.d/zammad.repo with the
correct baseurl (see below).

1. Verify repo baseurl
----------------------

Debian
++++++

::

 echo "deb https://deb.packager.io/gh/zammad/zammad jessie stable" | sudo tee /etc/apt/sources.list.d/zammad.list


Ubuntu
++++++

::

 echo "deb https://deb.packager.io/gh/zammad/zammad xenial stable" | sudo tee /etc/apt/sources.list.d/zammad.list


2. Update Zammad
----------------

::

  shell> apt-get update
  shell> apt-get upgrade


Note: The package will automatically execute maintanance task like database changes and Zammad restart.


3. Go and login to Zammad
-------------------------