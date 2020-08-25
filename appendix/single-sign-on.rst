Single Sign On
**************

Zammad provides many ways for authentication. Most of these options don't require any 
further configuration on your host. However, if you want to use Kerberos based SSO, this 
guide will help you through!

.. figure:: /
   :alt: Login screen showing SSO buttons
   :align: center

.. warning:: 🤓 **Please note the following limitations**

   **Kerberos Single Sign On is limited to self hosted setups only - Hosted Users can't use this option!**
   
   This guide expects a Windows Active Directory environment which supports AES 256bit encryption. 
   As on most things in these environments, you may need to adjust some commands and configurations to 
   your own environment! Some Linux commands and usernames mentioned may greatly differ on your OS! 

   **Proof of Concept System:**
   To help you to see the scope of this Guide, the following systems and software versions were used 
   during testing and writing this guide.

   * Active Directory version 2016 (on a Windows Server 2016)
   * Debian 10
   * Zammad 3.4

.. note:: 🤔 **Don't want to use Kerberos but still use the SSO endpoint?!**
   
   As it's impossible to cover all possible use cases here's the minimum information 
   that Zammad does require to use the SSO endpoint.

   | *Endpoint*: ``/auth/sso``
   | *Accepted Header*: ``X-Forwarded-User``
   | *Accepted ENV*: ``REMOTE_USER`` OR ``HTTP_REMOTE_USER``

   Zammad expects either one of the above ENV or Header. You can choose what's the best in your use case.

   The header or ENV does have to contain the ``login`` attribute of the user. 
   The user has to be present in Zammad!

   **Important:** 
   Above does not apply to existing third party authentications. 
   Please check our `third party authentication page <https://admin-docs.zammad.org/en/latest/settings/security.html#third-party-applications>`_ before! This may save your time.

.. hint:: 😵 **Still puzzled and got lost?**
   
   No worries, we got you covered. If you require, we'll gladly provide commercial support on this topic. 
   Our consultants will gladly tailor a custom workshop for you - 
   `just drop us a line <https://zammad.com/contact>`_.

Requirements
=============

Please ensure that the following points apply to you and your environment:

   * you'll need root access to your Zammad host
   * you'll need administrative access to your Active Directory
   * you know how to configure a basic apache installation

.. tip:: For best experience with kerberos based authentication, we suggest 
   using the Zammad `LDAP integration <https://admin-docs.zammad.org/en/latest/system/integrations/ldap.html>`_. 
   Even if you don't want to use it for authentication directly, it will automatically sync your users to 
   Zammad.

Prerequisites
=============

First of all we'll need a service account in your Active Directory. 
This user does not need any specific or administrative rights - a normal user will do! 

Open the accounts properties, change to the "Account" tab and enable the account option 
"This account supports Kerberos AES 256bit encryption.". Apply your changes.

If you have your user configured, open an administrative CMD and run the following commands. 
Note that we're using placeholders put in ``{}`` - adjust them to your environment!

.. code-block:: sh

   $ setspn -s HTTP/{Zammad-FQDN} {Zammad-Service-Account}
   $ ktpass /princ {Zammad-Service-Account}@{DOMAIN.TLD} /mapuser {Zammad-Service-Account} /crypto AES256-SHA1 /ptype KRB5_NT_PRINCIPAL /pass {Password-of-Service-Account} -SetPass +DUmpSalt /target {Master-DC} /out zammad.keytab

Above command will return something like below - note down **vno** (the number) and the key (starts with ``(0x``)). 

.. code-block:: sh
   
   Using legacy password setting method
   Failed to set property 'servicePrincipalName' to 'zammadsrv' on Dn 'CN=Zammad Service,DC=tha,DC=dev': 0x13.
   WARNING: Unable to set SPN mapping data.
   If zammadsrv already has an SPN mapping installed for zammadsrv, this is no cause for concern.
   Building salt with principalname zammadsrv and domain THA.DEV (encryption type 18)...
   Hashing password with salt "THA.DEVzammadsrv".
   Key created.
   Output keytab to zammad.keytab:
   Keytab version: 0x502
   keysize 67 zammadsrv@THA.DEV ptype 1 (KRB5_NT_PRINCIPAL) vno 3 etype 0x12 (AES256-SHA1) keylength 32 (0x5ee827c30c736dd4095c9cbe146eabc216415b1ddb134db6aabd61be8fdf7fb1)

