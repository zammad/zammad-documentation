Configure the webserver of your choice
======================================

You can find current configuration files for your webserver within ``contrib/`` of 
your Zammad installation.

If you're using the package installation, Zammad attempts to automatically install 
a configuration file fo you (``/etc/nginx/sites-enabled/zammad.conf``).

.. note:: The Zammad installation will not automatically set any host- or server name for you.


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