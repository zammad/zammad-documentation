Environment Variables
=====================

Find the most important environment variables below with default values, if
applicable. The variables for docker and package based installations can be
different in some cases. You can find a badge in the column **Limited** with the
following meaning:

- |docker| => Only available for docker installations
- |package| => Only available for package installation
- Without badge => Available for both installation variants

.. hint::

   If you want to use a ``.env`` file in docker compose deployments, you can
   use the provided ``.env.dist`` file and copy it to ``.env``. That way it will
   be picked up by docker compose automatically and not overwritten during
   updates.

Miscellaneous
-------------

.. list-table::
   :widths: 28 3 22 47
   :header-rows: 1

   * - Variable
     - Limited
     - Default Value
     - Description
   * - GPG_PATH
     - |package|
     - unset
     - Defines the path of your GPG installation. Only needed if you want to use
       different versions of PGP or if your PGP installation differs from the
       standard installation.
   * - RAILS_LOG_TO_STDOUT
     - |package|
     - unset
     - This setting can be overwritten during update on package installations.
       Use ``enabled`` to turn this option on only until the next update.
       Use ``true`` to turn it on permanently.
   * - ZAMMAD_SAFE_MODE
     - |package|
     - unset
     - Be careful when running Zammad commands on production systems in safe
       mode. While it may allow an escape hatch for certain commands, it has a
       potential to break regular Zammad operations.
   * - ZAMMAD_BIND_IP
     - |package|
     - ``127.0.0.1``
     - The IP address that the web server is bound to.
   * - S3_URL
     - |package|
     - unset
     - Allows you to provide your S3 configuration. Please have a look in our
       admin documentation, where the
       :admin-docs:`setup of S3 storage </settings/system/storage.html>` is
       described.
       Example for value:
       ``https://key:secret@s3.eu-central-1.amazonaws.com/zammad-storage-bucket?region=eu-central-1&force_path_style=true``

Zammad
------

.. list-table::
   :widths: 28 3 22 47
   :header-rows: 1

   * - Variable
     - Limited
     - Default Value
     - Description
   * - VERSION
     - |docker|
     - current stable version of Zammad
     - Allows customization of the Zammad image tag. Example: ``6.3.1-54``.
       This default version may be increased when you update your Zammad docker
       stack. Please see the
       `example env template <https://github.com/zammad/zammad-docker-compose/blob/master/.env.dist>`_
       for more details on this variable.
   * - AUTOWIZARD_JSON
     - |docker|
     - unset
     - This variable allows you to provide initial configuration data for your
       instance. Autowizard JSON is out of scope of this documentation, however
       `this example file <https://github.com/zammad/zammad/blob/stable/contrib/auto_wizard_example.json>`_
       should help.
   * - ZAMMAD_HTTP_TYPE
     - 
     - unset
     - Set the :admin-docs:`http type </settings/system/base.html>` for your
       instance. Possible values are ``http`` and ``https``.
   * - ZAMMAD_FQDN
     - 
     - unset
     - Set the :admin-docs:`FQDN </settings/system/base.html>` for your instance.
   * - RAILS_TRUSTED_PROXIES
     - 
     - ``127.0.0.1,::1``
     - This setting is important for the correct detection of client IP addresses
       and features based on it, like rate limiting.

       By default, Zammad trusts localhost proxies only. Any additional proxy
       servers will have to be added here, by IP address (if static) or by host
       name. Host names are resolved during the start of Zammad, so that a
       restart is required whenever the IP address of a proxy server changes.

       Note that in docker context, Zammad may see the network gateway IP
       address instead of the actual proxy server IP address, if it is placed in
       another network.
   * - | ZAMMAD_PROCESS_DELAYED\_
       | AI_JOBS_WORKERS
     - 
     - unset
     - How many instances of AI workers to run simultaneously. AI workers handle
       Zammad's AI requests and fetch the responses from the configured AI
       provider. By default, one worker is running.
       Self hosted AI users should be careful in increasing it, your AI service
       might collapse. For AI cloud service users with a big Zammad instance, it
       could make sense to increase it to have some kind of parallelization.
       The maximum number of workers is ``16``.
   * - | ZAMMAD_PROCESS_DELAYED\_
       | AI_JOBS_WORKERS_THREADS
     - 
     - ``5``
     - How many threads should be processed by **one** AI worker (if you have more
       than one worker, it is multiplied by the amount of workers). This may
       speed up the AI processing, but be aware that a ruby worker can only span
       across 1 core anyway. The maximum number of threads is ``16``.
   * - MEMCACHE_SERVERS
     - 
     - - Docker: ``zammad-memcached:11211``
       - Package: unset
     - Provide your own Memcached instance to Zammad if you already have one.
       The package installation fallback is ``/opt/zammad/tmp/cache*``.
   * - REDIS_URL
     - 
     - - Docker: ``redis://zammad-redis:6379``
       - Package: unset
     - Provide your own Redis instance if you already have one. Please note
       that this method currently does not allow authentication.
       The package installation fallback is ``/opt/zammad/tmp/websocket_*``.

