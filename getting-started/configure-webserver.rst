Configure the Webserver
=======================

.. include:: /install/includes/hosted-services.rst

You can find current sample configuration files for your webserver within
``contrib/`` of your Zammad installation.
If you're using the package installation, Zammad attempts to automatically
install a configuration file to your Nginx for you.

.. note::

   **Docker Compose / Kubernetes users**
   Skip this page. Configure the webserver port, hostname and
   scheme via the ``NGINX_*`` and ``ZAMMAD_RAILSSERVER_*``
   variables, as you can find on the :doc:`environment variables
   page </appendix/environment-variables>`.

.. _configure_webserver_obtain_certificate:

Obtain an SSL Certificate
-------------------------

Zammad requires HTTPS in production. Use one of the options below to obtain
a certificate before continuing with the webserver configuration.

Commercial Certificate Authority
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Buy an annual certificate from any trusted public CA. A few common options
are `Sectigo`_, `GlobalSign`_ or `DigiCert`_. Install the resulting
certificate, key and chain on your server as you would for any HTTPS
service, then continue with the webserver configuration below.

.. _Sectigo: https://sectigo.com/ssl-certificates-tls
.. _GlobalSign: https://www.globalsign.com/en/managed-ssl
.. _DigiCert: https://www.digicert.com/tls-ssl/

Let's Encrypt
^^^^^^^^^^^^^

Let's Encrypt issues free, automatically renewable certificates. Two
clients are commonly used.

.. tabs::

   .. group-tab:: Certbot

      Certbot is the most widely used ACME client. Follow the
      upstream
      `Certbot installation instructions <https://certbot.eff.org/instructions>`_,
      select your distribution and the matching webserver plugin in
      the selector and complete the install. Once installed, request a
      certificate by replacing ``<webserver>`` with either ``nginx``
      or ``apache`` and ``zammad.example.com`` with your subdomain:

      .. code-block:: console

         $ sudo certbot --<webserver> -d zammad.example.com

      Certbot will issue the certificate, ask whether to redirect
      HTTP to HTTPS (choose ``[1] not redirect`` if you plan to use
      the Zammad sample configuration, which already handles the
      redirect, otherwise choose ``[2] redirect``) and arrange
      automatic renewal once the certificate has less than 30 days of
      validity remaining.

   .. group-tab:: acme.sh

      `acme.sh <https://github.com/acmesh-official/acme.sh>`_ is a
      lightweight shell-based ACME client and an alternative to Certbot.
      Issue the certificate by replacing ``<webserver-plugin>`` with
      ``nginx``, ``apache`` or ``standalone`` and ``zammad.example.com``
      with your subdomain:

      .. code-block:: console

         $ acme.sh --issue --<webserver-plugin> -d zammad.example.com

      Install the certificate to a directory of your choice and reload
      the webserver after each renewal by replacing
      ``<webserver-service>`` with the matching systemd service name
      (``nginx``, ``apache2`` or ``httpd``):

      .. code-block:: console

         $ acme.sh --install-cert -d zammad.example.com \
             --cert-file      /etc/ssl/private/zammad.example.com.pem  \
             --key-file       /etc/ssl/private/zammad.example.com.key  \
             --fullchain-file /etc/ssl/private/zammad.example.com.full.pem \
             --reloadcmd     "systemctl force-reload <webserver-service>"

      See the `acme.sh documentation`_ for further use cases.

      .. _acme.sh documentation: https://github.com/acmesh-official/acme.sh/wiki/How-to-issue-a-cert

.. _configure_webserver_adjust:

Adjust the Webserver Configuration
----------------------------------

