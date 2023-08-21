Docker Compose Environment Variables
************************************

Zammad's Docker Compose supports several environment variables that are not
set by default. The best way to provide these is within the file ``.env``.

In case our default ``docker-compose.yml`` is not good enough, please use
``docker-compose.override.yml`` to provide own changes.

.. note::

   Unless stated otherwise, below environment variables count for the whole
   Zammad stack and not single containers. Below grouping is to help you find
   them better, but do not reflect their container.

Docker Compose
--------------
.. list-table::
   :widths: 28 20 26 26
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
     - Additional Info
   * - RESTART
     - ``always``
     - By default containers will be restarted in case they stopped for whatever reason.
     -
   * - VERSION
     -
     - This variables contains the version tag. Example: ``3.6.0-20``
     - We update this string from time to time, Docker Hub may contain more current tags to the moment you're pulling.

Zammad
------
.. list-table::
   :widths: 28 20 26 26
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
     - Additional Info
   * - AUTOWIZARD_JSON
     - ``''``
     - This variable allows you to provide initial configuration data for your instance. Autowizard JSON is out of scope of this documentation, however `this example file`_ should help.
     - .. include:: /install/docker-compose/init-specific.include.rst
   * - ZAMMAD_WEB_CONCURRENCY
     - ``(unset)``
     - Allows spawning ``n`` workers to allow more simultaneous connections for Zammads web UI. Please also note :doc:`/appendix/configure-env-vars` in this regard.
     - .. tip:: This variable is specific to the ``railsserver`` container.
   * - | ZAMMAD_SESSION_JOBS
       | _CONCURRENT
     - ``(unset)``
     - Allows spawning ``n`` session job workers to release pressure from Zammads background worker. Please also note :doc:`/appendix/configure-env-vars` in this regard.
     - .. include:: /install/docker-compose/scheduler-specific.include.rst
   * - | ZAMMAD_PROCESS_SCHEDULED
       | _JOBS_WORKERS
     - ``(unset)``
     - Allows spawning ``1`` independent scheduled job worker to release pressure from Zammads background worker. Please also note :doc:`/appendix/configure-env-vars` in this regard.
     - .. Tip:: This variable is specific to the ``scheduler`` container.
   * - | ZAMMAD_PROCESS_DELAYED
       | _JOBS_WORKERS
     - ``(unset)``
     - Allows spawning ``n`` delayed job workers to release pressure from Zammads background worker. Please also note :doc:`/appendix/configure-env-vars` in this regard.
     - .. Tip:: This variable is specific to the ``scheduler`` container.
   * - RAILS_TRUSTED_PROXIES
     - ``['127.0.0.1', '::1']``
     - By default Zammad trusts localhost proxies only.
     - .. Tip:: This variable is specific to the ``init`` container.
       .. danger:: **⚠ Only change this option if you know what you're doing! ⚠**

.. _this example file:
   https://github.com/zammad/zammad/blob/stable/contrib/auto_wizard_example.json


Elasticsearch
-------------
.. list-table::
   :widths: 28 20 26 26
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
     - Additional Info
   * - ELASTICSEARCH_ENABLED
     - ``true``
     - Setting this variable to false will allow you to run your Zammad without Elasticsearch. Please note that we strongly advise **against** doing so.
     - .. include:: /install/docker-compose/init-specific.include.rst
   * - ELASTICSEARCH_HOST
     - ``zammad-elasticsearch``
     - Provide a host name or address to your external Elasticsearch cluster.
     - .. include:: /install/docker-compose/init-specific.include.rst
   * - ELASTICSEARCH_PORT
     - ``9200``
     - Provide a different port for Elasticsearch if needed.
     - .. include:: /install/docker-compose/init-specific.include.rst
   * - ELASTICSEARCH_SCHEMA
     - ``http``
     - By default Elasticsearch is reachable via HTTP.
     - .. include:: /install/docker-compose/init-specific.include.rst
   * - ELASTICSEARCH_NAMESPACE
     - ``zammad``
     - With this name space all Zammad related indexes will be created. Change this if you're using external clusters.
     - .. include:: /install/docker-compose/init-specific.include.rst
   * - ELASTICSEARCH_REINDEX
     - ``true``
     - By default the docker-compose will *always re-index* upon a restart. On big installations this may be troublesome.
     - .. warning:: Disabling this setting requires you to re-index your search index manually whenever that's needed by upgrading to a new Zammad version!
       .. include:: /install/docker-compose/init-specific.include.rst
   * - ELASTICSEARCH_SSL_VERIFY
     - ``true``
     - Allows you to let the compose scripts ignore self signed SSL certificates for your Elasticsearch installation if needed.
     - .. include:: /install/docker-compose/init-specific.include.rst

