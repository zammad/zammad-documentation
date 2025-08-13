Environment Variables
=====================

Find the available environment variables below with default values, if
applicable. The variables for docker and package based installations might be
different in some cases. You can find a hint in the tables below with the
following meaning:

- |docker| => Only available for docker installations
- |package| => Only available for package installation
- Without badge => Available in both installation variants

To copy/paste batches of variables at once, please have a look at the
`.env.dist file for docker in Github <https://github.com/zammad/zammad-docker-compose/blob/master/.env.dist>`_
or go to the
`section at the end of the page for package installation variables`.

.. hint::

   If you want to use a ``.env`` file in docker compose deployments, you can
   use the provided ``.env.dist`` file and copy it to ``.env``. That way it will
   be picked up by docker compose automatically and not overwritten during
   updates.

Zammad
------
.. list-table::
   :widths: 28 20 52
   :header-rows: 1

   * - |package| Variable
     - Default Value
     - Description
   * - |package| VERSION
     - (current stable version of Zammad)
     - Allows customization of the Zammad image tag. Example: ``6.3.1-54``.
       This default version may be increased when you update your Zammad docker stack.
       Please see the `example env template <https://github.com/zammad/zammad-docker-compose/blob/master/.env.dist>`_
       for more details on this variable.
   * - |package| AUTOWIZARD_JSON
     - ``''``
     - This variable allows you to provide initial configuration data for your
       instance. Autowizard JSON is out of scope of this documentation, however
       `this example file`_ should help.
   * - |package| ZAMMAD_HTTP_TYPE
     - ``(unset)``
     - Set the :admin-docs:`http type </settings/system/base.html>` for your
       instance.
   * - |package| ZAMMAD_FQDN
     - ``(unset)``
     - Set the :admin-docs:`FQDN </settings/system/base.html>` for your instance.
   * - |package| RAILS_TRUSTED_PROXIES
     - ``127.0.0.1,::1``
     - This setting is important for the correct detection of client IP addresses
       and features based on it, like rate limiting.

       By default, Zammad trusts localhost proxies only. Any additional proxy servers
       will have to be added here, by IP address (if static) or by host name.
       Host names are resolved during the start of Zammad, so that a restart is required
       whenever the IP address of a proxy server changes.

       Note that in docker context, Zammad may see the network gateway IP address instead of the
       actual proxy server IP address, if it is placed in another network.
   * - |package| ZAMMAD_WEB_CONCURRENCY
     - ``(unset)``
     - Allows spawning ``n`` workers to allow more simultaneous connections for
       Zammad's web UI. See also: :doc:`/appendix/configure-env-vars`

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-railsserver's CPU setting should match the value from this variable.
   * - |package| | ZAMMAD_PROCESS_SESSION
       | _JOBS_WORKERS
     - ``(unset)``
     - Allows spawning ``n`` independent session jobs workers to release
       pressure from Zammad's background worker. See also:
       :doc:`/appendix/configure-env-vars`.

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker settings variables.
   * - |package| | ZAMMAD_PROCESS_SCHEDULED
       | _JOBS_WORKERS
     - ``(unset)``
     - Allows spawning ``1`` independent scheduled jobs worker to release
       pressure from Zammad's background worker. See also:
       :doc:`/appendix/configure-env-vars`.

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker settings variables.
   * - |package| | ZAMMAD_PROCESS_DELAYED
       | _JOBS_WORKERS
     - ``(unset)``
     - Allows spawning ``n`` delayed jobs workers to release pressure from
       Zammad's background worker. See also: :doc:`/appendix/configure-env-vars`.


       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker settings variables.
   * - |package| MEMCACHE_SERVERS
     - ``zammad-memcached:11211``
     - Provide your own Memcached instance to Zammad if you already have one.
   * - |package| REDIS_URL
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

   * - |package| Variable
     - Default Value
     - Description
   * - |package| ELASTICSEARCH_ENABLED
     - ``true``
     - Setting this variable to false will allow you to run your Zammad without
       Elasticsearch. Please note that we strongly advise **against** doing so.
   * - |package| ELASTICSEARCH_HOST
     - ``zammad-elasticsearch``
     - Provide a host name or address to your external Elasticsearch cluster.
   * - |package| ELASTICSEARCH_PORT
     - ``9200``
     - Provide a different port for Elasticsearch if needed.
   * - |package| ELASTICSEARCH_SCHEMA
     - ``http``
     - By default Elasticsearch is reachable via HTTP.
   * - |package| ELASTICSEARCH_NAMESPACE
     - ``zammad``
     - With this name space all Zammad related indexes will be created. Change
       this if you're using external clusters.
   * - |package| ELASTICSEARCH_REINDEX
     - ``(unset)``
     - The searchindex automatically gets rebuilt when no index can be
       detected. If you need to rebuild the searchindex manually, either set
       this variable to ``true`` or run the reindex command via docker manually.
   * - |package| ELASTICSEARCH_SSL_VERIFY
     - ``true``
     - Allows you to let the compose scripts ignore self signed SSL certificates
       for your Elasticsearch installation if needed.
   * - |package| ELASTICSEARCH_HEAP_SIZE
     - ``1G``
     - Set the available memory for Elasticsearch. If you face issues with ES
       and its performance, you should increase this value to a reasonable size.

