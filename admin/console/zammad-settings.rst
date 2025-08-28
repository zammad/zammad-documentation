Query and Set / Update Zammad Settings
======================================

.. include:: /admin/console/missing-commands-ask-community.include.rst

Auto Shutdown Setting
---------------------

Defines if an automatic shutdown of Zammad is performed
when the the database has been changed
(e.g. after custom attributes have been created in the
:admin-docs:`object manager </system/objects.html>`).
The underlying system (Systemd, Docker, Kubernetes) will then restart the
processes/containers after this shutdown.

Default: **true**

Setting this to ``false`` might only make sense in very rare cases and you
have to restart the Zammad services then manually.

.. code-block:: irb

   >> Setting.set('auto_shutdown', 'true')

Ticket_hook Setting
-------------------

This will give you the ticket hook that you'll find inside the ``[]`` in front
of the ticket number. By default this will be `Ticket#` - you shouldn't change
this setting in a productive system.

.. code-block:: irb

   >> Setting.get('ticket_hook')

FQDN Setting
------------

Get the current FQDN setting of Zammad and, if needed, adjust it.

.. note::

   This setting has no effect on SSL certificates or any web server
   configurations.

Get current FQDN:

.. code-block:: irb

   >> Setting.get('fqdn')

Set a new FQDN:

.. code-block:: irb

   >> Setting.set('fqdn', 'new.domain.tld')

HTTP(s) Setting
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

Get the current http type:

.. code-block:: irb

   >> Setting.get('http_type')

Change the http type to ``https``:

.. code-block:: irb

   >> Setting.set('http_type', 'https')

Storage Provider Setting
------------------------

The storage provider setting is set to ``DB`` on default installations.
However, if you receive a lot of attachments or have a fairly busy installation,
using the database to store attachments is not the best approach.

Get the current attachment storage method:

.. code-block:: irb

   >> Setting.get('storage_provider')

Change Attachment-Storage to database:

.. code-block:: irb

   >> Setting.set('storage_provider', 'DB')

If you have already stored files and want to move them, you can use the
following example. Please be aware that this operation should only be executed
in non-productive environments. In case you have to perform it in production
environments, you should specify a sleep delay - otherwise your Zammad can be
unresponsive.

Move files from ``DB`` to ``File`` with a specified delay after each file in
seconds, e.g. ``1``:

.. code-block:: irb

   >> Store::File.move('DB', 'File', delay_in_sec)

The following settings are available in a default installation:

   * ``DB`` (database)
   * ``File`` (Filesystem (``/opt/zammad/storage/``))

Configuring Elasticsearch
-------------------------

If your Elasticsearch installation changes, you can use the following commands
to ensure that Zammad still can access Elasticsearch.

Change elasticsearch URL:

.. code-block:: irb

   >> Setting.set('es_url', 'http://127.0.0.1:9200')

Set elasticsearch user (e.g. for authentication):

.. code-block::

   >> Setting.set('es_user', 'elasticsearch')

Set the password for authentication of the elasticsearch user:

.. code-block:: irb

   >> Setting.set('es_password', 'zammad')

Change the index name:

.. code-block:: irb

   >> Setting.set('es_index', Socket.gethostname + '_zammad')

Set ignored file extensions / file types (they will not be indexed):

.. code-block:: irb

   >> Setting.set('es_attachment_ignore', %w[.png .jpg .jpeg .mpeg .mpg .mov .bin .exe .box .mbox])

Set the maximum attachment to be indexed by elasticsearch:

.. code-block:: irb

   >> Setting.set('es_attachment_max_size_in_mb', 50)

Turn SSL verification off (or on by using ``true``):

.. code-block:: irb

   >> Setting.set('es_ssl_verify', 'false')

Enable Proxy
------------

Zammad needs to use a proxy for network communication? Set it here.

Set proxy address:

.. code-block:: irb

   >> Setting.set('proxy', 'proxy.example.com:3128')

Set proxy user:

.. code-block:: irb

   >> Setting.set('proxy_username', 'some user')

Set proxy user's password:

.. code-block:: irb

   >> Setting.set('proxy_password', 'some pass')


.. _disable-asciifold:

Disable Asciifold
-----------------

This feature is turned on by default. In case you need a more exact search, you
can turn it off:

.. code-block:: irb

   >> Setting.set('es_asciifolding', false)

After changing the setting, make sure to
:ref:`rebuild the search index <es-rebuild-searchindex>`.