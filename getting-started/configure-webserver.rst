Configure the Webserver
=======================

.. include:: /install/includes/hosted-services.rst

You can find current sample configuration files for your webserver within
``contrib/`` of your Zammad installation.
If you're using the package installation, Zammad attempts to automatically
install a configuration file to your Nginx for you.

.. note::

   The Zammad installation will not automatically set any host- or server name
   for you.

   | **Docker Compose / Kubernetes users**
   | Please also note the environment information on
     :doc:`this page </appendix/environment-variables>`

Get a SSL Certificate (recommended)
-----------------------------------

Don't know how to get SSL certificates and install them on a webserver yet?
The guide within the tabs below can help you jumping in.

Make sure to used named configuration. The default sample configuration
for both Nginx and Apache are *not* named.
To fix this, open the ``zammad.conf`` in your webserver's configuration
directory and make sure to replace ``server_name localhost;`` (Nginx) or
``ServerName localhost`` (Apache 2) with Zammad's actual subdomain.

**Where?**

.. tabs::

   .. tab:: Nginx

      .. include:: includes/nginx-config-paths.include.rst

   .. tab:: Apache 2

      .. include:: includes/apache-config-paths.include.rst


**How?**

.. tabs::

   .. tab:: I don't need that

      You either already know what you're doing, you're developing or like the
      danger. ⚔️

   .. tab:: Let's Encrypt

      Let's Encrypt is an easy and free way to retrieve valid ssl certificates.
      These certificates are valid for 90 days and can be renewed automatically.

      The two most common tools are
      `Certbot <https://certbot.eff.org/instructions>`_ and
      `acme.sh <https://github.com/acmesh-official/acme.sh>`_.

      .. tabs::

         .. tab:: Certbot

            If not happened automatically, you have to install
            the Nginx or Apache plugin for Certbot:
            ``python3-certbot-nginx`` OR ``python3-certbot-apache``

            During the first Certbot run it will request additional information
            once. Replace ``<webserver>`` in below command by either
            ``apache``, ``httpd`` or ``nginx`` and to match your setup.

            .. code-block:: console

               $ certbot --<webserver> -d zammad.example.com

            Certbot will now attempt to issue a certificate for you.
            If successful, Certbot will ask you if you want to
            ``[1] not redirect`` or ``[2] redirect`` automatically.
            You can choose to not redirect **if** you plan to use the sample
            configuration of Zammad. If not, select ``[2] redirect``.

            From this moment on, Certbot will automatically renew your
            installed certificates if they're valid for another 30 days or less.

            .. hint:: **Not exactly what you're looking for?**

               The `Certbot documentation`_
               has a lot more use cases than we cover here.

         .. tab:: acme.sh

            .. note::

               acme.sh by default no longer uses Let's Encrypt.
               For this reason you'll have to change the default CA.

               .. code-block:: console

                  $ acme.sh --set-default-ca  --server letsencrypt

               If you want to use any other CA with acme.sh, consult their
               documentation on how to.

            First of all you'll need to issue your certificate.
            acme.sh will save this certificate to
            ``/root/.acme.sh/<your-domain>/``

            Replace ``<webserver>`` in the following command by either
            ``apache`` or ``nginx`` and to match your setup, use ``standalone`` for other webservers.

            .. code-block:: console

               $ acme.sh --issue --<webserver> -d zammad.example.com

            It's not recommended to use the just stored certificates directly.
            Instead you should install the certificate to a directory of your
            choice.

            We're using ``/etc/ssl/private/`` in this case, but you can use any
            directory you like.

            .. warning::

               Ensure to adjust value for ``--reloadcmd`` as this will
               ensure that acme.sh reloads your webserver automatically
               after getting a renewal. Replace ``<webserver>`` by either
               ``apache2``, ``httpd`` or ``nginx``

            .. code-block:: console

               $ acme.sh --install-cert -d zammad.example.com \
                   --cert-file      /etc/ssl/private/zammad.example.com.pem  \
                   --key-file       /etc/ssl/private/zammad.example.com.key  \
                   --fullchain-file /etc/ssl/private/zammad.example.com.full.pem \
                   --reloadcmd     "systemctl force-reload <webserver>"

            From this moment on, acme.sh will automatically renew your
            installed certificates if they're valid for another 30 days or less.

            .. hint::

               **Not exactly what you're looking for?**

               The `acme.sh documentation`_ has a lot more use cases than
               we cover here.

   .. tab:: public, paid CA

      If you prefer to use certificates from other official CAs than
      Let's Encrypt, you can do so as well. Just get your certificate bundle from
      the source you prefer and continue with
      `Adjusting the webserver configuration`_.

      .. note::

         **🙋 I'm new to SSL certificates. Where can I get a certificate?**

         The easiest way to get certificates is to buy an annual
         subscription through a commercial CA, such as:

         * `Sectigo (formerly Comodo)`_
         * `Secorio`_
         * `GlobalSign`_

         (Zammad is not affiliated with these CAs in any way.)

   .. tab:: self-signed (discouraged)

      Another way is to use self signed certificates from your own CA.
      In general you shouldn't use this option when you have users accessing
      Zammad that can't verify your certificates.

      Beside creating own certificates via e.g. XCA or Microsoft CA, you can
      also generate a certificate really quick like so:

      On any system with ``openssl`` installed, you can run below command.
      Provide the requested information and ensure to provide the fqdn of
      Zammad when being asked for
      ``Common Name (e.g. server FQDN or YOUR name)``.

      .. code-block:: console

         $ openssl req -newkey rsa:4096 -nodes -x509 -days 1825\
             -keyout key.pem -out certificate.pem

      Above command creates a certificate that's valid for 5 years. It will
      write the certificate and private key to the current directory you're in.
      If you want to check your certificate you just created, you can use the
      following command.

      .. code-block:: console

         $ openssl x509 -text -noout -in certificate.pem

      .. hint::

         **Not good enough for you?**

         If above command is not good enough for you, the
         `openSSL documentation`_ is a good place to learn more.

