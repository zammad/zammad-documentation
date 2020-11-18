Set up Elasticsearch
********************

Zammad's search function is powered by Elasticsearch, and requires one of:

* Elasticsearch 5.5 (with the `mapper attachments plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/5.0/mapper-attachments.html>`_)
* Elasticsearch 5.6 or above (with the `ingest attachment plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/5.0/ingest-attachment.html>`_)

.. warning:: Versions below 5.5 may continue to work for the time being,
   but are officially deprecated. Support will be dropped in upcoming releases.

.. note:: This guide uses the ``zammad run`` command prefix in command line examples.
   This prefix is only applicable to package installations
   (*i.e.,* via apt/yum/zypper, or ``.deb``/``.rpm`` files).

   If you installed from source, be sure to omit this prefix
   and run the bare ``rails ...`` or ``rake ...`` commands instead.


Step 1: Installation
====================

.. tabs::

   .. tab:: Ubuntu

      ::

         $ apt-get install apt-transport-https sudo wget
         $ echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
         $ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
         $ apt-get update
         $ apt-get install elasticsearch
         $ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: Debian

      ::

         $ apt-get install apt-transport-https sudo wget
         $ echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
         $ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
         $ apt-get update
         $ apt-get install elasticsearch
         $ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: CentOS

      ::

         $ rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
         $ echo "[elasticsearch-7.x]
         name=Elasticsearch repository for 7.x packages
         baseurl=https://artifacts.elastic.co/packages/7.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=1
         autorefresh=1
         type=rpm-md"| sudo tee /etc/yum.repos.d/elasticsearch-7.x.repo
         $ sudo yum install -y elasticsearch
         $ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: OpenSUSE

      ::

         $ rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
         $ echo "[elasticsearch-7.x]
         name=Elasticsearch repository for 7.x packages
         baseurl=https://artifacts.elastic.co/packages/7.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=1
         autorefresh=1
         type=rpm-md"| sudo tee /etc/zypp/repos.d/elasticsearch-7.x.repo
         $ sudo zypper install elasticsearch
         $ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: Direct Download

      Find the latest release on the `downloads page <https://www.elastic.co/downloads/elasticsearch>`_,
      or see the `installation guide <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html>`_
      for in-depth instructions. 
      Ensure to also install the fitting (and mandatory!) attachment plugin for elasticsearch.

      .. code-block:: sh

         # Install the attachment plugin
         $ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment  # for 5.6+
         $ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-attachments # for 5.5

         # Increase the virtual memory map limit
         $ sudo sysctl -w vm.max_map_count=262144

After you installed Elasticsearch and its attachment plugin, ensure to enable it by default and start it.

.. code-block:: sh
   
   $ systemctl start elasticsearch
   $ systemctl enable elasticsearch

.. note:: 🐋 **Docker installations on macOS/Windows:**

   Setting the ``vm.max_map_count`` kernel parameter requires 
   `additional steps <https://www.elastic.co/guide/en/elasticsearch/reference/master/docker.html#_set_vm_max_map_count_to_at_least_262144s>`_.

Step 2: Suggested Configuration
===============================

We use the following settings to optimize the performance of our Elasticsearch servers. Your mileage may vary.

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

.. note:: For more information on the ``indices.query.bool.max_clause_count`` setting,
   see the `Elasticsearch 6.6 release notes <https://www.elastic.co/guide/en/elasticsearch/reference/6.8/breaking-changes-6.6.html#_literal_query_string_literal_literal_multi_match_literal_and_literal_simple_query_string_literal_query>`_.

Step 3: Connect Zammad
======================

.. hint:: **🤓 Before proceeding here...**

   Make sure to install Zammad before running below commands, as this will fail other wise.

      * install from :doc:`package <package>`
      * install from :doc:`source <source>`

.. code-block:: sh

   # Set the Elasticsearch server address
   $ zammad run rails r "Setting.set('es_url', 'http://localhost:9200')"

   # Build the search index
   $ zammad run rake searchindex:rebuild

Optional settings
-----------------

.. tabs::

   .. tab:: Authentication

      .. code-block:: sh

         # HTTP Basic
         $ zammad run rails r "Setting.set('es_user', '<username>')"
         $ zammad run rails r "Setting.set('es_password', '<password>')"

      .. hint:: 🤔 **How do I set up authentication on my Elasticsearch server?**

         For HTTP Basic auth, try `this nginx reverse proxy config <https://github.com/zammad/zammad/blob/develop/contrib/nginx/elasticsearch.conf>`_.

         Elasticsearch also supports authentication via its `X-Pack paid subscription service <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-xpack.html>`_
         Consult the official Elasticsearch guides for more details.

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
         $ zammad run rails r "Setting.set('es_attachment_ignore', [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )"

         # Files larger than this size (in MB) will not be indexed
         $ zammad run rails r "Setting.set('es_attachment_max_size_in_mb', 50)"

Appendix
========

.. toctree::
   :maxdepth: 0
   :titlesonly:

   elasticsearch/indexed-attributes
