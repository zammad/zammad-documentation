Single Sign-On for Kerberos
===========================

This guide will discuss how to set up single sign-on
using Microsoft Active Directory.

.. note:: SSO can only be configured on **self-hosted installations**.

.. figure:: /images/appendix/single-sign-on/login-sso-button.png
   :alt: Login screen with SSO button for one-click login.
   :align: center

Conceptual Overview
-------------------

Like every other web application out there,
Zammad has its own logic for signing users up, storing their passwords,
authenticating them, and managing their sessions.

If your IT department keeps its own user identity store (like Active Directory),
Zammad's SSO support allows you to leverage that existing auth system
so that anyone with an account on your local intranet will
1) automatically have an account in Zammad and
2) be able to log in with a single click.

.. note:: If you *don't* have this IT infrastructure
   but still want one-click login,
   see :admin-docs:`Third Party Authentication </settings/security.html#third-party-applications>`
   for alternatives.

How Does it Work?
-----------------

Zammad does not speak Kerberos itself. It provides the endpoint
``https://your.zammad.host/auth/sso`` and relies on the web server in front
of it to authenticate the user before a request reaches that endpoint. The
web server passes the user name along, Zammad looks up the user by their
login and starts a session.

The user name can arrive in one of three forms, which Zammad checks in this
order:

- the ``REMOTE_USER`` variable of the web server, only when the web server
  runs Zammad in its own process
- the ``Remote-User`` request header, which Zammad sees as ``HTTP_REMOTE_USER``
- the ``X-Forwarded-User`` request header

Which one applies depends on your installation:

Package installation
   Apache replaces Nginx on the Zammad host, authenticates ``/auth/sso`` and
   sets ``X-Forwarded-User``.

Docker stack
   The stack's own Nginx stays in place. An additional container in front of
   ``/auth/sso`` authenticates, sets ``X-Forwarded-User`` and forwards the
   request to Zammad's application server directly.

.. note:: 😬 **Wait. SSO allows you to sign in with only a username?**

   In principle, yes.

   **How is that okay?**

   In this guide, we configure our web server (Apache)
   to intercept all requests to the ``/auth/sso`` endpoint.
   Instead of forwarding them to Zammad,
   Apache initiates a three-sided login process (*Kerberos authentication*)
   between the itself, the user, and the Active Directory server.

   If Active Directory doesn't recognize the user or their password,
   Zammad never sees the request, and the session is never created.

   **What does this all mean?**

   It means there are many ways you could set up SSO—you
   don't need to follow this guide or even use Active Directory or Kerberos—but
   if you don't know what you're doing,
   you're going to end up with a *massive* security hole.

Getting Started
---------------

.. hint:: 😵 **Too busy to handle it on your own?**

   We've got you covered.
   Our experts offer custom-tailored workshops
   to get your team up and running fast and with confidence.
   `Just drop us a line <https://zammad.com/contact>`_!

You will need:

- a Microsoft Active Directory environment with

  - root access
  - support for AES 256-bit encryption

- a Zammad installation with a fully-qualified domain name (FQDN), either

  - a package installation with root access on the host, or
  - the Docker stack behind a reverse proxy that terminates TLS and routes
    by path, such as the :ref:`Nginx Proxy Manager scenario
    <add-nginx-proxy-manager>`

- some familiarity with system administration (*e.g.,* Apache configuration)

For best results, set up :admin-docs:`LDAP integration </system/integrations/ldap/index.html>`
to make sure your Active Directory and Zammad user accounts
are always in sync.

.. _sso-register-spn:

Step 1: Configure Active Directory
----------------------------------

In the Kerberos authentication scheme,
the **authentication server** (Active Directory)
needs to maintain shared secrets with the **service** (Zammad).
To make this possible, we need to register a **service principal name** (SPN)
for Zammad on Active Directory.

.. note:: These directions have been confirmed on Windows Server 2016.

1a. Create a service account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may use an existing service account if you have one.
Admin privileges are not required; a normal user account will do.

.. figure:: /images/appendix/single-sign-on/active-directory-service-account-settings.png
   :alt: Login screen with SSO button for one-click login.
   :align: center

   Select "This account supports Kerberos AES 256 bit encryption" under
   **Properties > Account > Account options**.

