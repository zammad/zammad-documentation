Configure the webserver of your choice
======================================

You can find current sample configuration files for your webserver within ``contrib/`` of 
your Zammad installation.

If you're using the package installation, Zammad attempts to automatically install 
a configuration file to your nginx for you.

.. note:: The Zammad installation will not automatically set any host- or server name for you.

Adjusting the webserver configuration
-------------------------------------

.. warning:: For a quick start, we're installing a HTTP configuration. 
   You should **never** use HTTP connections for authentication - instead, we encourage you to use HTTPS!

   If Zammad scripts automatically installed your webserver configuration file, ensure to not rename it.

... for nginx (default)
   In order to access Zammad from external open Zammads vHost configuration 
   (``/etc/nginx/sites-enabled/zammad.conf`` - your path may differ).

   Locate any ``server_name`` directive and adjust ``example.com`` to the subdomain you have chosen for 
   your Zammad instance.  

   After you made your required changes, don't forget to reload your nginx: ``systemctl reload nginx``.

... for apache2
   In order to access Zammad from external open Zammads vHost configuration 
   (``/etc/apache/sites-enabled/zammad.conf`` - your path may differ).

   Locate any ``ServerName`` directives and adjust them to your chosen subdomain. 

      .. hint:: **🧐 Ensure all required modules are enabled:**

         * proxy
         * proxy_html
         * proxy_http
         * proxy_wstunnel
         * headers

... for local testing or other Proxies
   Want to test locally first or use a different Proxy we don't support?
   The main application (rails server) is listening on ``http://localhost:3000``.

   If you're using a proxy server, also ensure that you proxy the websockets as well. 
   The websocket server listens on ``ws://localhost:6042``.

   .. tip:: If above ports are used by other applications already you may want to have a look
      at :ref:`network options <network_options>` on our environment page.

... using SSL
   Don't know how to get SSL certificates and install them on a webserver yet?
   Have a look on the :ref:`getting SSL certificates <getting_ssl>` section.


**If you just installed Zammad, you'll be greeted by our installation wizard. 🙌**

   .. figure:: /images/install/getting-started-wizard.png
      :alt: Getting started wizard after installing Zammad
      :width: 90%
      :align: center