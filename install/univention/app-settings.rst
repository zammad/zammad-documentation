Univention App-Settings
***********************

.. include:: /install/univention/deprecation-warning.rst

.. note:: The App-Settings part is only valid starting with App version 3.1.0-7.

Within the management interface of Univention, you can change some access
related settings:

  * FQDN of Zammad (Domain you can access it from)
  * Another Port
  * Other certificates beside the Univention certificate

.. note::

   Some settings require you to have a combination of the above settings.
   If the combination of settings is not met, the update script will
   automatically revert these changes.

   This ensures that your Univention Host stays operational. Please do not try
   to trick the scripts, it might cause outages.

If you're using the default settings, we'll empty the values of the text fields
to reduce confusion. This is not a bug, but a "feature".


Using another FQDN
==================

This consists of two settings: a selection and a text field.
The default setting of the App is ``Default UCS-Hostname`` which will use the
FQDN of the Univention-Host (and it's SSL-Certificate).

.. note::

   In order to use custom hostnames, please also ensure to use a custom
   certificate.

If you set ``Custom Hostname``, you'll need to enter a hostname in the text
field below. Ensure that your Univention host can resolve the hostname
(and it's pointing to the host in question!).

.. note:: We won't create any DNS entries or certificates during this process.


Using another Port
==================

Currently you can choose between ``Default Highport`` and ``Port 8443``.
By default, we'll use Port ``10412`` for Zammad, if you decide for Port
``8443``, we'll handle the firewall steps needed and adjust the vHosts-Port.

.. warning::

   Please ensure that if you choose another Port, that it's not used already!
   We do not verify this!

.. note::

   Please note that for technical reasons (how Univention and Zammad work) it's
   not possible to use Zammad on Port 443 or within a sub directory.


Using other certificates
========================

By default we're using the Univention-Host certificate
(``Univention (default)``). In some cases
(and especially if you're using custom hostnames) this might be troublesome.

.. note:: You can use custom certificates without changing the hostname.

.. warning::

   We're not verifying if the certificates are valid in any way
   (e.g. still valid in time and if the hostname is inside). This step might
   follow, but please be aware that this might lead to certificate issues.


If you choose ``Let's Encrypt``, please ensure that you already have installed
the ``Let's Encrypt App`` (by Univention GmbH) and also already aquired a
certificate via it. If you're applying the settings, we'll check for the 
following two files:

   .. code-block::

      /etc/univention/letsencrypt/signed_chain.crt
      /etc/univention/letsencrypt/domain.key

If we can't find these, we'll revert to the default Univention certificate.


You can also choose to use your very own certificate by selecting
``Custom Certificate``. For this it's important to know, that we expect the
certificate to be within a specific location (``/etc/univention/ssl/``).
Within the two text fields, you'll need to provide the filenames of your
certificate and your certificate-key.

These certificates can be kept in a sub folder. If we cannot find either of the
two files, we reset the setting to the default Univention certificate.
