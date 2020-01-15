Install on CentOS via RPM
*************************

.. note:: Currently we support RHEL7 & CentOS7.

Prerequisites
=============

Setup Elasticsearch
-------------------

Elasticsearch is a dependency of Zammad and needs to be provided before installing Zammad.
Please take a look at the following page: :doc:`/install/elasticsearch` .


Add Zammad-Repo and Install Zammad
==================================

.. code-block:: sh

   $ sudo yum -y install epel-release wget
   $ sudo wget -O /etc/yum.repos.d/zammad.repo https://dl.packager.io/srv/zammad/zammad/stable/installer/el/7.repo

   $ sudo yum -y install zammad


SeLinux & Firewalld
-------------------

On Centos SeLinux & Firewalld are possibly enabled.
To get everything work you have to use the following commands:

.. code-block:: sh

   $ setsebool httpd_can_network_connect on -P
   $ firewall-cmd --zone=public --add-service=http --permanent
   $ firewall-cmd --zone=public --add-service=https --permanent
   $ firewall-cmd --reload



Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.


Change your webserver configuration (non localhost connections):
----------------------------------------------------------------

Add your fully qualified domain name or public IP to server name directive in your web server configuration and restart your web server.
The installer will give you a hint where Zammad's web server config file is located.

nginx
-----

.. warning:: Please **do not rename** the webserver config file for nginx or apache.
  The update process will re create it, if it does not exist!

::

   # /etc/nginx/conf.d/zammad.conf

   server {
       listen 80;

       # replace 'localhost' with your fqdn if you want to use zammad from remote
       server_name localhost;


You can manage the Zammad services manually:
============================================

Zammad
------

.. code-block:: sh

   $ sudo systemctl status zammad
   $ sudo systemctl stop zammad
   $ sudo systemctl start zammad
   $ sudo systemctl restart zammad

Only web application server
---------------------------

.. code-block:: sh

   $ sudo systemctl status zammad-web
   $ sudo systemctl stop zammad-web
   $ sudo systemctl start zammad-web
   $ sudo systemctl restart zammad-web

Only worker process
-------------------

.. code-block:: sh

   $ sudo systemctl status zammad-worker
   $ sudo systemctl stop zammad-worker
   $ sudo systemctl zammad-worker
   $ sudo systemctl restart zammad-worker

Only websocket server
---------------------

.. code-block:: sh

   $ sudo systemctl status zammad-websocket
   $ sudo systemctl stop zammad-websocket
   $ sudo systemctl start zammad-websocket
   $ sudo systemctl restart zammad-websocket
