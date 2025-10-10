Install Elasticsearch 7
=======================

This guide shows a simple standard installation of Elasticsearch 7. The
intention is to get you up and running quickly. However, in case you
need a more advanced configuration or face any issues, have a look at
the `official Elasticsearch installation
documentation <https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch>`__.
Adapt it wherever needed in case your use-case differs.

You can find the consolidated installation steps below.
Be aware that the maintenance of version 7 might be stopped earlier than for
later versions, which also come with some additional security features.

Installation
------------

.. tabs::

   .. tab:: Ubuntu/Debian

      .. code-block:: console

         $ sudo apt install apt-transport-https sudo wget curl gnupg

      .. code-block:: console

         $ curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
           gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/elasticsearch.gpg> /dev/null

      .. tabs::

         .. tab:: Deb822 format

            In this tab, the repository is added by using the
            `deb822 format <https://repolib.readthedocs.io/en/latest/deb822-format.html>`_.
            If you run a distribution which doesn't support it, use the legacy
            format instead.

            .. code-block:: console

               $ printf "Types: deb
               URIs: https://artifacts.elastic.co/packages/7.x/apt
               Suites: stable
               Components: main
               Signed-By: /etc/apt/trusted.gpg.d/elasticsearch.gpg" | \
               sudo tee /etc/apt/sources.list.d/elastic-7.x.sources > /dev/null

         .. tab:: Legacy format

            .. code-block:: console

               $ echo "deb [signed-by=/etc/apt/trusted.gpg.d/elasticsearch.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main"| \
               sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list > /dev/null

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install elasticsearch

      .. code-block:: console

         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: CentOS

      .. code-block:: console

         $ sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

      .. code-block:: console

         $ echo "[elasticsearch-7.x]
         name=Elasticsearch repository for 7.x packages
         baseurl=https://artifacts.elastic.co/packages/7.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=1
         autorefresh=1
         type=rpm-md"| sudo tee /etc/yum.repos.d/elasticsearch-7.x.repo

      .. code-block:: console

         $ sudo yum install -y elasticsearch

      .. code-block:: console

         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: OpenSUSE

      .. code-block:: console

         $ sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

      .. code-block:: console

         $ echo "[elasticsearch-7.x]
         name=Elasticsearch repository for 7.x packages
         baseurl=https://artifacts.elastic.co/packages/7.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=1
         autorefresh=1
         type=rpm-md"| sudo tee /etc/zypp/repos.d/elasticsearch-7.x.repo

      .. code-block:: console

         $ sudo zypper install elasticsearch

      .. code-block:: console

         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   .. tab:: Direct Download

      Find the latest release on the
      `downloads page <https://www.elastic.co/downloads/elasticsearch>`_,
      or see the
      `installation guide <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html>`_
      for in-depth instructions. Ensure to also install the fitting
      (and mandatory!) attachment plugin for Elasticsearch, if installing
      version 7.

      Install the attachment plugin:

      .. code-block:: console

         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

      Increase the virtual memory map limit:

      .. code-block:: console

         $ sudo sysctl -w vm.max_map_count=262144

After you installed Elasticsearch and its attachment plugin,
ensure to enable it by default and start it.

.. code-block:: console

   $ sudo systemctl start elasticsearch

.. code-block:: console

   $ sudo systemctl enable elasticsearch

Configuration
-------------

Install ingest-plugin (only for Elasticsearch <= 7)
   .. code-block:: console

      $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

Increase virtual memory map limit
   .. code-block:: console

      $ sudo sysctl -w vm.max_map_count=262144

Adjust ``/etc/elasticsearch/elasticsearch.yml``
   We use the following settings to optimize the performance of our Elasticsearch
   servers. You may want to append that to your ``elasticsearch.yml`` as a useful
   basic configuration.

   .. code-block:: text

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

Enable and start Elasticsearch
   .. code-block:: console

      $ sudo systemctl start elasticsearch

   .. code-block:: console

      $ sudo systemctl enable elasticsearch