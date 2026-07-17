Configure the Webserver
=======================

.. include:: /install/includes/hosted-services.rst

Configure your webserver to reverse-proxy the Zammad application server. The
page covers obtaining an SSL certificate, adjusting the sample configuration for
Nginx and Apache 2 and reloading the webserver to apply the changes.

You can find sample configuration files for your webserver within
the ``contrib/`` directory of your Zammad installation. There are
two example files per webserver: ``zammad.conf`` (plain HTTP) and
``zammad_ssl.conf`` (HTTPS). The non-SSL file is intended for
local testing only and must not be used in production. During a
package installation of Zammad, the package automatically copies
the non-SSL ``zammad.conf`` to your webserver's config directory.
For production use, replace it with the ``zammad_ssl.conf`` and
follow the steps on this page.

.. note::

   **Docker Compose / Kubernetes users**:

   Skip this page. Configure the webserver port, hostname and
   scheme via the ``NGINX_*`` and ``ZAMMAD_RAILSSERVER_*``
   variables, as you can find on the
   :doc:`environment variables page </appendix/environment-variables>`.

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
      the selector and complete the install. Once installed, request
      a certificate by replacing ``<webserver>`` with ``nginx`` or
      ``apache`` and ``zammad.example.com`` with your subdomain:

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
      lightweight shell-based ACME client and an alternative to Certbot,
      but it no longer uses Let's Encrypt by default. Set the default
      CA to Let's Encrypt before issuing a certificate:

      .. code-block:: console

         $ acme.sh --set-default-ca --server letsencrypt

      Issue the certificate by replacing ``<webserver-plugin>`` with
      ``nginx``, ``apache`` or ``standalone`` and ``zammad.example.com``
      with your subdomain:

      .. code-block:: console

         $ acme.sh --issue --<webserver-plugin> -d zammad.example.com

      Install the certificate to a directory of your choice (e.g.
      ``/etc/ssl/private/``) and reload the webserver after each
      renewal. Replace ``<webserver-service>`` in the command below
      with the matching systemd service name (``nginx``, ``apache2``
      or ``httpd``):

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
         Adjust the just copied file with a text editor of your
         choice (e.g. vi or nano).
         Locate both ``server_name`` directives (one in the HTTP
         server block on port 80, one in the HTTPS server block on
         port 443) and adjust ``example.com`` to the subdomain you
         have chosen for your Zammad instance.

         Now you'll need to adjust the path and file names for
         your SSL certificates you obtained on the prior steps.
         Adjust the following directives to match your setup:

         - ``ssl_certificate`` (your SSL certificate)
         - ``ssl_certificate_key`` (the certificates private key)
         - ``ssl_trusted_certificate`` (the public CA certificate)

         To improve HTTPS security, also configure a Diffie-Hellman
         parameter file and point ``ssl_dhparam`` at it:

         .. code-block:: console

            $ sudo openssl dhparam -out /etc/ssl/dhparam.pem 4096

      Reload and verify
         Verify the configuration:

          .. code-block:: console

             $ sudo nginx -t

         Reload Nginx:

         .. code-block:: console

            $ sudo systemctl reload nginx

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
         Adjust the just copied file with a text editor of your
         choice (e.g. vi or nano).
         Locate any ``ServerName`` directive and adjust ``example.com``
         to the subdomain you have chosen for your Zammad instance.
         The first ``ServerName`` (in the HTTP VirtualHost) defaults to
         ``example.com`` and the second (in the HTTPS VirtualHost) to
         ``localhost``.

         Now you'll need to adjust the path and file names for
         your SSL certificates you obtained on the prior steps.
         Adjust the following directives to match your setup:

         - ``SSLCertificateFile`` (your SSL certificate)
         - ``SSLCertificateKeyFile`` (the certificates private key)
         - ``SSLCertificateChainFile`` (the public CA certificate)

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

   .. tab:: Local testing or other proxy servers

      Zammad's main application listens on port ``3000`` and the websocket
      server on port ``6042``. If you put your own reverse proxy in front of
      Zammad, forward both.

      If the default ports conflict with other applications on your host,
      see :doc:`/appendix/environment-variables` to change them.

      .. warning::

         Do not expose Zammad directly to the internet. Zammad only
         provides plain HTTP and would be reachable without
         authentication.

Now visit your configured Zammad domain in a browser. You should reach
the Zammad getting started wizard for new installations (see screenshot below).
If you don't see Zammad's setup wizard or Zammad UI at all, check the
:ref:`Troubleshooting section <configure_webserver_troubleshooting>` below.

.. figure:: /images/install/getting-started-wizard.png
   :alt: Getting started wizard after installing Zammad
   :width: 80%
   :align: center

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
your domain and wait for them to propagate. Replace the ``zammad.example.com``
in the following command with your configured domain of Zammad and check if
the domain points to the right server:

.. code-block:: console

   $ host zammad.example.com

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
