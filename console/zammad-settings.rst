Getting and Updating Zammad-Settings
************************************

.. Note:: Please note that this is not a full setting list, if you're missing settings, feel free to ask over at our `Community <https://community.zammad.org>`_.


Send all outgoing E-Mails to a BCC-Mailbox
------------------------------------------

::
 
 Setting.set('system_bcc', 'alias@domain.tld')

 
::
 
 Setting.get('system_bcc')


Get ticket_hook setting
-----------------------

::

 Setting.get('ticket_hook')


Get fqdn setting
----------------

::

 Setting.get('fqdn')


Find storage_provide setting
----------------------------

::

 Setting.find_by(name: 'storage_provider')


Set storage_rpovider Setting
----------------------------

::

 Setting.set('storage_provider', 'DB')


Configuring Elasticsearch
-------------------------

::

 Setting.set('es_url', 'http://127.0.0.1:9200')
 Setting.set('es_user', 'elasticsearch')
 Setting.set('es_password', 'zammad')
 Setting.set('es_index', Socket.gethostname + '_zammad')
 Setting.set('es_attachment_ignore', [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )
 Setting.set('es_attachment_max_size_in_mb', 50)


Use the OTRS importer from the shell
------------------------------------

::

 Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 Setting.set('import_otrs_endpoint_key', 'xxx')
 Setting.set('import_mode', true)
 Import::OTRS.start


Enable proxy
------------

::

 Setting.set('proxy', 'proxy.example.com:3128')
 Setting.set('proxy_username', 'some user')
 Setting.set('proxy_password', 'some pass')