Elasticsearch
-------------

.. list-table::
   :widths: 28 3 22 47
   :header-rows: 1

   * - Variable
     - Limited
     - Default Value
     - Description
   * - ELASTICSEARCH_ENABLED
     - |docker|
     - ``true``
     - Setting this variable to false will allow you to run your Zammad without
       Elasticsearch. Please note that we strongly advise **against** doing so.
   * - ELASTICSEARCH_HOST
     - |docker|
     - ``zammad-elasticsearch``
     - Provide a host name or address to your external Elasticsearch cluster.
   * - ELASTICSEARCH_PORT
     - |docker|
     - ``9200``
     - Provide a different port for Elasticsearch if needed.
   * - ELASTICSEARCH_SCHEMA
     - |docker|
     - ``http``
     - By default, Elasticsearch is reachable via HTTP.
   * - ELASTICSEARCH_NAMESPACE
     - |docker|
     - ``zammad``
     - With this name space all Zammad related indexes will be created. Change
       this if you're using external clusters.
   * - ELASTICSEARCH_REINDEX
     - |docker|
     - unset
     - The searchindex automatically gets rebuilt when no index can be
       detected. If you need to rebuild the searchindex manually, either set
       this variable to ``true`` or run the reindex command via docker manually.
   * - ELASTICSEARCH_SSL_VERIFY
     - |docker|
     - ``true``
     - Allows you to let the compose scripts ignore self signed SSL certificates
       for your Elasticsearch installation if needed.
   * - ELASTICSEARCH_HEAP_SIZE
     - |docker|
     - ``1G``
     - Set the available memory for Elasticsearch. If you face issues with ES
       and its performance, you should increase this value to a reasonable size.

PostgreSQL
----------

.. list-table::
   :widths: 28 3 22 47
   :header-rows: 1

   * - Variable
     - Limited
     - Default Value
     - Description
   * - POSTGRESQL_HOST
     - |docker|
     - ``zammad-postgresql``
     - Host name of your PostgreSQL server. Use your own if you already have one.
   * - POSTGRESQL_PORT
     - |docker|
     - ``5432``
     - Adjust the Port of your PostgreSQL server.
   * - POSTGRESQL_USER
     - |docker|
     - ``zammad``
     - The database user for Zammad.
   * - POSTGRESQL_PASS
     - |docker|
     - ``zammad``
     - The password of Zammad's database user.
   * - POSTGRESQL_DB
     - |docker|
     - ``zammad_production``
     - Zammad's database to use.
   * - POSTGRESQL_OPTIONS
     - |docker|
     - ``?pool=50``
     - Additional postgresql params to be appended to the database URI.
   * - POSTGRESQL_DB_CREATE
     - |docker|
     - ``true``
     - By default, Zammad creates the required database. On already existing
       database servers, the default might be troublesome.

Nginx
-----

