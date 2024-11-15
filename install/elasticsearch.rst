Set Up Elasticsearch
====================

Zammad's search function can be powered by Elasticsearch (which is **highly
recommended**).

If these manual steps aren't what you are looking for, consider a `hosted Zammad
setup <https://zammad.com/en/pricing>`_ or :doc:`deploy Zammad via Docker </install/docker-compose>`.

.. note:: Some steps may be required depending on your Elasticsearch version and
   configuration. See remarks in the configuration steps below.

Step 1: Installation
--------------------

Elasticsearch offers two versions. Currently, the versions 7 and 8
are maintained. For installation instructions, you should first and foremost
follow
`Elastic's installation documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html#elasticsearch-install-packages>`_.
Use the dropdown in the top left corner to choose which version you want to
install.

However, if you want go with Elasticsearch 7 (which is slightly easier to
install), you can find the consolidated installation steps below.
Be aware that the maintenance of version 7 might be stopped earlier than for
version 8, which also comes with some additional security features.

.. hint:: If you are installing Elasticsearch 8 and want to follow our
   standard configuration in step 2, make sure to copy/save the password which
   is shown while installing Elasticsearch.

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
      (and mandatory!) attachment plugin for elasticsearch, if installing
      version 7.

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

Step 2: Configuration
---------------------

Install ingest-plugin (only for Elasticsearch <= 7)
   .. code-block:: sh

      $ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

Increase virtual memory map limit
   .. code-block:: sh

      $ sudo sysctl -w vm.max_map_count=262144

Adjust ``/etc/elasticsearch/elasticsearch.yml``
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

Enable and start Elasticsearch
   .. code-block:: sh

      $ systemctl start elasticsearch
      $ systemctl enable elasticsearch

.. _configure_zammad_with_elasticsearch:

Step 3: Connecting Zammad with Elasticsearch
--------------------------------------------

Before proceeding here, make sure to install Zammad before running below
commands, as this will fail otherwise.

* Install from :doc:`package <package>`
* Install from :doc:`source <source>`

.. note::
   This guide uses the ``zammad run`` command prefix in command line examples.
   This prefix is only applicable to package installations.
   If you installed from source, be sure to omit this prefix
   and run the bare ``rails ...`` or ``rake ...`` commands instead.

Elasticsearch URL
   .. code-block:: sh

      # Set the Elasticsearch server address; adapt it to your scenario.

      # Elasticsearch 7:
      $ sudo zammad run rails r "Setting.set('es_url', 'http://localhost:9200')"

      # Elasticsearch 8:
      $ sudo zammad run rails r "Setting.set('es_url', 'https://localhost:9200')"


Elasticsearch user and password (only for Elasticsearch >= 8)
   Now you need your password which was shown to you while installing
   Elasticsearch.

   .. code-block:: sh

      # Set Elasticsearch user and password
      $ zammad run rails r "Setting.set('es_user', 'elastic')"
      $ zammad run rails r "Setting.set('es_password', '<password>')"

Add certificate to Zammad (only for Elasticsearch >= 8)
   Show and copy the auto-generated certificate from Elasticsearch and add it
   to Zammad. Make sure to copy/paste the delimiters
   (e.g. ``-----BEGIN CERTIFICATE-----``) too.

   .. code-block:: sh

      $ sudo cat /etc/elasticsearch/certs/http_ca.crt

   Go to the admin panel of Zammad and add your copied certificate under
   :admin-docs:`SSL Certificates </settings/security/ssl-certificates.html>`.

   .. figure:: /images/install/elasticsearch/admin-certificate-management.png
      :alt: Screenshot shows certificate management in Zammad's admin panel
      :align: center

Build/rebuild the searchindex
   .. code-block:: sh

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
