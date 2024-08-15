Set Up Elasticsearch
====================

Zammad's search function can be powered by Elasticsearch (which is **highly
recommended**).

If these manual steps aren't what you are looking for, consider a `hosted Zammad
setup <https://zammad.com/en/pricing>`_ or :doc:`deploy Zammad via Docker </install/docker-compose>`.

Step 1: Installation
--------------------

Zammad allows you to use **elasticsearch** or **elasticsearch-oss**.
For installation instructions please follow
`Elastic's installation instructions <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html>`_.

Step 2: Configuration
---------------------

.. code-block:: sh

   # Install the ingest-attachment plugin manually, if running ES 7 or older
   $ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   # Increase the virtual memory map limit
   $ sudo sysctl -w vm.max_map_count=262144

We use the following settings to optimize the performance of our Elasticsearch
servers. You may want to append that to your ``elasticsearch.yml`` as a useful
basic configuration.

.. code-block:: sh

   # /etc/elasticsearch/elasticsearch.yml

   # Tickets above this size (articles + attachments + metadata)
   # may fail to be properly indexed (Default: 100mb).
   #
   # When Zammad sends tickets to Elasticsearch for indexing,
   # it bundles together all the data on each individual ticket
   # and issues a single HTTP request for it.
   # Payloads exceeding this threshold will be truncated.
   #
   # Performance may suffer if it is set too high.
   http.max_content_length: 400mb

   # Allows the engine to generate larger (more complex) search queries.
   # Elasticsearch will raise an error or deprecation notice if this value is too low,
   # but setting it too high can overload system resources (Default: 1024).
   #
   # Available in version 6.6+ only.
   indices.query.bool.max_clause_count: 2000

After installation and configuration, ensure to enable Elasticsearch
by default and start it:

.. code-block:: sh

   $ systemctl start elasticsearch
   $ systemctl enable elasticsearch

.. _configure_zammad_with_elasticsearch:

Step 3: Connect Zammad
----------------------

Before proceeding here, make sure to install Zammad before running below
commands, as this will fail otherwise.

* install from :doc:`package <package>`
* install from :doc:`source <source>`

.. note::
   This guide uses the ``zammad run`` command prefix in command line examples.
   This prefix is only applicable to package installations.
   If you installed from source, be sure to omit this prefix
   and run the bare ``rails ...`` or ``rake ...`` commands instead.

.. code-block:: sh

   # Set the Elasticsearch server address
   # It has to be https starting with ES8
   $ sudo zammad run rails r "Setting.set('es_url', 'http://localhost:9200')"

   # Build the search index
   $ sudo zammad run rake zammad:searchindex:rebuild

   # Optionally, you can specify a number of CPU cores which are used for
   # rebuilding the searchindex, as in the following example with 8 cores:
   $ sudo zammad run rake zammad:searchindex:rebuild[8]

Optional settings
-----------------

We collected some useful settings you may want to apply. For further
information please have a look at
`Elastic's documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`_.

.. tabs::

   .. tab:: Authentication

      .. code-block:: sh

         # HTTP Basic
         $ zammad run rails r "Setting.set('es_user', '<username>')"
         $ zammad run rails r "Setting.set('es_password', '<password>')"

   .. tab:: Index namespacing

      Useful when connecting multiple services or Zammad instances
      to a single Elasticsearch server (to prevent name collisions during indexing).

      .. code-block:: sh

         $ zammad run rails r "Setting.set('es_index', Socket.gethostname.downcase + '_zammad')"

   .. tab:: File-attachment indexing rules

      Zammad supports searching by the contents of file attachments,
      which means Elasticsearch has to index those, too.

      Limiting such indexing can help conserve system resources.

      .. code-block:: sh

         # Files with these extensions will not be indexed
         $ zammad run rails r "Setting.set('es_attachment_ignore',\
           [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )"

         # Files larger than this size (in MB) will not be indexed
         $ zammad run rails r "Setting.set('es_attachment_max_size_in_mb', 50)"

   .. tab:: Remote host

      Change your Elasticsearch URL if you have a separate Elasticsearch server.
      Default is ``localhost``.

      .. code-block:: sh

         $ zammad run rails r "Setting.set('es_url', 'https://example.com')"

   .. tab:: SSL Verification

      You can define if a SSL verification will be performed. Default is
      ``true``.

      .. code-block:: sh

         # Deactivating SSL verification is NOT recommended
         $ zammad run rails r "Setting.set('es_ssl_verify', false)"

      If you want to use custom certificates, you can find information about
      how to use them in Zammad
      :admin-docs:`here </settings/security/ssl-certificates.html>`.

Appendix
--------

.. toctree::
   :maxdepth: 0
   :titlesonly:

   elasticsearch/indexed-attributes
   elasticsearch/troubleshooting
