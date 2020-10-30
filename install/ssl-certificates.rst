.. _getting_ssl:

Installing SSL Certificates
***************************

SSL certificates help to secure the network connection between you, the user and the webserver. 
When ever possible, you should use ssl protected connections.

.. note:: Below options can't provide a full how to. If you experience issues on these steps, please
   consult the documentation of the vendor responsible.

   We expect that you installed everything required for below options.

Issue a certificate
===================

Option 1: Using letsencrypt
---------------------------

letsencrypt is an easy and free way to retreive valid ssl certificates.
These certificates are valid for 90 days and can be renewed automatically.

The two most common tools are `certbot <https://certbot.eff.org/instructions>`_ 
and `acme.sh <https://github.com/acmesh-official/acme.sh>`_.

... using certbot
   .. hint:: If not happened automatically, you may need to install the nginx or apache plugin for certbot:
      ``python3-certbot-nginx`` OR ``python3-certbot-apache``

   During the first certbot run it will request additional information once.
   Replace ``<webserver>`` in below command by either ``apache``, ``httpd`` or ``nginx`` 
   and to match your setup.
   
   .. code-block:: sh

      certbot --<webserver> -d zammad.example.com

   Certbot will now attempt to issue a certificate for you. 
   If successful, certbot will ask you if you want to ``[1] not redirect`` or ``[2] redirect`` automatically.
   You can choose to not redirect **if** you plan to use the :ref:`sample configuration <use_sample_ssl_config>`
   of Zammad. If not, select ``[2] redirect``.

   From this moment on, certbot will automatically renew your installed certificates if they're valid for 
   another 30 days or less.

      .. hint:: **👀 Not exactly what you're looking for?**

         The `cerbot documentation <https://certbot.eff.org/docs/using.html#certbot-commands>`_ has alot 
         more use cases than we cover here.

... using acme.sh
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


Option 2: Obtaining a certificate from a public CA
--------------------------------------------------

If you prefer to use certificates from other official CAs than letsencrypt, you can do so as well. 
Just get your certificate bundle from the source you prefer and continue with :ref:`use_sample_ssl_config` below.

Option 3: Creating a self signed certificate (discouraged)
----------------------------------------------------------

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

.. _use_sample_ssl_config:

Adjust the sample configuration of Zammad
=========================================

      If you already have certificates on your system, adjust the following mandatory directives to fit your certificates: 
      ``ssl_certificate`` and ``ssl_certificate_key``.

      You can provide a trusted CA storage by using ``ssl_trusted_certificate`` - if you prefer to rely on your local system, 
      comment out this directive (``# ssl_trusted_certificate``).