Without this option, the keytab carries only RC4 keys, which current Kerberos
libraries reject; the Docker SSO container is one of them.

1b. Reset Password
^^^^^^^^^^^^^^^^^^

Reset service account password after enabling the "This account supports
Kerberos AES 256 bit encryption".

1c. Register a SPN for Zammad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replace the following placeholders in the command below:

:``<zammad-host>``:              Zammad FQDN
:``<service-acct>``:             Service account logon name
:``<password>``:                 Password of the service account
                                 (Option ``/pass *`` did prove to not work)
:``<domain>``:                   Windows domain
:``<master-domain-controller>``: Master domain controller IP/FQD

Below command will prompt for the users password:

.. code-block:: console

   $ setspn -s HTTP/<zammad-host> <service-acct>
   $ ktpass /princ HTTP/<zammad-host>@<DOMAIN> \
            /mapuser <service-acct> \
            /crypto AES256-SHA1 \
            /ptype KRB5_NT_PRINCIPAL \
            /pass <password> -SetPass +DumpSalt \
            /target <master-domain-controller> \
            /out zammad.keytab

1d. Note the secret key and version number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This step is for the package installation only. The Docker stack uses the
``zammad.keytab`` file written by the command above as it is.

The output of the command above contains important data for Step 2f below:

.. code-block:: text

   Using legacy password setting method
   Failed to set property 'servicePrincipalName' to 'HTTP/<zammad-host>' on Dn 'CN=Zammad Service,DC=<domain>,DC=<tld>': 0x13.
   WARNING: Unable to set SPN mapping data.
   If <service-acct> already has an SPN mapping installed for HTTP/<zammad-host>, this is no cause for concern.
   Building salt with principalname HTTP/<zammad-host> and domain <domain> (encryption type 18)...
   Hashing password with salt "<domain><service-acct>".
   Key created.
   Output keytab to zammad.keytab:
   Keytab version: 0x502
   keysize 67 <service-acct>@<domain> ptype 1 (KRB5_NT_PRINCIPAL) vno 3 etype 0x12 (AES256-SHA1) keylength 32 (0x5ee827c30c736dd4095c9cbe146eabc216415b1ddb134db6aabd61be8fdf7fb1)

On the last line, take note of:

:the secret key:                in parentheses at the end (**0x5ee827...**)
:the secret key version number: preceded by ``vno`` (**3**)

Step 2: Set Up the Kerberos Endpoint
------------------------------------

Next, requests to ``/auth/sso`` must pass a web server that performs the
Kerberos authentication before they reach Zammad. How you set this up depends
on your installation: follow :ref:`sso-package` or :ref:`sso-docker`.

.. _sso-package:

Package Installation
^^^^^^^^^^^^^^^^^^^^

Next, the Zammad host must be configured to support Kerberos
(and to accept auth credentials provided by the Active Directory server).

In most cases, you would have to recompile NGINX from source
with an extra module to enable Kerberos support.
To get around this, we will use Apache,
which offers Kerberos support through a plug-in module instead.

.. note:: All commands in this section must be run as root (or with ``sudo``).

2a. Turn Off NGINX
""""""""""""""""""

.. warning:: This will take your Zammad instance **offline**
   until Apache is fully configured and running.

Turn off Nginx:

.. code-block:: console

   $ sudo systemctl stop nginx

Keep it off after reboot:

.. code-block:: console

   $ sudo systemctl disable nginx

If you wish to minimize downtime, you can save this step for last;
just bear in mind that Apache will not start
if the port it wants to listen on is being used by NGINX.

If for any reason you can't complete this tutorial,
simply turn off Apache and restore NGINX:

.. code-block:: console

   $ sudo systemctl stop apache2

.. code-block:: console

   $ sudo systemctl disable apache2

.. code-block:: console

   $ sudo systemctl enable nginx

.. code-block:: console

   $ sudo systemctl start nginx

2b. Pre-Configure Apache
""""""""""""""""""""""""

This documentation expects a already working Apache configuration.
Please see :doc:`/getting-started/configure-webserver` before continuing.