.. tabs::

   .. tab:: Nginx (default)

      Get the sample config into place
         Copy the SSL sample configuration to your Nginx config directory:

         .. code-block:: console

            $ sudo cp /opt/zammad/contrib/nginx/zammad_ssl.conf \
                /etc/nginx/sites-available/zammad.conf

         Most common Nginx config directories:

         .. include:: includes/nginx-config-paths.include.rst

      Adjust server name and certificate paths
         Open the copied file in a text editor and replace
         ``example.com`` in the ``server_name`` directive with your
         subdomain (e.g. ``zammad.example.com``), then adjust the
         following directives:

         - ``ssl_certificate`` (path to your certificate)
         - ``ssl_certificate_key`` (path to your certificate's private key)
         - ``ssl_trusted_certificate`` (path to the public CA bundle, used
           for OCSP stapling)

         To improve HTTPS security, also configure a Diffie-Hellman
         parameter file and point ``ssl_dhparam`` at it:

         .. code-block:: console

            $ sudo openssl dhparam -out /etc/ssl/dhparam.pem 4096

      Reload and verify
         Reload Nginx and verify the configuration:

         .. code-block:: console

            $ sudo systemctl reload nginx

         Visit ``https://<your-subdomain>`` in a browser. You should reach
         the Zammad getting started wizard. If you do not, see the
         `Troubleshooting`_ section below.

   .. tab:: Apache 2

      Enable the required modules
         Zammad requires modules that are not enabled by default. On
         Ubuntu, Debian and openSUSE use ``a2enmod``:

         .. code-block:: console

            $ sudo a2enmod proxy proxy_html proxy_http proxy_wstunnel \
                headers ssl

         For HTTP/2 support also enable:

         .. code-block:: console

            $ sudo a2enmod h2 proxy_http2 mpm_event

         On CentOS / RHEL add the matching ``LoadModule`` lines to
         ``/etc/httpd/conf/httpd.conf`` instead:

         .. code-block:: text

            LoadModule headers_module modules/mod_headers.so
            LoadModule proxy_module modules/mod_proxy.so
            LoadModule proxy_html_module modules/mod_proxy_html.so
            LoadModule proxy_http_module modules/mod_proxy_http.so
            LoadModule proxy_wstunnel_module modules/mod_proxy_wstunnel.so

         Restart Apache after enabling the modules:

         .. code-block:: console

            $ sudo systemctl restart apache2

      Get the sample config into place
         Copy the SSL sample configuration to your Apache config directory:

         .. code-block:: console

            $ sudo cp /opt/zammad/contrib/apache2/zammad_ssl.conf \
                /etc/apache2/sites-available/zammad.conf

         Most common Apache config directories:

         .. include:: includes/apache-config-paths.include.rst

         The package installation attempts to copy this file for you.
         Do not rename it.

      Adjust server name and certificate paths
         Open the copied file in a text editor and replace
         ``localhost`` in the ``ServerName`` directive with your
         subdomain (e.g. ``zammad.example.com``), then adjust the
         following directives:

         - ``SSLCertificateFile`` (path to your certificate)
         - ``SSLCertificateKeyFile`` (path to your certificate's private key)
         - ``SSLCertificateChainFile`` (path to the public CA bundle)

         To improve HTTPS security, also configure a Diffie-Hellman
         parameter file and point ``SSLOpenSSLConfCmd DHParameters`` at
         it:

         .. code-block:: console

            $ sudo openssl dhparam -out /etc/ssl/dhparam.pem 4096

      Enable the site
         On Ubuntu, Debian and openSUSE:

         .. code-block:: console

            $ sudo a2ensite zammad

         On CentOS / RHEL:

         .. code-block:: console

            $ sudo ln -s /etc/httpd/sites-available/zammad_ssl.conf \
                /etc/httpd/sites-enabled/

         Make sure ``IncludeOptional sites-enabled/*.conf`` is present in
         ``/etc/apache2/apache2.conf`` (Ubuntu, Debian, openSUSE) or
         ``/etc/httpd/conf/httpd.conf`` (CentOS / RHEL).

      Reload and verify
         Reload Apache and verify the configuration:

         .. code-block:: console

            $ sudo systemctl reload apache2

         Visit ``https://<your-subdomain>`` in a browser. You should reach
         the Zammad getting started wizard. If you do not, see the
         `Troubleshooting`_ section below.

   .. tab:: Local testing or other proxy servers

      Zammad's main application listens on ``http://127.0.0.1:3000`` and
      the websocket server on ``ws://127.0.0.1:6042``. If you proxy Zammad
      through another reverse proxy, make sure to forward the websockets
      as well.

      If the default ports conflict with other applications on your host,
      see :doc:`/appendix/environment-variables` to change them.

      .. warning::

         Do not expose Zammad directly to the internet. Zammad only
         provides plain HTTP and would be reachable without
         authentication.

.. _configure_webserver_troubleshooting:

Troubleshooting
---------------

Default Landing Page Instead of Zammad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you reach the webserver's default landing page rather than Zammad,
your ``zammad.conf`` may be overruled by another config file. Check
the vhost directory for ``000-default.conf`` or ``default.conf`` and
disable it.

DNS Not Resolving
^^^^^^^^^^^^^^^^^

If the subdomain does not resolve, double-check the DNS records for
your domain and wait for them to propagate.

CSRF Token Errors
^^^^^^^^^^^^^^^^^

If users cannot log in because of CSRF token errors, your webserver
chain may not pass the original connection type to Zammad. Tell the
proxy directly that the connection is HTTPS.

Nginx
   Within your virtual host configuration, locate
   ``proxy_set_header X-Forwarded-Proto`` and replace ``$scheme``
   with ``https``.

Apache 2
   Within your virtual host configuration, just above the first
   ``ProxyPass`` directive, insert:

   .. code-block:: text

      RequestHeader set X_FORWARDED_PROTO 'https'
      RequestHeader set X-Forwarded-Ssl on

If you just installed Zammad, you'll be greeted by our getting started
wizard. You can now continue with :doc:`first-steps`.

.. _Troubleshooting: #configure-webserver-troubleshooting

.. figure:: /images/install/getting-started-wizard.png
   :alt: Getting started wizard after installing Zammad
   :width: 80%
   :align: center
