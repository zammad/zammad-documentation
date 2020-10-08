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