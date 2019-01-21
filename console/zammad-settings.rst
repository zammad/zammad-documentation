Getting and Updating Zammad-Settings
************************************

.. Note:: Please note that this is not a full setting list, if you're missing settings, feel free to ask over at our `Community <https://community.zammad.org>`_.


Send all outgoing E-Mails to a BCC-Mailbox
------------------------------------------

::
 
 rails> Setting.set('system_bcc', 'alias@domain.tld')

 
::
 
 rails> Setting.get('system_bcc')


Get ticket_hook setting
-----------------------

::

 rails> Setting.get('ticket_hook')


Get fqdn setting
----------------

::

 rails> Setting.get('fqdn')


Find storage_provide setting
----------------------------

::

 rails> Setting.find_by(name: 'storage_provider')


Set storage_rpovider Setting
----------------------------

::

 rails> Setting.set('storage_provider', 'DB')


Configuring Elasticsearch
-------------------------

::

 rails> Setting.set('es_url', 'http://127.0.0.1:9200')
 rails> Setting.set('es_user', 'elasticsearch')
 rails> Setting.set('es_password', 'zammad')
 rails> Setting.set('es_index', Socket.gethostname + '_zammad')
 rails> Setting.set('es_attachment_ignore', [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )
 rails> Setting.set('es_attachment_max_size_in_mb', 50)


Use the OTRS importer from the shell
------------------------------------

::

 rails> Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 rails> Setting.set('import_otrs_endpoint_key', 'xxx')
 rails> Setting.set('import_mode', true)
 rails> Import::OTRS.start


Enable proxy
------------

::

 rails> Setting.set('proxy', 'proxy.example.com:3128')
 rails> Setting.set('proxy_username', 'some user')
 rails> Setting.set('proxy_password', 'some pass')

