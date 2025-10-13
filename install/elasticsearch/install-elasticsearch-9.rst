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

   .. tab:: Ubuntu/Debian

      Install required tools:

      .. code-block:: console

         $ sudo apt-get install apt-transport-https

      Add repo key:

      .. code-block:: console

         $ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

   .. tab:: OpenSUSE/SLES

      .. code-block:: console

         $ rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

   .. tab:: CentOS/RHEL

      .. code-block:: console

         $ rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch


Add the Repository
^^^^^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Ubuntu/Debian

      .. code-block:: console

         $ echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list

   .. tab:: OpenSUSE/SLES

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

   .. tab:: CentOS/RHEL

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

   .. tab:: Ubuntu/Debian

      .. code-block:: console

         $ sudo apt-get update && sudo apt-get install elasticsearch

   .. tab:: OpenSUSE/SLES

      .. code-block:: console

         $ sudo zypper modifyrepo --enable elasticsearch && \
           sudo zypper install elasticsearch; \
           sudo zypper modifyrepo --disable elasticsearch

   .. tab:: CentOS/RHEL

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

Configuration
-------------

Open ``/etc/elasticsearch/elasticsearch.yml`` and adjust/uncomment the
following values:

.. code-block:: yaml

   network.host: 0.0.0.0
   transport.host: 0.0.0.0

Optional to increase the maximum context size to index:

.. code-block:: yaml

   http.max_content_length: 400mb

Start and Enable Elasticsearch
------------------------------

.. code-block:: console

   $ sudo systemctl enable elasticsearch.service --now

Next Steps
----------

Go on with the :doc:`installation of Zammad <../package>`.
After the installation of Zammad is completed, you can :doc:`connect Zammad
with Elasticsearch <connect-configure-elasticsearch>`.
