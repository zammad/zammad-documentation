Docker Environment Variables
****************************

Find the available docker environment variables below with default values, if
applicable. You might also be interested in the
:doc:`environment variables documentation </appendix/configure-env-vars>`.

.. hint::

   If you want to use a ``.env`` file, you can use the provided ``.env.dist``
   file and copy it to ``.env``. That way it will be picked up by Docker-Compose
   automatically and not overwritten during updates.

Zammad
------
.. list-table::
   :widths: 28 20 52
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
   * - VERSION
     - (current stable version of Zammad)
     - Allows customization of the Zammad image tag. Example: ``6.3.1-54``.
       This default version may be increased when you update your Zammad docker stack.
       Please see the `example env template <https://github.com/zammad/zammad-docker-compose/blob/master/.env.dist>`_
       for more details on this variable.
   * - AUTOWIZARD_JSON
     - ``''``
     - This variable allows you to provide initial configuration data for your
       instance. Autowizard JSON is out of scope of this documentation, however
       `this example file`_ should help.
   * - ZAMMAD_HTTP_TYPE
     - ``(unset)``
     - Set the :admin-docs:`http type </settings/system/base.html>` for your
       instance.
   * - ZAMMAD_FQDN
     - ``(unset)``
     - Set the :admin-docs:`FQDN </settings/system/base.html>` for your instance.
   * - ZAMMAD_WEB_CONCURRENCY
     - ``(unset)``
     - Allows spawning ``n`` workers to allow more simultaneous connections for
       Zammad's web UI. See also: :doc:`/appendix/configure-env-vars`

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-railsserver's CPU setting should match the value from this variable.
   * - | ZAMMAD_PROCESS_SESSION
       | _JOBS_WORKERS
     - ``(unset)``
     - Allows spawning ``n`` independent session jobs workers to release
       pressure from Zammad's background worker. See also:
       :doc:`/appendix/configure-env-vars`.

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker settings variables.
   * - | ZAMMAD_PROCESS_SCHEDULED
       | _JOBS_WORKERS
     - ``(unset)``
     - Allows spawning ``1`` independent scheduled jobs worker to release
       pressure from Zammad's background worker. See also:
       :doc:`/appendix/configure-env-vars`.

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker settings variables.
   * - | ZAMMAD_PROCESS_DELAYED
       | _JOBS_WORKERS
     - ``(unset)``
     - Allows spawning ``n`` delayed jobs workers to release pressure from
       Zammad's background worker. See also: :doc:`/appendix/configure-env-vars`.


       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker settings variables.
   * - RAILS_TRUSTED_PROXIES
     - ``['127.0.0.1', '::1']``
     - By default Zammad trusts localhost proxies only.
   * - MEMCACHE_SERVERS
     - ``zammad-memcached:11211``
     - Provide your own Memcached instance to Zammad if you already have one.
   * - REDIS_URL
     - ``redis://zammad-redis:6379``
     - Provide your own Redis instance if you already have one. Please note
       that this method currently does not allow authentication.


.. _this example file:
   https://github.com/zammad/zammad/blob/stable/contrib/auto_wizard_example.json


Elasticsearch
-------------
.. list-table::
   :widths: 28 20 52
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
   * - ELASTICSEARCH_ENABLED
     - ``true``
     - Setting this variable to false will allow you to run your Zammad without
       Elasticsearch. Please note that we strongly advise **against** doing so.
   * - ELASTICSEARCH_HOST
     - ``zammad-elasticsearch``
     - Provide a host name or address to your external Elasticsearch cluster.
   * - ELASTICSEARCH_PORT
     - ``9200``
     - Provide a different port for Elasticsearch if needed.
   * - ELASTICSEARCH_SCHEMA
     - ``http``
     - By default Elasticsearch is reachable via HTTP.
   * - ELASTICSEARCH_USER
     - ``elastic``
     - Set a user to access the Elasticsearch index.
   * - ELASTICSEARCH_PASS
     - ``zammad``
     - Set a password for the Elasticsearch user.
   * - ELASTICSEARCH_NAMESPACE
     - ``zammad``
     - With this name space all Zammad related indexes will be created. Change
       this if you're using external clusters.
   * - ELASTICSEARCH_REINDEX
     - ``true``
     - By default the docker-compose will *always re-index* upon a restart.
       On big installations this may be troublesome.

       .. warning::
          Disabling this setting requires you to re-index your search
          index manually whenever that's needed by upgrading to a new Zammad
          version!
   * - ELASTICSEARCH_SSL_VERIFY
     - ``true``
     - Allows you to let the compose scripts ignore self signed SSL certificates
       for your Elasticsearch installation if needed.
   * - ELASTICSEARCH_HEAP_SIZE
     - ``(unset)``
     - Set the available memory for Elasticsearch.

PostgreSQL
----------
.. list-table::
   :widths: 28 20 52
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
   * - POSTGRESQL_HOST
     - ``zammad-postgresql``
     - Host name of your PostgreSQL server. Use your own if you already have one.
   * - POSTGRESQL_PORT
     - ``5432``
     - Adjust the Port of your PostgreSQL server.
   * - POSTGRESQL_USER
     - ``zammad``
     - The database user for Zammad.
   * - POSTGRESQL_PASS
     - ``zammad``
     - The password of Zammad's database user.
   * - POSTGRESQL_DB
     - ``zammad_production``
     - Zammad's database to use.
   * - POSTGRESQL_OPTIONS
     - ``?pool=50``
     - Additional postgresql params to be appended to the database URI.
   * - POSTGRESQL_DB_CREATE
     - ``true``
     - By default we will create the required database.

       .. note::
          On own database servers this setting might be troublesome.

nginx
-----
.. list-table::
   :widths: 28 20 52
   :header-rows: 1

   * - Variable
     - Default Value
     - Description
   * - NGINX_EXPOSE_PORT
     - ``8080``
     - The port to be exposed for accessing the Zammad stack from outside.
       Change this to another value if you already have an existing service
       listening on this port.
   * - NGINX_PORT
     - ``8080``
     - The internal port the nginx service will listen on.
   * - NGINX_SERVER_NAME
     - ``_``
     - By default the Nginx container of Zammad will respond to all request.
       You can provide your IP / FQDN if you want to.
   * - NGINX_SERVER_SCHEME
     - ``\$scheme``
     - If the Nginx container for Zammad **is not** the upstream server
       (aka you're using another proxy in front of nginx) ``$scheme`` may be
       wrong. You can set the correct scheme ``http`` or ``https`` if needed.
   * - NGINX_CLIENT_MAX_BODY_SIZE
     - ``(unset)``
     - Define the maximum size of data that a client can send to the server.
   * - ZAMMAD_RAILSSERVER_HOST
     - ``zammad-railsserver``
     - Host name of the rails server container.
   * - ZAMMAD_RAILSSERVER_PORT
     - ``3000``
     - Port of Zammad's rails server. See also: :doc:`/appendix/configure-env-vars`
   * - ZAMMAD_WEBSOCKET_HOST
     - ``zammad-websocket``
     - Host name of Zammad's websocket server.
   * - ZAMMAD_WEBSOCKET_PORT
     - ``6042``
     - Port of Zammad's websocket server. See also: :doc:`/appendix/configure-env-vars`

.. include:: /getting-started/include-csrf-hints.rst