2c. Install Further Apache Dependencies
"""""""""""""""""""""""""""""""""""""""

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install krb5-user libapache2-mod-auth-gssapi

   .. tab:: CentOS

      .. code-block:: console

         $ sudo dnf install krb5-workstation mod_auth_kerb

   .. tab:: OpenSUSE

      .. code-block:: console

         $ sudo zypper ref

      .. code-block:: console

         $ sudo zypper install krb5-client apache2-mod_auth_kerb

2d. Enable Apache Modules
"""""""""""""""""""""""""

SSO requires modules that are not enabled by default. By default you can use
``a2enmod`` to do so.

.. tabs::

   .. tab:: a2enmod (Ubuntu / Debian)

      .. code-block:: console

         $ a2enmod auth_gssapi rewrite

      .. code-block:: console

         $ sudo systemctl restart apache2

   .. tab:: a2enmod (OpenSUSE)

      .. code-block:: console

         $ a2enmod auth_kerb rewrite

      .. code-block:: console

         $ systemctl restart apache2

   .. tab:: via configuration file (CentOS)

      add/uncomment the appropriate ``LoadModule`` statements
      in your Apache config:

      .. code-block:: text

         # /etc/httpd/conf/httpd.conf

         LoadModule auth_kerb_module /usr/lib/apache2/modules/mod_auth_kerb.so
         LoadModule rewrite_module modules/mod_rewrite.so

.. _sso-configure-kerberos:

2e. Configure Kerberos
""""""""""""""""""""""

Kerberos realm configuration is how you tell the Zammad server
how to reach the *domain controller* (Active Directory server).

Replace the following placeholders in the sample config below:

:``<domain>``:                   Windows domain
:``<domain-controller>``:        Domain controller IP/FQDN(s)
:``<master-domain-controller>``: Master domain controller IP/FQDN

                                 (must not be read-only,
                                 but can be the same as ``<domain-controller>``)

.. code-block:: text

   # /etc/krb5.conf

   [libdefaults]
      default_realm = <DOMAIN>

      default_tkt_enctypes = aes256-cts-hmac-sha1-96
      default_tgs_enctypes = aes256-cts-hmac-sha1-96
      permitted_enctypes = aes256-cts-hmac-sha1-96

      kdc_timesync = 1
      ccache_type = 4
      forwardable = false
      proxiable = false
      fcc-mit-ticketflags = false

   [realms]
            # multiple KDCs ok (one `kdc = ...` definition per line)
            <DOMAIN> = {
                     kdc = <domain-controller>
                     admin_server = <master-domain-controller>
                     default_domain = <domain>

                     # below is only for GSSAPI
                     auth_to_local = RULE:[1:$1@$0](.*@<domain>)s/@<domain>$//
                     auth_to_local = DEFAULT
            }

   [domain_realm]
            .<domain> = <DOMAIN>
            <domain> = <DOMAIN>

.. _sso-generate-keytab:

2f. Generate Keytab
"""""""""""""""""""

Apache needs a Kerberos *keytab* (key table)
to manage its shared secrets with the domain controller.


Replace the following placeholders in the commands below:

:``<zammad-host>``: Zammad FQDN
:``<domain>``:      Windows domain
:``<secret-key>``:  Secret key (**omit the leading** ``0x``)
:``<vno>``:         Secret key version number

The secret key and version number were found in :ref:`sso-register-spn` above.

.. code-block:: console

   $ ktutil

   ktutil: addent -key -p HTTP/<zammad-host>@<DOMAIN> -k <vno> -e aes256-cts
   Key for HTTP/<zammad-host>@<domain> (hex): <secret-key>

   ktutil: list  # confirm the entry was added successfully
   slot KVNO Principal
   ---- ---- ---------------------------------------------------------------
      1    3 HTTP/<zammad-host>@<DOMAIN>

   ktutil: wkt /root/zammad.keytab  # write keytab to disk

   ktutil: quit

Then, place the keytab in the Apache config directory
and set the appropriate permissions:

