Install on CentOS via RPM
*************************

Currently we support RHEL7 & CentOS7.


Add Zammad & epel-release RPM repos and install RPM
===================================================

::

 sudo yum -y install epel-release
 sudo rpm --import https://rpm.packager.io/key
 echo "[zammad]
 name=Repository for zammad/zammad application.
 baseurl=https://rpm.packager.io/gh/zammad/zammad/centos7/stable
 enabled=1" | sudo tee /etc/yum.repos.d/zammad.repo
 sudo yum -y install zammad


Go to http://localhost and you'll see:
===========================================

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.


Change your webserver configuration (non localhost connections):
=================

Add your fully qualified domain name or public IP to server name directive in your web server configuration and restart your web server.
The installer will give you a hint where Zammad's web server config file is located.

nginx
^^^^^^^^^^^^^^^^^

*/etc/nginx/sites-enabled/zammad.conf*

::

 server {
     listen 80;

     # replace 'localhost' with your fqdn if you want to use zammad from remote
     server_name localhost;


You can manage the Zammad services manually:
===========================================

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
