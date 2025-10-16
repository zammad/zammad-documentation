Connect and Configure Elasticsearch
===================================

.. _configure_zammad_with_elasticsearch:

Connect Zammad with Elasticsearch
---------------------------------

Before proceeding here, make sure to install Zammad before running below
commands, as this will fail otherwise.

* Install from :doc:`package <../package>`
* Install with :doc:`Docker <../docker-compose>` (the default stack already includes Elasticsearch)

.. note::
   This guide uses the ``zammad run`` command prefix in command line examples.
   This prefix is only applicable to package installations.
   Check the :doc:`console guide </admin/console>` for more information.

Elasticsearch URL
   Set the Elasticsearch server address; adapt it to your scenario.

   Elasticsearch 7:

   .. code-block:: console

      $ zammad run rails r "Setting.set('es_url', 'http://localhost:9200')"

   Elasticsearch 8 and newer:

   .. code-block:: console

      $ zammad run rails r "Setting.set('es_url', 'https://localhost:9200')"


Elasticsearch user and password (Elasticsearch 8 and newer)
   Now you need your password which was shown during the installation.

   Set Elasticsearch user:

   .. code-block:: console

      $ zammad run rails r "Setting.set('es_user', 'elastic')"

   Set Elasticsearch password. Replace ``<password>`` with the one you got
   during the installation of Elasticsearch. In case you need to create a new
   password, run
   ``/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic``.

   .. code-block:: console

      $ zammad run rails r "Setting.set('es_password', '<password>')"

Add certificate to Zammad (Elasticsearch 8 and newer)
   Add it via **Rails console**:
      In case you are installing a new Zammad and didn't run through the
      getting started wizard already, add the certificate via console:

      .. code-block:: console

         $ sudo cat /etc/elasticsearch/certs/http_ca.crt | zammad run rails r "SSLCertificate.create!(certificate: STDIN.read)"

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

   Without specifying CPU cores:

   .. code-block:: console

      $ zammad run rake zammad:searchindex:rebuild

   Example with specifying 8 CPU cores:

   .. code-block:: console

      $ zammad run rake zammad:searchindex:rebuild[8]


Optional settings
-----------------

We collected some useful settings you may want to apply. For further
information please have a look at
`Elastic's documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`_.

.. tabs::

   .. tab:: Index namespacing

      Useful when connecting multiple services or Zammad instances
      to a single Elasticsearch server (to prevent name collisions during indexing).

      .. code-block:: console

         $ zammad run rails r "Setting.set('es_index', Socket.gethostname.downcase + '_zammad')"

   .. tab:: File-attachment indexing rules

      Zammad supports searching by the contents of file attachments, which means
      Elasticsearch has to index those, too. Limiting such indexing can help
      conserve system resources.

      Files with these extensions will not be indexed:

      .. code-block:: console

         $ zammad run rails r "Setting.set('es_attachment_ignore',\
           [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )"

      Files larger than this size (in MB) will not be indexed:

      .. code-block:: console

         $ zammad run rails r "Setting.set('es_attachment_max_size_in_mb', 50)"

   .. tab:: Remote host

      Change your Elasticsearch URL if you have a separate Elasticsearch server.
      Default is ``localhost``.

      .. code-block:: console

         $ zammad run rails r "Setting.set('es_url', 'https://example.com')"

   .. tab:: SSL Verification

      You can disable SSL verification, which is not recommended. Default is
      ``true``.

      .. code-block:: console

         $ zammad run rails r "Setting.set('es_ssl_verify', false)"

      If you want to use custom certificates, you can find information about
      how to use them in Zammad
      :admin-docs:`here </settings/security/ssl-certificates.html>`.

   .. tab:: Asciifold

      By default, the
      `Asciifold <https://www.elastic.co/docs/reference/text-analysis/analysis-asciifolding-tokenfilter>`_
      feature of Elasticsearch is enabled. This can be useful if you deal with
      text which includes diacritics and/or umlauts.

      In case you need a more exact search, you can turn it off:

      .. code-block:: console

         $ zammad run rails r "Setting.set('es_asciifolding', false)"

Appendix
--------

.. toctree::
   :maxdepth: 0
   :titlesonly:

   indexed-attributes
   troubleshooting