.. tabs::

   .. tab:: Ubuntu, Debian, OpenSUSE

      .. code-block:: console

         $ sudo mv /root/zammad.keytab /etc/apache2/

      .. code-block:: console

         $ sudo chown root:www-data /etc/apache2/zammad.keytab

      .. code-block:: console

         $ sudo chmod 640 /etc/apache2/zammad.keytab

   .. tab:: CentOS

      .. code-block:: console

         $ sudo mv /root/zammad.keytab /etc/httpd/

      .. code-block:: console

         $ sudo chown root:apache /etc/httpd/zammad.keytab

      .. code-block:: console

         $ sudo chmod 640 /etc/httpd/zammad.keytab

2g. Configure Apache
""""""""""""""""""""

Add the following directive to the end of the virtual host configuration file
to create your Kerberos SSO endpoint at ``/auth/sso``:

Replace the following placeholders in the command below:

:``<zammad-host>``: Zammad FQDN
:``<domain>``:      Windows domain

The configuration for CentOS and OpenSUSE below contains two ``Krb5KeyTab``
lines! Keep only the one you need.

.. tabs::

   .. tab:: Ubuntu/Debian

      .. code-block:: apache

         # /etc/apache2/sites-available/zammad.conf

         <LocationMatch "/auth/sso">
            SSLRequireSSL
            AuthType GSSAPI
            AuthName "Your Zammad"
            GssapiBasicAuth On
            GssapiCredStore keytab:/etc/apache2/zammad.keytab
            GssapiLocalName On
            require valid-user

            RewriteEngine On
            RewriteCond %{LA-U:REMOTE_USER} (.+)
            RewriteRule . - [E=RU:%1,NS]
            RequestHeader set X-Forwarded-User "%{RU}e" env=RU
         </LocationMatch>

   .. tab:: CentOS/OpenSUSE

      .. code-block:: apache

         # /etc/apache2/sites-available/zammad.conf

         <LocationMatch "/auth/sso">
            SSLRequireSSL
            AuthType Kerberos
            AuthName "Your Zammad"
            KrbMethodNegotiate On
            KrbVerifyKDC On
            KrbMethodK5Passwd On
            KrbAuthRealms <DOMAIN>
            # strips @REALM suffix from REMOTE_USER variable
            KrbLocalUserMapping on
            KrbServiceName HTTP/<zammad-host>@<DOMAIN>
            # Ubuntu, Debian, & openSUSE
            Krb5KeyTab /etc/apache2/zammad.keytab
            # CentOS
            Krb5KeyTab /etc/httpd/zammad.keytab
            require valid-user

            RewriteEngine On
            RewriteCond %{LA-U:REMOTE_USER} (.+)
            RewriteRule . - [E=RU:%1,NS]
            RequestHeader set X-Forwarded-User "%{RU}e" env=RU
         </LocationMatch>

2h. Restart Apache to Apply Changes
"""""""""""""""""""""""""""""""""""

.. code-block:: console

   $ sudo systemctl restart apache2

.. _sso-docker:

Docker Installation
^^^^^^^^^^^^^^^^^^^

The Docker stack runs its web server inside the ``zammad-nginx`` image, so
you cannot swap it for Apache as in the package installation. Instead, a
small additional container does the Kerberos part: the reverse proxy in
front of the stack sends only ``/auth/sso`` through it, everything else goes
straight to ``zammad-nginx`` as before. Zammad and the stack's compose files
stay as they are; the SSO container is part of your infrastructure, like the
reverse proxy that terminates TLS.

.. code-block:: text

   browser ──► reverse proxy (TLS)
                 ├─ /auth/sso ──► zammad-sso ──(Kerberos ok, sets X-Forwarded-User)──► zammad-railsserver
                 └─ everything else ──────────────────────────────────────────► zammad-nginx ──► zammad-railsserver

The SSO container forwards ``/auth/sso`` to Zammad's application server
directly and passes the user name in the ``X-Forwarded-User`` header, as the
package installation does. One hop fewer, and ``zammad-nginx`` is not involved
in the login.

.. note:: **Your reverse proxy can do Kerberos itself?**

   Then you don't need the SSO container. Configure the proxy to
   authenticate ``/auth/sso`` via Negotiate, put the user name without the
   realm into the ``X-Forwarded-User`` header, drop ``Remote-User`` and
   ``X-Forwarded-User`` sent by clients on every path, send ``/auth/sso`` to
   ``zammad-railsserver:3000``, pass all other requests unchanged, and
   continue with :ref:`sso-docker-trusted-proxies`.

You need:

- the stack behind a reverse proxy that routes by path. This guide uses the
  :ref:`Nginx Proxy Manager scenario <add-nginx-proxy-manager>`; any proxy
  with path-based routing works the same way. If your proxy runs in a
  separate compose project, use the :ref:`external network scenario
  <add-external-network-to-nginx>` and add that network to the
  ``zammad-sso`` service in the override file as well, so that the proxy can
  reach it.
- the ``zammad.keytab`` file written by ``ktpass`` in :ref:`sso-register-spn`,
  copied to the Docker host. The ``ktutil`` step of the package installation
  is not needed.

Files
"""""

