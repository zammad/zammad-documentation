Install on SUSE via RPM
***********************

.. note:: Currently we support SLES 12 and OpenSUSE with versions 42.2 and 42.3

.. warning:: OpenSUSE LEAP 15.0 hasn't been tested yet, but should work as well.


Install dependencies
====================

Setup Elasticsearch
-------------------

Elasticsearch is a dependency of Zammad and needs to be provided before installing Zammad.
Please take a look at the following page: :doc:`/install/elasticsearch` .


nginx on SLES12
---------------

.. code-block:: sh

   $ sudo zypper addrepo "http://nginx.org/packages/sles/12" "nginx"


Add Zammad RPM repo and install
===============================

.. code-block:: sh

   $ sudo zypper install wget
   $ sudo wget -O /etc/zypp/repos.d/zammad.repo https://dl.packager.io/srv/zammad/zammad/stable/installer/sles/12.repo
   $ sudo zypper install zammad



Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.

Note: Make sure that the firewall is not blocking port 80 (configure firewall via "yast firewall" or stop it via "systemctl stop SuSEfirewall2").


Change your webserver configuration (non localhost connections):
================================================================

Add your fully qualified domain name or public IP to server name directive in your web server configuration and restart your web server.
The installer will give you a hint where Zammad's web server config file is located.

nginx
--------

.. warning:: Please **do not rename** the webserver config file for nginx or apache.
   The update process will re create it, if it does not exist!


::

   # /etc/nginx/sites-enabled/zammad.conf

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
