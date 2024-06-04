Query and set / update Zammad settings
**************************************

.. include:: /admin/console/missing-commands-ask-community.include.rst

ticket_hook setting
-------------------

This will give you the ticket hook that you'll find inside the ``[]`` in front
of the ticket number. By default this will be `Ticket#` - you shouldn't change
this setting in a productive system.

.. code-block:: ruby

   >> Setting.get('ticket_hook')

FQDN setting
------------

Get the current FQDN setting of Zammad and, if needed, adjust it.

.. note::

   This setting has no effect on SSL certificates or any web server
   configurations.

.. code-block:: ruby

   >> Setting.get('fqdn')                    # Get current FQDN
   >> Setting.set('fqdn', 'new.domain.tld')  # Set a new FQDN

HTTP(s) setting
---------------

This setting indirectly belongs to your FQDN setting and is relevant for
variable based URLs (e.g. in notifications) Zammad generated.

.. warning::

   This setting also affects Zammad's CSRF token behavior.
   If you set this setting to e.g. HTTPs but you're using HTTP,
   *logging in will fail*!

.. note::

   This setting has no effect on SSL certificates or any web server
   configurations.

.. code-block:: ruby

   >> Setting.get('http_type')            # Get the current http type
   >> Setting.set('http_type', 'https')   # Change the http type to HTTPs

Storage provider setting
------------------------

The storage provider setting is set to ``DB`` on default installations.
However, if you receive a lot of attachments or have a fairly busy installation,
using the database to store attachments is not the best approach.

Use the following command

.. code-block:: ruby

   >> Setting.get('storage_provider')               # get the current Attachment-Storage
   >> Setting.set('storage_provider', 'DB')         # Change Attachment-Storage to database

If you have already stored files and want to move them, you can use the
following example. Please be aware that this operation should only be executed
in non-productive environments. In case you have to perform it in production
environments, you should specify a sleep delay - otherwise your Zammad can be
unresponsive.

.. code-block:: ruby

   >> Store::File.move('DB', 'File', delay_in_sec)  # Move files from DB to File with a specified delay after each file in seconds, e.g. 1

The following settings are available in a default installation:

   * ``DB`` (database)
   * ``File`` (Filesystem (``/opt/zammad/storage/``))

Configuring Elasticsearch
-------------------------

If your Elasticsearch installation changes, you can use the following commands
to ensure that Zammad still can access Elasticsearch.

.. code-block:: ruby

   >> Setting.set('es_url', 'http://127.0.0.1:9200')           # Change elasticsearch URL to poll
   >> Setting.set('es_user', 'elasticsearch')                  # Change elasticsearch user (e.g. for authentication)
   >> Setting.set('es_password', 'zammad')                     # Change the elasticsearch password for authentication
   >> Setting.set('es_index', Socket.gethostname + '_zammad')  # Change the index name
   >> Setting.set('es_attachment_ignore', %w[.png .jpg .jpeg .mpeg .mpg .mov .bin .exe .box .mbox])  # A list of ignored file extensions (they will not be indexed)
   >> Setting.set('es_attachment_max_size_in_mb', 50)          # Limit the Attachment-Size to push to your elasticsearch index
   >> Setting.set('es_ssl_verify', 'false')                    # Turn SSL verification on or off

Enable proxy
------------

Zammad needs to use a proxy for network communication? Set it here.

.. code-block:: ruby

   >> Setting.set('proxy', 'proxy.example.com:3128')
   >> Setting.set('proxy_username', 'some user')
   >> Setting.set('proxy_password', 'some pass')