Create the following files next to the stack's ``docker-compose.yml``:

.. code-block:: text

   docker-compose.override.yml   adds the SSO container to the stack
   zammad-sso/                   build context of the SSO image
     Dockerfile
     apache2-foreground
     zammad-sso.conf
   local/zammad-sso/             files mounted into the container
     krb5.conf
     zammad.keytab

Keep the keytab out of the build context: Docker reads every file in
``zammad-sso/`` when it builds the image, and a keytab that only the
container's user may read makes the build fail. The container runs as
``www-data`` with user ID 33, so on a Linux host:

.. code-block:: console

   $ sudo chown 33 local/zammad-sso/zammad.keytab

.. code-block:: console

   $ sudo chmod 0400 local/zammad-sso/zammad.keytab

``zammad-sso/Dockerfile`` builds Apache with ``mod_auth_gssapi`` from the
Debian packages and runs it unprivileged:

.. code-block:: dockerfile

   FROM debian:trixie-slim

   RUN apt-get update && \
       apt-get install -y --no-install-recommends apache2 libapache2-mod-auth-gssapi krb5-user curl && \
       rm -rf /var/lib/apt/lists/*

   RUN a2enmod auth_gssapi proxy proxy_http headers rewrite && \
       a2dissite 000-default

   COPY zammad-sso.conf /etc/apache2/sites-available/zammad-sso.conf
   RUN a2ensite zammad-sso

   # Debian's envvars assigns the APACHE_* variables unconditionally. Turn every
   # "export VAR=value" into ": ${VAR:=value}; export VAR", so that values from the
   # environment win, the same way the official php:apache image does it.
   RUN sed -ri 's/^export ([^=]+)=(.*)$/: ${\1:=\2}\nexport \1/' /etc/apache2/envvars

   # Run unprivileged: listen on 8080, pid/lock/logs under /tmp.
   ENV APACHE_RUN_DIR=/tmp/apache2 \
       APACHE_PID_FILE=/tmp/apache2/apache2.pid \
       APACHE_LOCK_DIR=/tmp/apache2 \
       APACHE_LOG_DIR=/tmp/apache2

   RUN echo 'Listen 8080' > /etc/apache2/ports.conf && \
       { echo 'ServerName zammad-sso'; \
         echo 'ErrorLog /proc/self/fd/2'; \
         echo 'CustomLog /proc/self/fd/1 combined'; } > /etc/apache2/conf-available/zz-docker.conf && \
       a2enconf zz-docker

   COPY apache2-foreground /usr/local/bin/apache2-foreground

   USER www-data
   EXPOSE 8080

   # Healthy = the keytab is readable and apache answers /auth/sso with the Negotiate
   # challenge (401). A keytab with a wrong key is not detected here: apache still
   # answers 401 and logs a GSS ERROR for every sign-in attempt.
   HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
     CMD klist -k /etc/apache2/zammad.keytab >/dev/null 2>&1 && \
         [ "$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8080/auth/sso)" = "401" ] || exit 1

   CMD ["apache2-foreground"]

``zammad-sso/apache2-foreground`` starts Apache as the container's main
process. Make it executable with ``chmod +x``:

.. code-block:: sh

   #!/bin/sh
   # Start apache directly instead of through apache2ctl, so that it runs as PID 1
   # and receives the container's signals. The run directory is created on every
   # start and a stale pid file from a previous run is removed.
   set -e
   . /etc/apache2/envvars
   mkdir -p "$APACHE_RUN_DIR" "$APACHE_LOCK_DIR" "$APACHE_LOG_DIR"
   rm -f "$APACHE_PID_FILE"
   exec apache2 -DFOREGROUND "$@"

``zammad-sso/zammad-sso.conf`` authenticates ``/auth/sso`` and forwards it to
the stack:

.. code-block:: apache

   <VirtualHost *:8080>
     <Location "/auth/sso">
       AuthType GSSAPI
       AuthName "Zammad SSO"
       GssapiCredStore keytab:/etc/apache2/zammad.keytab
       GssapiAllowedMech krb5
       # strips @REALM
       GssapiLocalName On
       Require valid-user

       # inbound client values never survive
       RequestHeader unset Remote-User
       RequestHeader unset X-Forwarded-User
       RewriteEngine On
       RewriteCond %{LA-U:REMOTE_USER} (.+)
       RewriteRule . - [E=RU:%1,NS]
       RequestHeader set X-Forwarded-User "%{RU}e" env=RU
       # don't leak the Negotiate token downstream
       RequestHeader unset Authorization

       ProxyPreserveHost On
       ProxyPass        http://zammad-railsserver:3000/auth/sso
       ProxyPassReverse http://zammad-railsserver:3000/auth/sso
     </Location>
   </VirtualHost>

``docker-compose.override.yml`` adds the container:

.. code-block:: yaml

   ---
   services:
     zammad-sso:
       build: ./zammad-sso
       restart: ${RESTART:-always}
       volumes:
         - ./local/zammad-sso/krb5.conf:/etc/krb5.conf:ro
         - ./local/zammad-sso/zammad.keytab:/etc/apache2/zammad.keytab:ro

``local/zammad-sso/krb5.conf`` tells the container how to reach your domain
controller. Replace the placeholders as described in
:ref:`sso-configure-kerberos`:

.. code-block:: text

   [libdefaults]
       default_realm = <DOMAIN>
       dns_lookup_realm = false
       dns_lookup_kdc = false
       rdns = false

   [realms]
       <DOMAIN> = {
           kdc = <domain-controller>
           admin_server = <master-domain-controller>
       }

   [domain_realm]
       .<domain> = <DOMAIN>
       <domain> = <DOMAIN>

Add the override file and the reverse proxy as trusted proxy to your
``.env``:

.. code-block:: text

   COMPOSE_FILE=docker-compose.yml:scenarios/add-nginx-proxy-manager.yml:docker-compose.override.yml
   ZAMMAD_FQDN=<zammad-host>
   ZAMMAD_HTTP_TYPE=https
   RAILS_TRUSTED_PROXIES=nginx-proxy-manager

Then build and start the stack:

.. code-block:: console

   $ docker compose up -d --build

The ``zammad-sso`` container reports ``healthy`` once the keytab is readable
and Apache answers ``/auth/sso`` with the Kerberos challenge. If it stays
unhealthy, the keytab is missing or not readable by user ID 33.

Configure the Reverse Proxy
"""""""""""""""""""""""""""

In Nginx Proxy Manager:

1. Create a proxy host for your Zammad FQDN with scheme ``http``, forward
   host ``zammad-nginx`` and port ``8080``. Enable *Websockets Support* and
   set up the certificate on the *SSL* tab.
2. Add a *Custom Location* for ``/auth/sso`` with scheme ``http``, forward
   host ``zammad-sso`` and port ``8080``.

Do not rely on the *Advanced* field to strip headers: ``proxy_set_header``
lines entered there do not reach the generated locations and would only
give a false sense of security. Client-sent headers are removed in the SSO
container.

With Traefik, the equivalent is a router that points at the SSO container,
with a higher priority than the router for the rest of the stack and the rule:

.. code-block:: text

   Host(`<zammad-host>`) && PathPrefix(`/auth/sso`)

.. _sso-docker-trusted-proxies:

Trusted Proxies
"""""""""""""""

Zammad has to trust the reverse proxy, so that it takes the address of the
user's browser as the client instead of a container address. That is what
``RAILS_TRUSTED_PROXIES`` in ``.env`` does; with another proxy, name that one
instead, see :doc:`/appendix/environment-variables`. The SSO container does
not need to be listed: Zammad takes the address the reverse proxy forwarded
and falls back to the sending container only when no untrusted forwarded
address is left.

The *Trusted SSO Proxy IPs* setting in :ref:`sso-enable` then holds the
address ranges from which users may sign in via SSO, typically your intranet.
A changed value applies after at most 15 seconds. Without the reverse proxy
in ``RAILS_TRUSTED_PROXIES``, Zammad takes a container's address as the
client, and the setting would have to hold the stack's network range, which
admits every container.

.. warning:: The setting guards the way in through the reverse proxy only.
   Inside the stack's network, ``zammad-railsserver`` accepts an
   ``X-Forwarded-User`` header from any container, and a container can send
   the ``X-Forwarded-For`` header the check relies on along with it. Keep
   ``zammad-railsserver`` reachable only from the stack's own containers and
   the SSO container, and set the trusted IPs before you enable SSO.

Portainer
"""""""""

Without shell access to the Docker host, you can build and run the same
container through the Portainer UI:

1. *Images → Build a new image*: upload a tarball that contains the three
   files of ``zammad-sso/`` at its top level (not the directory itself) and
   tag the image, e.g. ``zammad-sso:local``. The image contains no keytab, so
   it holds no secret.
2. *Volumes → Add volume*: create ``zammad-sso-secrets``.
3. Put ``zammad.keytab`` and ``krb5.conf`` into the volume. Portainer Business
   has a volume browser with upload. In the Community Edition, deploy a
   throwaway container (``alpine`` with the command ``sleep infinity``) that
   mounts the volume at ``/secrets``, paste the files through its console
   (for example via ``base64 -d``), set owner ``33`` and mode ``0400`` on the
   keytab, and remove the container again.
4. *Stacks → Add stack* with the web editor: deploy the SSO container as a
   stack of its own that joins the Zammad stack's network. Replace
   ``<zammad-stack>`` with the name of your Zammad stack in Portainer.

   .. code-block:: yaml

      services:
        zammad-sso:
          image: zammad-sso:local
          restart: always
          volumes:
            - type: volume
              source: zammad-sso-secrets
              target: /etc/krb5.conf
              read_only: true
              volume:
                subpath: krb5.conf
            - type: volume
              source: zammad-sso-secrets
              target: /etc/apache2/zammad.keytab
              read_only: true
              volume:
                subpath: zammad.keytab
          networks:
            - zammad

      networks:
        zammad:
          external: true
          name: <zammad-stack>_default

      volumes:
        zammad-sso-secrets:
          external: true

The reverse proxy is configured as above and has to be a trusted proxy of the
Zammad stack, see :ref:`sso-docker-trusted-proxies`.

.. _sso-enable:

Step 3: Enable SSO in Zammad
----------------------------

Next, enable "Authentication via SSO" in Zammad's admin settings under
*Settings > Security > Third-party Applications*. Make sure to configure the
trusted SSO proxy IPs for production systems. For the Docker stack,
:ref:`sso-docker-trusted-proxies` explains which addresses belong there.

.. figure:: /images/appendix/single-sign-on/authentication-via-sso.png
   :align: center
   :alt: Screenshot shows SSO configuration in Zammad.

Step 4: Configure Client System (Windows Only)
----------------------------------------------

For the full SSO experience (*i.e.,* for passwordless, one-click sign-in),
Zammad users must:

1. be on the Active Directory server's local intranet; and
2. modify their network settings for the Zammad host
   to be treated as a local intranet server.

.. figure:: /images/appendix/single-sign-on/password-prompt-non-ad-member.png
   :align: center
   :alt: In-browser login prompt for single sign-on

   Without this step, users must enter their Active Directory credentials during SSO.

.. tabs::

   .. tab:: IE / Edge / Chromium

      .. tip:: This setting can be centrally managed across the entire intranet
         using a **group policy object** (GPO).

      1. Add your Zammad FQDN in Internet Options
         under **Security > Local Intranet > Sites > Advanced**.
      2. Select "Require server verification (https:) for all sites in this zone".
      3. Under **Security level for this zone > Custom level... > Settings >
         User Authentication > Logon**,
         select "Automatic logon only in Intranet Zone".

   .. tab:: Firefox

      .. note:: This option cannot be centrally managed
         because it is set in the browser rather than Windows Settings.

      1. Enter ``about:config`` in the address bar.
         Click **Accept the risk and continue**.
      2. Search for the ``network.negotiate-auth.trusted-uris`` option.
      3. Double-click to edit, then add your Zammad FQDN.
      4. Restart Firefox to apply your changes.

.. _sso-troubleshooting:

Troubleshooting
---------------

- Are all relevant FQDNs/hostnames reachable
  from your Active Directory and Zammad servers (including each other's)?
- Are the system clocks of your Active Directory and Zammad servers synchronized
  within five minutes of each other?
  (Kerberos is a time-sensitive protocol.)

Errors in Apache Logs
^^^^^^^^^^^^^^^^^^^^^

.. tip:: **Try raising your Apache log level temporarily.**

   Add ``LogLevel debug`` to your virtual host configuration,
   then restart the service to apply the changes.

"an unsupported mechanism was requested"
   Does your Active Directory service account have **Kerberos AES 256-bit encryption** enabled?

   If for some reason your server does not support AES 256-bit encryption,
   the LDAP Wiki has `more information about Kerberos encryption types
   <https://ldapwiki.com/wiki/MsDS-SupportedEncryptionTypes>`_.

"failed to verify krb5 credentials: Key version is not available"
   Did you use the exact **version number** (``vno``) provided by ``ktpass``
   when :ref:`generating your keytab <sso-generate-keytab>`?

   Try generating it again, just to be sure.

"unspecified GSS failure. Minor code may provide more information (, No key table entry found for HTTP/FQDN\@DOMAIN)"
   Does the **service name** you provided to ``setspn`` exactly match
   the one you used when :ref:`generating your keytab <sso-generate-keytab>`?

   Try generating it again, just to be sure.

"No key table entry found for HTTP/FQDN\@DOMAIN"
   Does your virtual host configuration's ``KrbServiceName`` setting
   exactly match the **service name** you provided to ``setspn``?

   This setting is case-sensitive.

"Warning: received token seems to be NTLM, which isn't supported by the Kerberos module. Check your IE configuration"
   Is your Zammad host accessible at an FQDN?
   This error may indicate that you configured your Zammad host
   as a numeric IP address instead.

"Cannot decrypt ticket for HTTP/FQDN\@DOMAIN"
   Did you make sure to change the password
   on your Active Directory service account
   *after enabling 256-bit AES encryption?*

   And did you make sure to register the SPN (with ``ktpass``)
   and generate your keytab (with ``ktutil``)
   *after changing your password?*

   Try running ``kinit -k -t <path to keytab> HTTP/<zammad-host>@<DOMAIN>``.
   If no output is returned, you're good - if you see
   "kinit: Preauthentication failed while getting initial credentials"
   your credentials provided were wrong or you used ``/pass *`` during ktpass
   command.

"failed when verifying KDC" and "failed to verify krb5 credentials: Decrypt integrity check failed"
   Ensure ``KrbServiceName`` is the correct ServiceName provided via setspn.

   Ensure your Active Directory supports the encryption method configured.

   If all above is correct and the rest of FAQ also is ensured, make sure your
   client does not cache the results.
   ``klist purge`` clears the clients cache - a reboot of your client would do too.

Docker Stack
^^^^^^^^^^^^

"502 Bad Gateway" on ``/auth/sso`` only, after recreating the SSO container
   The reverse proxy still holds the container's old address. Nginx Proxy
   Manager resolves the name only when it loads its configuration, so reload
   it: ``docker compose exec nginx-proxy-manager nginx -s reload``.

Signing in via SSO fails although the ``zammad-sso`` container is healthy
   The health check verifies that the keytab is readable and that Apache
   issues the Kerberos challenge; it cannot verify the key itself. Check
   ``docker compose logs zammad-sso``: a line ``GSS ERROR … cannot decrypt
   ticket`` means the keytab does not match the service account's current
   key, usually because it was exported before the last password reset.
   Export it again as described in :ref:`sso-register-spn`.
