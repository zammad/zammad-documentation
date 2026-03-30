Environment Variables
=====================

Find the most important environment variables below with default values, if
applicable. The variables for Docker and package based installations can be
different in some cases. You can find a badge appended to variable names with
the following meaning:

- |docker| => Only available for Docker installations
- |package| => Only available for package installation
- Without badge => Available for both installation variants

.. hint::

   If you want to use a ``.env`` file in Docker Compose deployments, you can
   use the provided ``.env.dist`` file and copy it to ``.env``. That way it will
   be picked up by Docker Compose automatically and not overwritten during
   updates.

Miscellaneous
-------------

GPG_PATH |package|
   Default: unset

   Defines the path of your GPG installation. Only needed if you want to use
   different versions of PGP or if your PGP installation differs from the
   standard installation.

RAILS_LOG_TO_STDOUT |package|
   Default: unset

   This setting can be overwritten during update on package installations.
   Use ``enabled`` to turn this option on only until the next update.
   Use ``true`` to turn it on permanently.

ZAMMAD_SAFE_MODE |package|
   Default: unset

   Be careful when running Zammad commands on production systems in safe mode.
   While it may allow an escape hatch for certain commands, it has a potential
   to break regular Zammad operations.

ZAMMAD_BIND_IP |package|
   Default: ``127.0.0.1``

   The IP address that the web server is bound to.

S3_URL |package|
   Default: unset

   Allows you to provide your S3 configuration. Please have a look in our
   admin documentation, where the
   :admin-docs:`setup of S3 storage </settings/system/storage.html>` is
   described.
   Example for value:
   ``https://key:secret@s3.eu-central-1.amazonaws.com/zammad-storage-bucket?region=eu-central-1&force_path_style=true``

Zammad
------

VERSION |docker|
   Default: current stable version of Zammad

   Allows customization of the Zammad image tag. Example: ``6.3.1-54``.
   This default version may be increased when you update your Zammad Docker
   stack. Please see the
   `example env template <https://github.com/zammad/zammad-docker-compose/blob/master/.env.dist>`_
   for more details on this variable.

AUTOWIZARD_JSON |docker|
   Default: unset

   This variable allows you to provide initial configuration data for your
   instance. Autowizard JSON is out of scope of this documentation, however
   `this example file <https://github.com/zammad/zammad/blob/stable/contrib/auto_wizard_example.json>`_
   should help.

ZAMMAD_HTTP_TYPE
   Default: unset

   Set the :admin-docs:`http type </settings/system/base.html>` for your
   instance. Possible values are ``http`` and ``https``.

ZAMMAD_FQDN
   Default: unset

   Set the :admin-docs:`FQDN </settings/system/base.html>` for your instance.

RAILS_TRUSTED_PROXIES
   Default: ``127.0.0.1,::1``

   This setting is important for the correct detection of client IP addresses
   and features based on it, like rate limiting.

   By default, Zammad trusts localhost proxies only. Any additional proxy
   servers will have to be added here, by IP address (if static) or by host
   name. Host names are resolved during the start of Zammad, so that a
   restart is required whenever the IP address of a proxy server changes.

   Note that in Docker context, Zammad may see the network gateway IP
   address instead of the actual proxy server IP address, if it is placed in
   another network.

ZAMMAD_MANAGE_SESSIONS_JOBS_WORKERS
   Default: ``0``

   Allows to fork the job that dispatches the session jobs to their workers
   to a child process. Allowed value to enable it: ``1``.

ZAMMAD_PROCESS_DELAYED_AI_JOBS_WORKERS
   Default: ``0``

   How many instances of AI worker processes to run simultaneously. AI workers
   handle Zammad's AI requests and fetch the responses from the configured AI
   provider. ``0`` means it runs in the main process, ``1`` means one additional
   process, etc. The maximum number of workers is ``16``.

   Self hosted AI users should be careful in increasing it, your AI service
   might collapse. For AI cloud service users with a big Zammad instance, it
   could make sense to increase it to have some kind of parallelization.

ZAMMAD_PROCESS_DELAYED_AI_JOBS_WORKERS_THREADS
   Default: ``5``

   How many threads should be processed by **one** AI worker process (if you
   have more than one worker process, it is multiplied by their amount). This
   may speed up the AI processing, but be aware that a Ruby worker can only span
   across 1 core anyway. The maximum number of threads is ``16``.