So based on above sample, you'd note ``3`` for vno and 
``0x5ee827c30c736dd4095c9cbe146eabc216415b1ddb134db6aabd61be8fdf7fb1`` for the key. 
We'll need these information in the next step on our Zammad host.

Configure your Zammad-Host to allow Kerberos authentication
===========================================================

On this step we'll configure your Zammad host to support kerberos authentication and will 
switch from nginx to apache2. The following steps have to be run as administrative (root) 
user and expect the base directory ``/root``.

   .. note:: Apache2 is a fixed requirement for this approach, as nginx does not support kerberos authentication 
      out of the box. Compiling sources would exceed the possibilities of this documentation.

Stop & Disable nginx (if applicable)
   .. note:: This temporary draws your Zammad installation not reachable. 
      You can run below step as last step as well, however, there will be 
      error messages regarding used ports apache2 will try to use.

   .. code-block:: sh

      $ systemctl disable nginx; systemctl stop nginx

Install dependencies
   .. code-block:: sh

      # Ubuntu & Debian
      $ apt update
      $ apt install apache2 krb5-user libapache2-mod-auth-kerb

      # CentOS
      $ yum install httpd krb5-workstation mod_auth_kerb

      # openSUSE
      $ zypper ref
      $ zypper install apache2 krb5-client apache2-mod_auth_kerb

Enable required apache modules
   .. code-block:: sh

      # This step should work for all systems, on some systems ``a2enmod`` may not be available
      $ a2enmod auth_kerb headers rewrite proxy proxy_html proxy_http proxy_wstunnel

Configure KRB5 for your Realm
   This step will tell your system which server to contact for any realm it may need to handle. 
   The file you want to adjust here is ``/etc/krb5.conf``. You can use below version and adjust it.

   .. code-block:: sh

      [libdefaults]
        default_realm = {DOMAIN.TLD}
        default_tkt_enctypes = aes256-cts-hmac-sha1-96
        default_tgs_enctypes = aes256-cts-hmac-sha1-96
        permitted_enctypes = aes256-cts-hmac-sha1-96

        kdc_timesync = 1
        ccache_type = 4
        forwardable = true
        proxiable = true
        fcc-mit-ticketflags = true

      [realms]
              {DOMAIN.TLD} = {
                      # you can define more than one kdc (each on it's own line)
                      # this allows you to provide secondaries if needed
                      kdc = {IP / FQDN of domain controller}
                      # admin_server can be the same as kdc if it's not read only
                      admin_server = {IP / FQDN of master domain controller}
                      default_domain = {DOMAIN.TLD}
              }

      [domain_realm]
               # the point in front of domain.tld on the next line is no error!
              .{DOMAIN.TLD} = {DOMAIN.TLD}
              {DOMAIN.TLD} = {DOMAIN.TLD}

Create keytab file (requires secret from Windows Server)
   During keytab creation, you'll be asked for the secret key you noted earlier. 
   Provide ktutil with your key **without** ``0x``.

   .. code-block:: sh

      # add your windows principal
      $ ktutil
      ktutil: $ addent -key -p HTTP/{Zammad-FQDN} -k {vno-number} -e aes256-cts
      Key for HTTP/{Zammad-FQDN}@{DOMAIN.TLD} (hex):  $ {secret-key-without-0x}

      # list your principals to verify you're good to go
      ktutil: $ list

      # write your keytab file and quit ktutil
      ktutil: $ wkt zammad.keytab
      ktutil: $ quit

   .. hint:: A listing of your keytab looks similar to the following.

      .. code-block:: sh
         
         ktutil:  list
         slot KVNO Principal
         ---- ----       ---------------------------------------------------------------------
            1    3       HTTP/172.16.16.3@THA.DEV