PostgreSQL
----------
.. list-table::
   :widths: 28 20 52
   :header-rows: 1

   * - |package| Variable
     - Default Value
     - Description
   * - |package| POSTGRESQL_HOST
     - ``zammad-postgresql``
     - Host name of your PostgreSQL server. Use your own if you already have one.
   * - |package| POSTGRESQL_PORT
     - ``5432``
     - Adjust the Port of your PostgreSQL server.
   * - |package| POSTGRESQL_USER
     - ``zammad``
     - The database user for Zammad.
   * - |package| POSTGRESQL_PASS
     - ``zammad``
     - The password of Zammad's database user.
   * - |package| POSTGRESQL_DB
     - ``zammad_production``
     - Zammad's database to use.
   * - |package| POSTGRESQL_OPTIONS
     - ``?pool=50``
     - Additional postgresql params to be appended to the database URI.
   * - |package| POSTGRESQL_DB_CREATE
     - ``true``
     - By default we will create the required database.

       .. note::
          On own database servers this setting might be troublesome.

nginx
-----
.. list-table::
   :widths: 28 20 52
   :header-rows: 1

   * - |package| Variable
     - Default Value
     - Description
   * - |package| NGINX_EXPOSE_PORT
     - ``8080``
     - The port to be exposed for accessing the Zammad stack from outside.
       Change this to another value if you already have an existing service
       listening on this port.
   * - |package| NGINX_PORT
     - ``8080``
     - The internal port the nginx service will listen on.
   * - |package| NGINX_SERVER_NAME
     - ``_``
     - By default the Nginx container of Zammad will respond to all request.
       You can provide your IP / FQDN if you want to.
   * - |package| NGINX_SERVER_SCHEME
     - ``\$scheme``
     - If the Nginx container for Zammad **is not** the upstream server
       (aka you're using another proxy in front of nginx) ``$scheme`` may be
       wrong. You can set the correct scheme ``http`` or ``https`` if needed.
   * - |package| NGINX_CLIENT_MAX_BODY_SIZE
     - ``(unset)``
     - Define the maximum size of data that a client can send to the server.
   * - |package| ZAMMAD_RAILSSERVER_HOST
     - ``zammad-railsserver``
     - Host name of the rails server container.
   * - |package| ZAMMAD_RAILSSERVER_PORT
     - ``3000``
     - Port of Zammad's rails server. See also: :doc:`/appendix/configure-env-vars`
   * - |package| ZAMMAD_WEBSOCKET_HOST
     - ``zammad-websocket``
     - Host name of Zammad's websocket server.
   * - |package| ZAMMAD_WEBSOCKET_PORT
     - ``6042``
     - Port of Zammad's websocket server. See also: :doc:`/appendix/configure-env-vars`

.. |package| image:: /images/package.svg
   :height: 24px
   :width: 24px

.. |docker| image:: /images/docker.svg
   :height: 24px
   :width: 24px

Collection for Package Installation
-----------------------------------

.. code-block:: sh

   # Zammad

   VERSION
   AUTOWIZARD_JSON
   ZAMMAD_HTTP_TYPE
   ZAMMAD_FQDN
   RAILS_TRUSTED_PROXIES
   ZAMMAD_WEB_CONCURRENCY
   ZAMMAD_PROCESS_SESSION_JOBS_WORKERS
   ZAMMAD_PROCESS_SCHEDULED_JOBS_WORKERS
   ZAMMAD_PROCESS_DELAYED_JOBS_WORKERS
   MEMCACHE_SERVERS
   REDIS_URL


   # Elasticsearch

   ELASTICSEARCH_ENABLED
   ELASTICSEARCH_HOST
   ELASTICSEARCH_PORT
   ELASTICSEARCH_SCHEMA
   ELASTICSEARCH_NAMESPACE
   ELASTICSEARCH_REINDEX
   ELASTICSEARCH_SSL_VERIFY
   ELASTICSEARCH_HEAP_SIZE

   # PostgreSQL

   POSTGRESQL_HOST
   POSTGRESQL_PORT
   POSTGRESQL_USER
   POSTGRESQL_PASS
   POSTGRESQL_DB
   POSTGRESQL_OPTIONS
   POSTGRESQL_DB_CREATE

   # Nginx

   NGINX_EXPOSE_PORT
   NGINX_PORT
   NGINX_SERVER_NAME
   NGINX_SERVER_SCHEME
   NGINX_CLIENT_MAX_BODY_SIZE
   ZAMMAD_RAILSSERVER_HOST
   ZAMMAD_RAILSSERVER_PORT
   ZAMMAD_WEBSOCKET_HOST
   ZAMMAD_WEBSOCKET_PORT
