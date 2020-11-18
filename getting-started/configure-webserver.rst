Configure the webserver
=======================

You can find current sample configuration files for your webserver within ``contrib/`` of 
your Zammad installation.

If you're using the package installation, Zammad attempts to automatically install 
a configuration file to your nginx for you.

.. note:: The Zammad installation will not automatically set any host- or server name for you.

Get a ssl certificate (recommended)
-----------------------------------

Don't know how to get SSL certificates and install them on a webserver yet?
The guide within the tabs below can help you jumping in.

.. tabs::
   
   .. tab:: I don't need that

      You either already know what you're doing, you're developing or like the danger. 🐱‍👤

   .. tab:: letsencrypt

      letsencrypt is an easy and free way to retreive valid ssl certificates.
      These certificates are valid for 90 days and can be renewed automatically.

      The two most common tools are `certbot <https://certbot.eff.org/instructions>`_ 
      and `acme.sh <https://github.com/acmesh-official/acme.sh>`_.

      .. tabs::

         .. tab:: certbot

            .. hint:: If not happened automatically, you may need to install the nginx or apache plugin for certbot:
               ``python3-certbot-nginx`` OR ``python3-certbot-apache``

            During the first certbot run it will request additional information once.
            Replace ``<webserver>`` in below command by either ``apache``, ``httpd`` or ``nginx`` 
            and to match your setup.
            
            .. code-block:: sh

               certbot --<webserver> -d zammad.example.com

            Certbot will now attempt to issue a certificate for you. 
            If successful, certbot will ask you if you want to ``[1] not redirect`` or ``[2] redirect`` automatically.
            You can choose to not redirect **if** you plan to use the sample configuration of Zammad. 
            If not, select ``[2] redirect``.

            From this moment on, certbot will automatically renew your installed certificates if they're valid for 
            another 30 days or less.

               .. hint:: **👀 Not exactly what you're looking for?**

                  The `cerbot documentation <https://certbot.eff.org/docs/using.html#certbot-commands>`_ has alot 
                  more use cases than we cover here.

         .. tab:: acme.sh

            .. hint:: The most reliable way is to use the standalone method.

            First of all you'll need to issue your certificate. 
            acme.sh will save this certificate to ``/root/.acme.sh/<your-domain>/``

            .. code-block:: sh

                acme.sh --issue --standalone -d zammad.example.com


            It's not recommended to use the just stored certificates directly. 
            Instead you should install the certificate to a directory of your choice. 

            We're using ``/etc/ssl/private/`` in this case, but you can use any directory you like. 

               .. warning:: Ensure to adjust value for ``--reloadcmd`` as this will ensure that acme.sh 
                  reloads your webserver automatically after getting a renewal. Replace ``<webserver>`` 
                  by either ``apache2``, ``httpd`` or ``nginx``

            .. code-block:: sh

               acme.sh --install-cert -d zammad.example.com \
               --cert-file      /etc/ssl/private/zammad.example.com.pem  \
               --key-file       /etc/ssl/private/zammad.example.com.key  \
               --fullchain-file /etc/ssl/private/zammad.example.com.full.pem \
               --reloadcmd     "systemctl force-reload <webserver>"

            From this moment on, acme.sh will automatically renew your installed certificates if they're valid for 
            another 30 days or less.


               .. hint:: **👀 Not exactly what you're looking for?**

                  The `acme.sh documentation <https://github.com/acmesh-official/acme.sh/wiki/How-to-issue-a-cert>`_ 
                  has alot more use cases than we cover here.

   .. tab:: public, paid CA

      If you prefer to use certificates from other official CAs than letsencrypt, you can do so as well. 
      Just get your certificate bundle from the source you prefer and continue with `Adjusting the webserver configuration`_.

         .. note:: **🙋 I’m new to SSL certificates. Where can I get a certificate?**

            The easiest way to get certificates is to buy an annual subscription through a commercial CA, such as:

               * `Sectigo (formerly Comodo) <https://sectigo.com/ssl-certificates-tls>`_
               * `Secorio <https://secorio.com/en/productfinder/>`_
               * `GlobalSign <https://www.globalsign.com/en/managed-ssl>`_

            (Zammad is not affiliated with these CAs in any way.)

   .. tab:: self-signed (discouraged)

      Another way is to use self signed certificates from your own CA. 
      In general you shouldn't use this option when you have users accessing Zammad that can't verify your certificates.

      Beside creating own certificates via e.g. XCA or Microsoft CA, you can also generate a certificate really quick like so:

      On any system with ``openssl`` installed, you can run below command. 
      Provide the requested information and ensure to provide the fqdn of Zammad when being asked for 
      ``Common Name (e.g. server FQDN or YOUR name)``.

         .. code-block:: sh
            
            openssl req -newkey rsa:4096 -nodes -x509 -days 1825 -keyout key.pem -out certificate.pem 

      Above command creates a certificate that's valid for 5 years. It will write the certificate and private key 
      to the current directory you're in. If you want to check your certificate you just created, you can use the 
      following command.

         .. code-block:: sh

            openssl x509 -text -noout -in certificate.pem

         .. hint:: **👀 Not good enough for you?**

            If above command is not good enough for you, the `openSSL documentation <>`_ 
            is a good place to learn more.

Adjusting the webserver configuration
-------------------------------------

.. warning:: For a quick start, we're installing a HTTP configuration. 
   You should **never** use HTTP connections for authentication - instead, we encourage you to use HTTPS!

   If Zammad scripts automatically installed your webserver configuration file, ensure to not rename it.

.. tabs::
   
   .. tab:: nginx (default)

      In order to access Zammad from external open Zammads vHost configuration 
      (``/etc/nginx/sites-enabled/zammad.conf`` - your path may differ).

      Locate any ``server_name`` directive and adjust ``example.com`` to the subdomain you have chosen for 
      your Zammad instance.  

      After you made your required changes, don't forget to reload your nginx: ``systemctl reload nginx``.

   .. tab:: apache2

      In order to access Zammad from external open Zammads vHost configuration 
      (``/etc/apache/sites-enabled/zammad.conf`` - your path may differ).

      Locate any ``ServerName`` directives and adjust them to your chosen subdomain. 

         .. hint:: **🧐 Ensure all required modules are enabled:**

            * proxy
            * proxy_html
            * proxy_http
            * proxy_wstunnel
            * headers

   .. tab:: local testing or other proxy servers
   
      Want to test locally first or use a different Proxy we don't support?
      The main application (rails server) is listening on ``http://localhost:3000``.

      If you're using a proxy server, also ensure that you proxy the websockets as well. 
      The websocket server listens on ``ws://localhost:6042``.

      .. tip:: If above ports are used by other applications already you may want to have a look
         at :ref:`network options <network_options>` on our environment page.

**If you just installed Zammad, you'll be greeted by our getting started wizard. 🙌**

   .. figure:: /images/install/getting-started-wizard.png
      :alt: Getting started wizard after installing Zammad
      :width: 90%
      :align: center