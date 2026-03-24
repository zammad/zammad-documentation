Install Elasticsearch 9
=======================

This guide shows a simple standard installation of Elasticsearch 9. The
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

         $ sudo apt install apt-transport-https

   .. group-tab:: OpenSUSE / SLES

      .. code-block:: console

         $ sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

   .. group-tab:: CentOS / RHEL

      .. code-block:: console

         $ sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch


Add the Repository
^^^^^^^^^^^^^^^^^^

.. tabs::

   .. group-tab:: Ubuntu / Debian

      Add repo key:

      .. code-block:: console

         $ curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
           gpg --dearmor | sudo tee /usr/share/keyrings/elasticsearch-keyring.gpg \
           && sudo chmod 644 /usr/share/keyrings/elasticsearch-keyring.gpg

      Add repo:

      .. code-block:: console

         $ echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list

   .. group-tab:: OpenSUSE / SLES

      Create the file ``/etc/zypp/repos.d/elasticsearch.repo`` and add:

      .. code-block:: text

         [elasticsearch]
         name=Elasticsearch repository for 9.x packages
         baseurl=https://artifacts.elastic.co/packages/9.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=0
         autorefresh=1
         type=rpm-md

   .. group-tab:: CentOS / RHEL

      Create the file ``/etc/yum.repos.d/elasticsearch.repo`` and add:

      .. code-block:: text

         [elasticsearch]
         name=Elasticsearch repository for 9.x packages
         baseurl=https://artifacts.elastic.co/packages/9.x/yum
         gpgcheck=1
         gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
         enabled=0
         type=rpm-md

Install Elasticsearch
^^^^^^^^^^^^^^^^^^^^^

.. tabs::

   .. group-tab:: Ubuntu / Debian

      .. code-block:: console

         $ sudo apt update && sudo apt install elasticsearch

   .. group-tab:: OpenSUSE / SLES

      .. code-block:: console

         $ sudo zypper modifyrepo --enable elasticsearch && \
           sudo zypper install elasticsearch; \
           sudo zypper modifyrepo --disable elasticsearch

   .. group-tab:: CentOS / RHEL

      .. code-block:: console

         $ sudo dnf install --enablerepo=elasticsearch elasticsearch

.. tip::

   Make sure to check the output and to copy the password of the
   built-in superuser. Otherwise, you have to recreate it by running
   ``/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic``.

Configuration
-------------

Optionally, check and configure Elasticsearch's configuration file which you can
find under ``/etc/elasticsearch/elasticsearch.yml``.

We recommend to adjust the maximum context size which should get indexed
by Elasticsearch. Adjust it to a reasonable size like in the example:

.. code-block:: yaml

   http.max_content_length: 400mb

Additional configuration is out of scope of this documentation. In case your
scenario needs additional configuration, have a look at
`Elastic's configuration reference <https://www.elastic.co/docs/reference/elasticsearch/configuration-reference>`_.

Start and Enable Elasticsearch
------------------------------

.. code-block:: console

   $ sudo systemctl enable elasticsearch.service --now

Next Steps
----------

Go on with the :doc:`installation of Zammad <../package>`.
After the installation of Zammad is completed, you can :doc:`connect Zammad
with Elasticsearch <connect-configure-elasticsearch>`.