.. _Certbot documentation: https://certbot.eff.org/docs/using.html#certbot-commands
.. _acme.sh documentation: https://github.com/acmesh-official/acme.sh/wiki/How-to-issue-a-cert
.. _Sectigo (formerly Comodo): https://sectigo.com/ssl-certificates-tls
.. _Secorio: https://secorio.com/en/productfinder/
.. _GlobalSign: https://www.globalsign.com/en/managed-ssl
.. _openSSL documentation: https://www.openssl.org/docs/

Adjusting the Webserver Configuration
-------------------------------------

.. warning::

   For a quick start, we're installing a HTTP configuration.
   You should **never** use HTTP connections for authentication - instead, we
   encourage you to use HTTPS!

   If Zammad scripts automatically installed your webserver configuration file,
   ensure to not rename it. Below we'll cover HTTPs for above reason.

.. tabs::

   .. tab:: Nginx (default)

      Step 1 - Get a current config file
         Copy & overwrite the default ``zammad.conf`` by using

         .. code-block:: console

            $ cp /opt/zammad/contrib/nginx/zammad_ssl.conf /etc/nginx/sites-available/zammad.conf

         Your Nginx directories may differ, please adjust your commands if
         needed.

         Most common:

         .. include:: includes/nginx-config-paths.include.rst

      Step 2 - Adjust the config file
         Adjust the just copied file with a text editor of your choice (e.g.
         ``vi`` or ``nano``).

         Locate any ``server_name`` directive and adjust ``example.com`` to the
         subdomain you have chosen for your Zammad instance.

         Now you'll need to adjust the path and file names for your ssl
         certificates your obtained on the prior steps. Adjust the following
         directives to match your setup:

            * ``ssl_certificate`` (your ssl certificate)
            * ``ssl_certificate_key`` (the certificates private key)
            * ``ssl_trusted_certificate`` (the public CA certificate)

            .. note::

               Technically this is not a hard requirement, but recommended!

         .. include:: /getting-started/include-dhparam-webserver.rst

      (Optional) - Adjust HTTPs configuration
         .. include:: /getting-started/include-ssl-config-generator-webserver.rst

      Step 3 - Save & reload
         Reload your Nginx with ``systemctl reload nginx`` to apply your
         configuration changes.

   .. tab:: Apache2

      Step 1 - Ensure required modules are enabled
         Zammad requires modules that are not enabled by default. By default
         use ``a2enmod`` (**not** CentOS) to do so.

         .. tabs::

            .. tab:: a2enmod

               .. code-block:: console

                  $ a2enmod proxy proxy_html proxy_http proxy_wstunnel headers ssl

               If you want to run Zammad under HTTP/2, you will also need

               .. code-block:: console

                  $ a2enmod h2 proxy_http2 mpm_event

               .. code-block:: console

                  $ sudo systemctl restart apache2

            .. tab:: via configuration file (CentOS)

               add/uncomment the appropriate ``LoadModule`` statements
               in your Apache config:

               .. code-block:: text

                  # /etc/httpd/conf/httpd.conf

                  LoadModule headers_module modules/mod_headers.so
                  LoadModule proxy_module modules/mod_proxy.so
                  LoadModule proxy_html_module modules/mod_proxy_html.so
                  LoadModule proxy_http_module modules/mod_proxy_http.so
                  LoadModule proxy_wstunnel_module modules/mod_proxy_wstunnel.so

               Don't forget to restart your Apache.

      Step 2 - Get a current config file
         .. note::

            Package installations attempt to copy a ``zammad.conf`` to your
            webserver's configuration directory. **Do not rename** this file!

         Copy & overwrite the default ``zammad.conf`` by using

         .. code-block:: console

            $ cp /opt/zammad/contrib/apache2/zammad_ssl.conf /etc/apache2/sites-available/zammad.conf

         Your Apache directories may differ, please adjust your commands
         if needed.

         Most common:

         .. include:: includes/apache-config-paths.include.rst

      Step 3 - Adjust the config file
         Adjust the just copied file with a text editor of your choice (e.g.
         ``vi`` or ``nano``).

         Locate any ``ServerName`` directive and adjust ``example.com`` to the
         subdomain you have chosen for your Zammad instance.

         Now you'll need to adjust the path and file names for your ssl
         certificates your obtained on the prior steps. Adjust the following
         directives to match your setup:

            * ``SSLCertificateFile`` (your ssl certificate)
            * ``SSLCertificateKeyFile`` (the certificates private key)
            * ``SSLCertificateChainFile`` (the public CA certificate)

            .. note::

               Technically this is not a hard requirement, but recommended!

         .. include:: /getting-started/include-dhparam-webserver.rst

      (Optional) - Adjust HTTPs configuration
         .. include:: /getting-started/include-ssl-config-generator-webserver.rst

      (Optional) - Enable the site
         .. hint::

            This step mostly depends on your selected folders and most often
            only affects ``sites-available`` folders.

         .. tabs::

            .. tab:: Ubuntu / Debian / openSUSE

               .. code-block:: console

                  $ a2ensite zammad

            .. tab:: CentOS

               .. code-block:: console

                  $ ln -s /etc/httpd/sites-available/zammad_ssl.conf /etc/httpd/sites-enabled/

         Also, make sure the following line is present in your Apache
         configuration:

         .. code-block:: text

            IncludeOptional sites-enabled/*.conf

         You can find your config file in Ubuntu, Debian & openSUSE
         under ``/etc/apache2/apache2.conf`` and for CentOS under
         ``/etc/httpd/conf/httpd.conf``.

      Step 4 - Save & reload
         Reload your Apache to apply your configuration changes:

         .. code-block:: console

            $ sudo systemctl reload apache2

   .. tab:: local testing or other proxy servers

      Want to test locally first or use a different Proxy we don't support?
      The main application (Rails server) is listening on
      ``http://127.0.0.1:3000``.

      If you're using a proxy server, also ensure that you proxy the websockets
      as well. The websocket server listens on ``ws://127.0.0.1:6042``.

      If above ports are used by other applications already, please
      have a look at :doc:`/appendix/environment-variables`.

      .. warning::

         Do not expose Zammad directly to the internet, as Zammad only provides
         HTTP!

**If you just installed Zammad, you'll be greeted by our getting started
wizard. 🙌** You now can continue with :doc:`first-steps`.

.. hint::

   **You're not seeing Zammad's page but a default landing page of your OS?**

   Ensure that you did restart your webserver - also check if
   ``000-default.conf`` or ``default.conf`` in your vhost directory
   possibly overrules your configuration.

   Sometimes this is also a DNS resolving issue.

.. include:: /getting-started/include-csrf-hints.rst

.. figure:: /images/install/getting-started-wizard.png
   :alt: Getting started wizard after installing Zammad
   :width: 80%
   :align: center