ZAMMAD_PROCESS_DELAYED_COMMUNICATION_INBOUND_JOBS_WORKERS
   Default: ``0``

   Allows concurrent fetching of inbound communication channels.
   Useful if you have many channels and/or mailboxes added. ``0`` means it
   runs in the main process, ``1`` means one additional process, etc. The
   maximum number of workers is ``16``.

ZAMMAD_PROCESS_DELAYED_COMMUNICATION_INBOUND_JOBS_WORKER_THREADS
   Default: ``1``

   Threads used for fetching inbound communication channels. How many
   threads should be used by inbound jobs workers. The maximum
   number of threads is ``16``.

MEMCACHE_SERVERS
   Default:

   - Docker: ``zammad-memcached:11211``
   - Package: unset

   Provide your own Memcached instance to Zammad if you already have one.
   The package installation fallback is ``/opt/zammad/tmp/cache*``.

REDIS_URL
   Default:

   - Docker: ``redis://zammad-redis:6379``
   - Package: unset

   Provide your own Redis instance if you already have one.
   The package installation fallback is ``/opt/zammad/tmp/websocket_*``.
   See :doc:`Redis Variables </appendix/redis>` for a Sentinel setup.

Elasticsearch
-------------

ELASTICSEARCH_ENABLED |docker|
   Default: ``true``

   Setting this variable to false will allow you to run your Zammad without
   Elasticsearch. Please note that we strongly advise **against** doing so.

ELASTICSEARCH_HOST |docker|
   Default: ``zammad-elasticsearch``

   Provide a host name or address of your external Elasticsearch cluster.

ELASTICSEARCH_PORT |docker|
   Default: ``9200``

   Provide a different port for Elasticsearch if needed.

ELASTICSEARCH_SCHEMA |docker|
   Default: ``http``

   Change it to ``https`` if your Elasticsearch cluster is configured to use SSL.

ELASTICSEARCH_NAMESPACE |docker|
   Default: ``zammad``

   With this name space all Zammad related indexes will be created. Change
   this if you're using external clusters.

ELASTICSEARCH_REINDEX |docker|
   Default: unset

   The searchindex automatically gets rebuilt when no index can be
   detected. If you need to rebuild the searchindex manually, either set
   this variable to ``true`` or run the reindex command via Docker manually.

ELASTICSEARCH_SSL_VERIFY |docker|
   Default: ``true``

   Allows you to let the Compose scripts ignore self signed SSL certificates
   for your Elasticsearch installation if needed.

ELASTICSEARCH_HEAP_SIZE |docker|
   Default: ``1G``

   Set the available memory for Elasticsearch. If you face issues with ES
   and its performance, you should increase this value to a reasonable size.

PostgreSQL
----------

.. note:: Variables for Docker and package installation are partially different.
   Check the badges appended to the variable names and make sure to pick the
   right one. The both variables at the end of this section are valid for both
   installation types.

POSTGRESQL_HOST |package|
   Default: ``zammad-postgresql``

   Host name or IP address of your PostgreSQL server. In case you use an
   IPv6 address, enclose the address in square brackets (e.g.
   ``[2001:db8::2]``).

POSTGRESQL_PORT |package|
   Default: ``5432``

   Adjust the Port of your PostgreSQL server.

POSTGRESQL_USER |package|
   Default: ``zammad``

   The database user for Zammad.

POSTGRESQL_PASS |package|
   Default: ``zammad``

   The password of Zammad's database user.

POSTGRESQL_DB |package|
   Default: ``zammad_production``

   Zammad's database to use.

POSTGRES_HOST |docker|
   Default: ``zammad-postgresql``

   Host name or IP address of your PostgreSQL server. In case you use an
   IPv6 address, enclose the address in square brackets (e.g.
   ``[2001:db8::2]``).

POSTGRES_PORT |docker|
   Default: ``5432``

   Adjust the Port of your PostgreSQL server.

POSTGRES_USER |docker|
   Default: ``zammad``

   The database user for Zammad.

POSTGRES_PASS |docker|
   Default: ``zammad``

   The password of Zammad's database user.

POSTGRES_DB |docker|
   Default: ``zammad_production``

   Zammad's database to use.

