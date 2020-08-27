Getting and Updating Zammad-Settings
************************************

.. note:: Please note that this is not a full setting list, if you're missing settings, feel free to ask over at the `Community <https://community.zammad.org>`_.


Get ticket_hook setting
-----------------------

This will give you the Ticket hook that you'll find inside the `[]` in front of the ticket number.
By default this will be `Ticket#` - you shouldn't change this setting in a productive system.

.. code-block:: ruby

   >> Setting.get('ticket_hook')


Get fqdn setting
----------------

Get the current FQDN-Setting of Zammad and, if needed, adjust it.

.. code-block:: ruby

   >> Setting.get('fqdn')                    # Get FQDN
   >> Setting.set('fqdn', 'new.domain.tld')  # Set a new FQDN


Find storage_provider setting
----------------------------

The following command returns a list of available settings for `storage_provider` (for attachments).

.. code-block:: ruby

   >> Setting.find_by(name: 'storage_provider')


Set storage_provider Setting
----------------------------

Change the storage_provider if needed.

.. code-block:: ruby

   >> Setting.set('storage_provider', 'DB')  # Change Attachment-Storage to database
   >> Setting.get('storage_provider')        # get the current Attachment-Storage


Configuring Elasticsearch
-------------------------

If your elasticsearch installation changes, you can use the following commands to ensure that Zammad still can access elasticsearch.

.. code-block:: ruby

   >> Setting.set('es_url', 'http://127.0.0.1:9200')           # Change elasticsearch URL to poll
   >> Setting.set('es_user', 'elasticsearch')                  # Change elasticsearch user (e.g. for authentication)
   >> Setting.set('es_password', 'zammad')                     # Change the elasticsearch password for authentication
   >> Setting.set('es_index', Socket.gethostname + '_zammad')  # Change the index name
   >> Setting.set('es_attachment_ignore', %w[.png .jpg .jpeg .mpeg .mpg .mov .bin .exe .box .mbox])  # A list of ignored file extensions (they will not be indexed)
   >> Setting.set('es_attachment_max_size_in_mb', 50)          # Limit the Attachment-Size to push to your elasticsearch index


Use the OTRS importer from the shell
------------------------------------

If needed, you can configure and run the OTRS-Import from console.

.. code-block:: ruby

   >> Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
   >> Setting.set('import_otrs_endpoint_key', 'xxx')
   >> Setting.set('import_mode', true)
   >> Import::OTRS.start


Enable proxy
------------

Zammad needs to use a proxy for network communication? Set it here.

.. code-block:: ruby

   >> Setting.set('proxy', 'proxy.example.com:3128')
   >> Setting.set('proxy_username', 'some user')
   >> Setting.set('proxy_password', 'some pass')