Move and prepare keytab file
   .. code-block:: sh

      $ mv /root/zammad.keytab /etc/apache2/
      
      # Adjust ownership to webserver user #
      # webserver user and directory may depend on your OS
      $ chown www-data:www-data /etc/apache2/zammad.keytab
      $ chmod 400 /etc/apache2/zammad.keytab

Extend your vHost configuration
   .. hint:: If you didn't use apache up to now, you'll find a generic 
      sample vHost file here: ``/opt/zammad/contrib/apache2/zammad_ssl.conf``. 

      Configuration of said vHost file is out of scope of this documentation.

   Adjust the vHost file of your Zammad-vHost (usually in ``/etc/apache2/sites-available/``) 
   and add the following. Ensure to add below **to the end** of the configuration.

   .. code-block:: sh

      # SSO magic against Kerberos happens here
      <LocationMatch "/auth/sso">
         SSLRequireSSL
         AuthType Kerberos
         AuthName "Your Zammad"
         KrbMethodNegotiate On
         KrbMethodK5Passwd On
         KrbAuthRealms {DOMAIN.TLD}
         KrbLocalUserMapping on     # set to off if you don't
                                    # want to strip away your REALM
         KrbServiceName HTTP/{Zammad-FQDN}@{DOMAIN.TLD}
         Krb5KeyTab /etc/apache2/zammad.keytab
         require valid-user

         RewriteEngine On
         RewriteCond %{LA-U:REMOTE_USER} (.+)
         RewriteRule . - [E=RU:%1,NS]
         RequestHeader set X-Forwarded-User "%{RU}e" env=RU        
      </LocationMatch>

Restart apache to apply your changes
   .. code-block:: sh

      $ systemctl restart apache2

With this your system technically is able to authenticate against a Kerberos source. 
In order to trigger it, you have to open ``https://{zammadFQDN}/auth/sso`` in your Browser.

Enable SSO authentication within Zammad
=======================================

Starting with Zammad 3.5 you're provided a sso button within the login interface. 
To enable SSO authentication and it's button, go to Security and activate "Authentication via SSO" 
within "Third-party Applications" tab.

.. figure:: /images/appendix/single-sign-on/authentication-via-sso.png

Adjusting client configuration
==============================

.. note:: This step only works on machines that are member of your Active Directory!
   If you ignore below steps or the machine is not an AD member, you'll get a login prompt.

   .. figure:: /images/appendix/single-sign-on/password-prompt-non-ad-member.png

Internet Explorer

Edge

Firefox

Google Chrome


Troubleshooting
===============

You may stumble upon issues in some situations. The above guide should avoid them, but we thought 
below may still help. These error messages can be found within your apaches webserver log.

an unspported mechanism was requested (unsupported etype - server might not support AES256)
   Ensure that the service account you're using has the correct kerberos encryption enabled. 
   In the guide we expect to use AES256 bit encryption, but you may have adjusted if needed. 
   The `LDAP-Wiki <https://ldapwiki.com/wiki/MsDS-SupportedEncryptionTypes>`_ page is a great 
   source of further hints for encryption types for kerberos.

failed to verify krb5 credentials: Key version is not available
   This inidicates that you provided a wrong vno number during keytab 
   creation. Repeat the keytab creation. 
   ( ``vno {number}`` must have the same number for ``-k {number}`` (keytab))

unspecified GSS failure. Minor code may provide more information (, No key table entry found for HTTP/FQDN@DOMAIN)
   Indicates your provided a wrong service name - either on your Active Directory controller 
   or while using ktutil.

still broken?!
   * Ensure that both your Active Directory controller and Zammad can lookup all affected 
     hostnames. This included the Active Directory domain and especially the FQDN of Zammad.
   * Make sure that the time between the Zammad host and Active Directory server does not drift 
     more than 5 minutes. Kerberos is very time sensitive.
