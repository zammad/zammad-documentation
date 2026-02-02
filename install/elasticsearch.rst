Install Elasticsearch
=====================

This guide shows a simple standard installation of Elasticsearch 8. The
intention is to get you up and running quickly. However, in case you
need a more advanced configuration or face any issues, have a look at
the `official Elasticsearch installation
documentation <https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch>`__.
Adapt it wherever needed if your use-case differs.

Installation
------------

Download and Add the Public Signing Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tabs::

   .. group-tab:: Ubuntu / Debian

      Install required tools:

      .. code-block:: console

         $ sudo apt-get install apt-transport-https

      Add repo key:

      .. code-block:: console

         $ curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
           gpg --dearmor | sudo tee /usr/share/keyrings/elasticsearch-keyring.gpg \
           && sudo chmod 644 /usr/share/keyrings/elasticsearch-keyring.gpg

   .. group-tab:: OpenSUSE / SLES

      .. code-block:: console

         $ rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

   .. group-tab:: CentOS / RHEL

      .. code-block:: console

         $ rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch


Add the Repository
^^^^^^^^^^^^^^^^^^

.. tabs::

   .. group-tab:: Ubuntu / Debian

      .. code-block:: console

         $ echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

   .. group-tab:: OpenSUSE / SLES

      Create the file ``/etc/zypp/repos.d/elasticsearch.repo`` and add:

      .. code-block:: text

         [elasticsearch]
         name=Elasticsearch repository for 8.x packages
         baseurl=https://artifacts.elastic.co/packages/8.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=0
         autorefresh=1
         type=rpm-md

   .. group-tab:: CentOS / RHEL

      Create the file ``/etc/yum.repos.d/elasticsearch.repo`` and add:

      .. code-block:: text

         [elasticsearch]
         name=Elasticsearch repository for 8.x packages
         baseurl=https://artifacts.elastic.co/packages/8.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=0
         type=rpm-md

Install Elasticsearch
^^^^^^^^^^^^^^^^^^^^^

.. tabs::

   .. group-tab:: Ubuntu / Debian

      .. code-block:: console

         $ sudo apt-get update && sudo apt-get install elasticsearch

   .. group-tab:: OpenSUSE / SLES

      .. code-block:: console

         $ sudo zypper modifyrepo --enable elasticsearch && \
           sudo zypper install elasticsearch; \
           sudo zypper modifyrepo --disable elasticsearch

   .. group-tab:: CentOS / RHEL

      CentOS and RHEL 7 or earlier:

      .. code-block:: console

         $ sudo yum install --enablerepo=elasticsearch elasticsearch

      RHEL 8 and later:

      .. code-block:: console

         $ sudo dnf install --enablerepo=elasticsearch elasticsearch

.. tip::

   Make sure to check the output and to copy the password of the
   built-in superuser. Otherwise, you have to recreate it by running
   ``/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic``.

Step 2: Configuration
---------------------

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
   Set the Elasticsearch server address; adapt it to your scenario:

   .. code-block:: sh

      $ sudo zammad run rails r "Setting.set('es_url', 'https://localhost:9200')"


Elasticsearch user and password
   Now you need your password which was shown to you while installing
   Elasticsearch.

   .. code-block:: sh

      # Set Elasticsearch user and password
      $ zammad run rails r "Setting.set('es_user', 'elastic')"
      $ zammad run rails r "Setting.set('es_password', '<password>')"

Add certificate to Zammad
   Add it via **Rails console**:
      In case you are installing a new Zammad and didn't run through the
      getting started wizard already, add the certificate via console:

      .. code-block:: console

         $ sudo cat /etc/elasticsearch/certs/http_ca.crt | zammad run rails r 'SSLCertificate.create!(certificate: STDIN.read)'

   Add it via **UI**:
      In case you already have a running and configured Zammad, you can add the
      certificate in Zammad's
      :admin-docs:`admin settings </settings/security/ssl-certificates.html>`
      (*Settings > Security > SSL Certificates*) as an alternative.
      To show and copy the auto-generated certificate from Elasticsearch, run:

      .. code-block:: console

         $ sudo cat /etc/elasticsearch/certs/http_ca.crt

      To add it in Zammad, either upload the certificate file or paste the
      content in the dialog. Make sure to copy/paste the delimiters
      (e.g. ``-----BEGIN CERTIFICATE-----``) too.

   In any case, you can find the certificate in the UI. This looks like
   this:

   .. figure:: /images/install/elasticsearch/admin-certificate-management.png
      :alt: Screenshot shows certificate management in Zammad's admin panel
      :align: center

.. _es-rebuild-searchindex:

Build/rebuild the searchindex
   .. hint::
      - The rebuild may take many hours or even days, if a lot of data is
        already present in a productive environment. However, you can safely
        run this during operating times without the risk of loosing data. As a
        downside, it could lead to reduced performance and that some data may
        not be shown in search results.
      - Consider specifying a number of CPU cores to be used for the rebuild
        (see example below).

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
