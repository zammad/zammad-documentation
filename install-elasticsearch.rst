Set up Elasticsearch
********************

We use Elasticsearch for the awesome search in Zammad.

Install Elasticsearch and its Attachment plugin
===============================================

Install Elasticsearch 2.4 on your machine
-----------------------------------------

* https://www.elastic.co/downloads/elasticsearch (2.4.x)

Install the Attachment plugin
-----------------------------

::

 cd /usr/share/elasticsearch
 bin/plugin install mapper-attachments


Start Elasticsearch
-------------------

CentOS 7:
+++++++++

::

 systemctl start elasticsearch
 systemctl enable elasticsearch

CentOS 6:
+++++++++

::

 service elasticsearch start
 chkconfig zammad on


Configure Zammad to work with Elasticsearch
===========================================

::

 su - zammad
 rails r "Setting.set('es_url', 'http://127.0.0.1:9200')"

In certain cases you can also use the following settings **(by default not needed)**

Elasticsearch with HTTP basic auth
----------------------------------

::

 rails r "Setting.set('es_user', 'elasticsearch')"
 rails r "Setting.set('es_password', 'zammad')"

Extra Elasticsearch index name space (optional)
----------------------------------------------

::

 rails r "Setting.set('es_index', Socket.gethostname + '_zammad')"

Ignore certain file extentions for indexing (optional)
------------------------------------------------------

::

 rails r "Setting.set('es_attachment_ignore', [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )"

Maximum attachment size which is used for indexing, default is 50 MB (optional)
-------------------------------------------------------------------------------

::

 rails r "Setting.set('es_attachment_max_size_in_mb', 50)"


Create Elasticsearch index
==========================

After you have configured Zammad for using Elasticsearch, you need to rebuild the index with the following command:

::

 rake searchindex:rebuild # drop/create/reload


Using Elasticsearch on another server
=====================================

Elasticsearch can also be installed on another server but you have to know that this is insecure out of the box because Elasticsearch has no authentication.
For this reason you should run elasticsearch on 127.0.0.1 and use a reverse proxy with authentification to access it from Zammad.
You can find an example config @ https://github.com/zammad/zammad/blob/develop/contrib/nginx/elasticsearch.conf


