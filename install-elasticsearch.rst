.. _install_elasticsearch:

Set up Elasticsearch
********************

We use Elasticsearch for the awesome search in Zammad.

Currently we support:

* Elasticsearch 5.5.x with mapper-attachments plugin
* Elasticsearch 5.6.x, 6.x, 7.x with ingest-attachment plugin

.. warning:: Please note that we will be dropping Elasticsearch support prior 5.5.x on future releases.

This manual uses the ``zammad run`` command which is only available if you installed Zammad from one of our package repos.
If you're using a source code based install, simply leave that part away and just run ``rails ...`` or ``rake ...`` where ever neded.


Step 1: Installation
====================

:Direct Download:

   * Download and install via https://www.elastic.co/downloads/elasticsearch (5.6, 6.x or 7.x)
   * Install the Attachment plugin::

        sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

   * Setting vm.max_map_count for Elasticsearch::

        sysctl -w vm.max_map_count=262144

     .. tip:: On Mac OS you also have to do: https://www.elastic.co/guide/en/elasticsearch/reference/5.6/docker.html#docker-cli-run-prod-mode

   * Start elasticsearch

   The most current repository installation path can be found `here <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html>`_.

:CentOS 7:

   ::

      rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
      echo "[elasticsearch-7.x]
      name=Elasticsearch repository for 7.x packages
      baseurl=https://artifacts.elastic.co/packages/7.x/yum
      gpgcheck=1
      gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
      enabled=1
      autorefresh=1
      type=rpm-md"| sudo tee /etc/yum.repos.d/elasticsearch-7.x.repo
      yum install -y java-1.8.0-openjdk elasticsearch
      sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment
      systemctl start elasticsearch
      systemctl enable elasticsearch


:Debian 8:

   ::

      apt-get install apt-transport-https sudo wget
      echo "deb http://ftp.debian.org/debian jessie-backports main" | sudo tee -a /etc/apt/sources.list.d/debian-backports.list
      echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
      wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
      apt-get update
      apt-get install -t jessie-backports openjdk-8-jre
      apt-get install elasticsearch
      sudo /var/lib/dpkg/info/ca-certificates-java.postinst configure
      sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment
      systemctl restart elasticsearch
      systemctl enable elasticsearch


:Debian 9:

   ::

      apt-get install apt-transport-https sudo wget
      echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
      wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
      apt-get update
      apt-get install openjdk-8-jre elasticsearch
      sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment
      systemctl restart elasticsearch
      systemctl enable elasticsearch


:Ubuntu 16.04 & 18.04:

   ::

      apt-get install apt-transport-https sudo wget
      echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
      wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
      apt-get update
      apt-get install openjdk-8-jre elasticsearch
      sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment
      systemctl restart elasticsearch
      systemctl enable elasticsearch

Step 2: Suggested Configuration
===============================

.. note:: The we found the below settings to work good with Zammad. Please note that this is only suggestion that can affect your local environment.

To ensure an optimal performance of Zammad together with elasticsearch, you might want to increase the maximum possible
content length for http requests by adding the following to your ``/etc/elasticsearch/elasticsearch.yml``::

   http.max_content_length: 400mb

.. note:: The following step is only necessary starting with elasticsearch 7 and newer.


To enable Zammad to search for many values at the same time (to speed up your search), you'll also need to add the followingf option to your ``/etc/elasticsearch/elasticsearch.yml``::

   indices.query.bool.max_clause_count: 2000

Above setting is necessary, as the default value is ``1024`` which is too low.
elasticsearch 6.x will only throw a deprecation warning, so you might want to adjust it with above as well.

Step 3: Connect Zammad
======================

First of all we need to tell Zammad where it can find elasticsearch::

   zammad run rails r "Setting.set('es_url', 'http://localhost:9200')"

If you need to use authentication for your elasticsearch installation or specific indice namings, please take a look at :ref:`optional-settings`.

Create Elasticsearch index
--------------------------

After you have configured Zammad for using Elasticsearch, you need to rebuild the index with the following command::

   zammad run rake searchindex:rebuild

.. _optional-settings:

Optional settings
-----------------

:Elasticsearch with HTTP basic auth:

   If you're using another elasticsearch instance, you might need to authenticate against it.
   Below options help you with that::

      zammad run rails r "Setting.set('es_user', 'elasticsearch')"
      zammad run rails r "Setting.set('es_password', 'zammad')"


:Extra Elasticsearch index name space:

   If you're running several Zammad instances (or other services using ES) with a central elasticsearch server,
   you might want to specify which index Zammad should use::

      zammad run rails r "Setting.set('es_index', Socket.gethostname.downcase + '_zammad')"

:Ignore certain file extensions for indexing:

   Some attachments might be troublesome when indexing or simply not needed within the search index.
   You can tell Zammad to ignore those attachments by specifying their file extension so it won't post it to elasticsearch::

      zammad run rails r "Setting.set('es_attachment_ignore', [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )"

:Maximum attachment size which is used for indexing:

   .. note:: By default Zammad will limit indexing to attachments to 50 MB.

   Limiting the maximum size of attachments (for indexing) might be usefull, you can set it like so::

      zammad run rails r "Setting.set('es_attachment_max_size_in_mb', 50)"


:Using elasticsearch on another server:

   elasticsearch also allows you to use authentication via X-Pack to run it on another system as the one Zammad runs on.
   Please note that the configuration of this functionality is out of scope of this documentation.

   Elastic provides a great documentation on `how to set up X-Pack <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-xpack.html>`_.


Versions prior elasticsearch 6.3
--------------------------------

.. note:: Depending on the elasticsearch version it can provide authentication. There are also subscription based authentication features you can get from the elastic-team.

   `You can find an Nginx reverse proxy config here <https://github.com/zammad/zammad/blob/develop/contrib/nginx/elasticsearch.conf>`_

Appendix
========

.. toctree::
   :maxdepth: 0
   :titlesonly:

   elasticsearch/indexed-attributes