.. list-table::
   :widths: 28 3 22 47
   :header-rows: 1

   * - Variable
     - Limited
     - Default Value
     - Description
   * - NGINX_EXPOSE_PORT
     - |docker|
     - ``8080``
     - The port to be exposed for accessing the Zammad stack from outside.
       Change this to another value if you already have an existing service
       listening on this port.
   * - NGINX_PORT
     - |docker|
     - ``8080``
     - The internal port the Nginx service will listen on.
   * - NGINX_SERVER_NAME
     - |docker|
     - ``_``
     - By default, the Nginx container of Zammad will respond to all request.
       You can provide your IP / FQDN if you want to.
   * - NGINX_SERVER_SCHEME
     - |docker|
     - ``\$scheme``
     - If the Nginx container for Zammad **is not** the upstream server
       (aka you're using another proxy in front of Nginx) ``$scheme`` may be
       wrong. You can set the correct scheme ``http`` or ``https`` if needed.
   * - NGINX_CLIENT_MAX_BODY_SIZE
     - |docker|
     - unset
     - Define the maximum size of data that a client can send to the server.
   * - ZAMMAD_RAILSSERVER_HOST
     - |docker|
     - ``zammad-railsserver``
     - Host name of the rails server container.
   * - ZAMMAD_RAILSSERVER_PORT
     - |docker|
     - ``3000``
     - Port of Zammad's rails server.
   * - ZAMMAD_RAILS_PORT
     - |package|
     - ``3000``
     - Port of Zammad's rails server.
   * - ZAMMAD_WEBSOCKET_HOST
     - |docker|
     - ``zammad-websocket``
     - Host name of Zammad's websocket server.
   * - ZAMMAD_WEBSOCKET_PORT
     - |docker|
     - ``6042``
     - Port of Zammad's websocket server.

.. _performance-tuning:

Performance Tuning
------------------

Each of below settings comes with its own tradeoffs. There are no recommended
values here; the optimal configuration depends on your system's resources and
typical application load.

Proceed with caution; when adjusting any of these settings, there is a point at
which performance will begin to degrade rather than improve, or other problems
will begin to emerge.

Below settings may consume all available database connections. Please consider
the :doc:`configure-database-server` for more information.

.. list-table::
   :widths: 28 3 22 47
   :header-rows: 1

   * - Variable
     - Limited
     - Default Value
     - Description
   * - ZAMMAD_WEB_CONCURRENCY
     - 
     - unset
     - Allows spawning ``n`` workers to allow more simultaneous connections for
       Zammad's web UI.
       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-railsserver's CPU setting should match the value from this variable.
   * - | ZAMMAD_PROCESS\_
       | SESSION_JOBS_WORKERS
     - 
     - unset
     - How many instances of the session worker to run at a time. Increasing
       this value can speed up background jobs (like the scheduler) when many
       users are on Zammad at once. However, it is not useful to adjust this
       setting if you have less than 40 active users at a time. Increasing the
       amount of workers can consume a lot of resources!

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker
       settings variables.
   * - | ZAMMAD_PROCESS\_
       | SCHEDULED_JOBS_WORKERS
     - 
     - unset
     - Allows spawning ``1`` independent scheduled jobs worker to release
       pressure from Zammad's background worker. Maximum number of workers:
       ``1``.

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker
       settings variables.
   * - | ZAMMAD_PROCESS\_
       | DELAYED_JOBS_WORKERS
     - 
     - unset
     - Allows spawning ``n`` delayed jobs workers to release pressure from
       Zammad's background worker.

       In case you applied :doc:`docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
       the zammad-scheduler CPU setting should match the sum of all worker
       settings variables.

.. |package| image:: /images/package.svg
   :height: 24px
   :width: 24px

.. |docker| image:: /images/docker.svg
   :height: 24px
   :width: 24px

.. _how-to-env-var:

How to Set Environment Variables
--------------------------------

It depends on how you installed Zammad (package, docker).
Either set it via ``zammad config`` command as you can see below, use your
system's way of setting variables via command line
(e.g. ``export VARIABLE=value)``, place an ``.env`` file in the directory or
even use a GUI like Portainer to define them for a docker installation.

Example for package installations:

Set OPTION to "value":

.. code-block:: console

   $ zammad config:set OPTION=value

Get the value of OPTION:

.. code-block:: console

   $ zammad config:get OPTION

Unset the OPTION:

.. code-block:: console

   $ zammad config:unset OPTION

When changing settings, make sure to restart Zammad:

.. code-block:: console

   $ sudo systemctl restart zammad
