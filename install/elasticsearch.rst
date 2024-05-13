Set up Elasticsearch
********************

Zammad's search function is powered by Elasticsearch, and requires the
`ingest attachment plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/current/ingest-attachment.html>`_.

This guide uses the ``zammad run`` command prefix in command line examples.
This prefix is only applicable to package installations
(*i.e.,* via apt/yum/zypper, or ``.deb``/``.rpm`` files).

If you installed from source, be sure to omit this prefix
and run the bare ``rails ...`` or ``rake ...`` commands instead.

Step 1: Installation
====================

Starting with Zammad 4.0, our packages allow you to decide whether to use
``elasticsearch`` or ``elasticsearch-oss``.

``elasticsearch-oss`` users please use below "direct download" tab for
further installation steps.

.. warning::

   Above does not apply to CentOS because of compatibility reasons.

.. tabs::

   .. tab:: Ubuntu

      ::

         $ apt install apt-transport-https sudo wget curl gnupg
         $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/elasticsearch.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main"| \
           tee -a /etc/apt/sources.list.d/elastic-7.x.list > /dev/null
         $ curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
           gpg --dearmor | tee /etc/apt/trusted.gpg.d/elasticsearch.gpg> /dev/null
         $ apt update
         $ apt install elasticsearch
         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: Debian

      ::

         $ apt install apt-transport-https sudo wget curl gnupg
         $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/elasticsearch.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main"| \
           tee -a /etc/apt/sources.list.d/elastic-7.x.list > /dev/null
         $ curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
           gpg --dearmor | tee /etc/apt/trusted.gpg.d/elasticsearch.gpg> /dev/null
         $ apt update
         $ apt install elasticsearch
         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

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
         type=rpm-md"| tee /etc/yum.repos.d/elasticsearch-7.x.repo
         $ yum install -y elasticsearch
         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

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
         type=rpm-md"| tee /etc/zypp/repos.d/elasticsearch-7.x.repo
         $ zypper install elasticsearch
         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: Direct Download

      Find the latest release on the
      `downloads page <https://www.elastic.co/downloads/elasticsearch>`_,
      or see the
      `installation guide <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html>`_
      for in-depth instructions. Ensure to also install the fitting
      (and mandatory!) attachment plugin for elasticsearch.

      If you prefer the Open Source version of Elasticsearch, please use the
      `Elasticsearch-OSS <https://www.elastic.co/downloads/past-releases#elasticsearch-oss>`_
      download page.

      .. code-block:: sh

         # Install the attachment plugin
         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

         # Increase the virtual memory map limit
         $ sysctl -w vm.max_map_count=262144

After you installed Elasticsearch and its attachment plugin,
ensure to enable it by default and start it.

.. code-block:: sh

   $ systemctl start elasticsearch
   $ systemctl enable elasticsearch

.. note:: 🐋 **Docker installations on macOS/Windows:**

   Setting the ``vm.max_map_count`` kernel parameter requires
   `additional steps <https://www.elastic.co/guide/en/elasticsearch/reference/master/docker.html#_set_vm_max_map_count_to_at_least_262144s>`_.

Step 2: Suggested Configuration
===============================

We use the following settings to optimize the performance of our Elasticsearch
servers. Your mileage may vary.

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

.. _configure_zammad_with_elasticsearch:

Step 3: Connect Zammad
======================

Before proceeding here, make sure to install Zammad before running below
commands, as this will fail otherwise.

   * install from :doc:`package <package>`
   * install from :doc:`source <source>`

.. code-block:: sh

   # Set the Elasticsearch server address
   $ zammad run rails r "Setting.set('es_url', 'http://localhost:9200')"

   # Build the search index
   $ zammad run rake zammad:searchindex:rebuild

   # Optionally, you can specify a number of CPU cores which are used for
   # rebuilding the searchindex, as in the following example with 8 cores:
   $ zammad run rake zammad:searchindex:rebuild[8]

Starting with Elasticsearch 8+, you need to use a HTTPS URL in
'es_url' as 'https://localhost:9200' and configure an
authentication (see HTTP Basic below).


Optional settings
-----------------

.. tabs::

   .. tab:: Authentication

      .. code-block:: sh

         # HTTP Basic
         $ zammad run rails r "Setting.set('es_user', '<username>')"
         $ zammad run rails r "Setting.set('es_password', '<password>')"

      .. hint:: 🤔 **How do I set up authentication on my Elasticsearch server?**

         Elasticsearch provides many different authentication methods.
         Some of them may require paid X-Pack, please check the
         `elastic documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setting-up-authentication.html>`_
         for more information.

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

      .. hint:: 🤔 **But how to handle an Elasticsearch server with custom
         certificates?**

         You can import custom certificates and custom CA certificates to
         Zammad. Please have a look
         :admin-docs:`in the admin documentation </settings/security/ssl-certificates.html>`.

Appendix
========

.. toctree::
   :maxdepth: 0
   :titlesonly:

   elasticsearch/indexed-attributes
   elasticsearch/troubleshooting
