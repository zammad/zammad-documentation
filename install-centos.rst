Install on CentOS via RPM
*************************

Currently we support RHEL7 & CentOS7.


Add Zammad, Elasticsearch & epel-release RPM repos and install RPM
==================================================================

::

 sudo yum -y install epel-release wget
 sudo wget -O /etc/yum.repos.d/zammad.repo https://dl.packager.io/srv/zammad/zammad/stable/installer/el/7.repo

 echo "[elasticsearch-5.x]
 name=Elasticsearch repository for 5.x packages
 baseurl=https://artifacts.elastic.co/packages/5.x/yum
 gpgcheck=1
 gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
 enabled=1
 autorefresh=1
 type=rpm-md" | sudo tee /etc/yum.repos.d/elasticsearch.repo

 sudo yum -y install java elasticsearch
 sudo systemctl daemon-reload
 sudo systemctl enable elasticsearch
 sudo systemctl start elasticsearch

 sudo yum -y install zammad


SeLinux & Firewalld
===================

On Centos SeLinux & Firewalld are possibly enabled. 
To get everything work you have to use the following commands:

::

 setsebool httpd_can_network_connect on -P
 firewall-cmd --zone=public --add-service=http --permanent
 firewall-cmd --zone=public --add-service=https --permanent
 firewall-cmd --reload



Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.
 
+**Note** You should be sure that no other webserver is blocking port 80. Otherwise, this will not work.

Change your webserver configuration (non localhost connections):
================================================================

Add your fully qualified domain name or public IP to server name directive in your web server configuration and restart your web server.
The installer will give you a hint where Zammad's web server config file is located.

nginx
--------

*/etc/nginx/conf.d/zammad.conf*

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