POSTGRESQL_OPTIONS
   Default: ``?pool=50``

   Additional PostgreSQL params to be appended to the database URI.

POSTGRESQL_DB_CREATE
   Default: ``true``

   By default, Zammad creates the required database. On already existing
   database servers, the default might be troublesome.

Nginx
-----

NGINX_EXPOSE_PORT |docker|
   Default: ``8080``

   The port to be exposed for accessing the Zammad stack from outside.
   Change this to another value if you already have an existing service
   listening on this port.

NGINX_PORT |docker|
   Default: ``8080``

   The internal port the Nginx service will listen on.

NGINX_SERVER_NAME |docker|
   Default: ``_``

   By default, the Nginx container of Zammad will respond to all request.
   You can provide your IP / FQDN if you want to.

NGINX_SERVER_SCHEME |docker|
   Default: ``\$scheme``

   If the Nginx container for Zammad **is not** the upstream server
   (aka you're using another proxy in front of Nginx) ``$scheme`` may be
   wrong. You can set the correct scheme ``http`` or ``https`` if needed.
   Set this if you face a ``CSRF Token Verification Failed`` error.

NGINX_CLIENT_MAX_BODY_SIZE |docker|
   Default: unset

   Define the maximum size of data that a client can send to the server.

ZAMMAD_RAILSSERVER_HOST |docker|
   Default: ``zammad-railsserver``

   Host name of the Rails server container.

ZAMMAD_RAILSSERVER_PORT |docker|
   Default: ``3000``

   Port of Zammad's Rails server.

ZAMMAD_RAILS_PORT |package|
   Default: ``3000``

   Port of Zammad's Rails server.

ZAMMAD_WEBSOCKET_HOST |docker|
   Default: ``zammad-websocket``

   Host name of Zammad's websocket server.

ZAMMAD_WEBSOCKET_PORT |docker|
   Default: ``6042``

   Port of Zammad's websocket server.

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

ZAMMAD_WEB_CONCURRENCY
   Default: unset

   Allows spawning ``n`` worker processes to allow more simultaneous connections
   for Zammad's web UI.
   In case you applied :doc:`Docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
   the zammad-railsserver's CPU setting should match the value from this variable.

ZAMMAD_PROCESS_SESSION_JOBS_WORKERS
   Default: unset

   How many processes of the session worker to run at a time. Increasing
   this value can speed up background jobs (like the scheduler) when many
   users are on Zammad at once. However, it is not useful to adjust this
   setting if you have less than 40 active users at a time. Increasing the
   amount of these processes can consume a lot of resources!

   In case you applied :doc:`Docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
   the zammad-scheduler CPU setting should match the sum of all worker
   settings variables.

ZAMMAD_PROCESS_SCHEDULED_JOBS_WORKERS
   Default: unset

   Allows spawning ``1`` independent worker process to release
   pressure from Zammad's background worker. Maximum number of workers:
   ``1``.

   In case you applied :doc:`Docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
   the zammad-scheduler CPU setting should match the sum of all worker
   settings variables.

ZAMMAD_PROCESS_DELAYED_JOBS_WORKERS
   Default: unset

   Allows spawning ``n`` worker processes to release pressure from
   Zammad's background worker. ``0`` means it runs in the main process,
   ``1`` means one additional process, etc. The maximum number of workers
   is ``16``.

   In case you applied :doc:`Docker hardware resource limits </install/docker-compose/docker-compose-scenarios>`,
   the zammad-scheduler CPU setting should match the sum of all worker
   settings variables.

ZAMMAD_PROCESS_DELAYED_JOBS_WORKER_THREADS
   Default: unset

   Threads used by **one** delayed jobs worker process (if you have more than
   one worker process, it is multiplied by their amount). The maximum number of
   threads is ``16``.

.. |package| image:: /images/package.svg
   :height: 24px
   :width: 24px

.. |docker| image:: /images/docker.svg
   :height: 24px
   :width: 24px

.. _how-to-env-var:

How to Set Environment Variables
--------------------------------

It depends on how you installed Zammad (package, Docker).
Either set it via ``zammad config`` command as you can see below, use your
system's way of setting variables via command line
(e.g. ``export VARIABLE=value)``, place an ``.env`` file in the directory or
even use a GUI like Portainer to define them for a Docker installation.

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