Memcached
---------
.. list-table::
   :widths: 28 20 26 26
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
     - Additional Info
   * - MEMCACHE_SERVERS
     - ``zammad-memcached:11211``
     - Provide your own Memcached instance if you already have one existing.
     - .. warning:: Was ``MEMCACHED_HOST`` before 5.0.x!

Redis
-----
.. list-table::
   :widths: 28 20 26 26
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
     - Additional Info
   * - REDIS_URL
     - ``redis://zammad-redis:6379``
     - Provide your own Redis instance if you already have one.
     - .. warning:: This method currently does not allow authentication.

NGINX
-----
.. list-table::
   :widths: 28 20 26 26
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
     - Additional Info
   * - NGINX_PORT
     - ``8080``
     - The port Nginx will listen on.
     - .. include:: /install/docker-compose/nginx-specific.include.rst
   * - NGINX_SERVER_NAME
     - ``_``
     - By default the Nginx container of Zammad will respond to all request. You can provide your IP / FQDN if you want to.
     - .. include:: /install/docker-compose/nginx-specific.include.rst
   * - NGINX_SERVER_SCHEME
     - ``\$scheme``
     - If the Nginx container for Zammad **is not** the upstream server (aka you're using another proxy in front of nginx) ``$scheme`` may be wrong. You can set the correct scheme ``http`` or ``https`` if needed.
     - .. include:: /install/docker-compose/nginx-specific.include.rst
   * - ZAMMAD_RAILSSERVER_HOST
     - ``zammad-railsserver``
     - Host name of the rails server container.
     -
   * - ZAMMAD_RAILSSERVER_PORT
     - ``3000``
     - Port of Zammads rails server.
     - .. include:: /install/docker-compose/include-env-var-note.rst
   * - ZAMMAD_WEBSOCKET_HOST
     - ``zammad-websocket``
     - Host name of Zammads websocket server.
     - .. include:: /install/docker-compose/nginx-specific.include.rst
   * - ZAMMAD_WEBSOCKET_PORT
     - ``6042``
     - Port of Zammads websocket server.
     - .. include:: /install/docker-compose/include-env-var-note.rst

.. include:: /getting-started/include-csrf-hints.rst

PostgreSQL
----------
.. list-table::
   :widths: 28 20 26 26
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
     - Additional Info
   * - POSTGRESQL_HOST
     - ``zammad-postgresql``
     - Host name of your PostgreSQL server. Use your own if you already have one.
     -
   * - POSTGRESQL_PORT
     - ``5432``
     - Adjust the Port of your PostgreSQL server.
     -
   * - POSTGRESQL_USER
     - ``zammad``
     - The database user for Zammad.
     -
   * - POSTGRESQL_PASS
     - ``zammad``
     - The password of Zammads database user.
     -
   * - POSTGRESQL_DB
     - ``zammad_production``
     - Zammads database to use.
     -
   * - POSTGRESQL_DB_CREATE
     - ``true``
     - By default we will create the required database.
     - .. note:: On own database servers this setting might be troublesome.
       .. include:: /install/docker-compose/init-specific.include.rst
   * - RSYNC_ADDITIONAL_PARAMS
     - ``--no-perms --no-owner``
     - By default the compose will copy data without permissions and owners. This may not fit for your storage driver.
     - .. include:: /install/docker-compose/init-specific.include.rst
