Configuration via Environment Variables
=======================================

Use these environment variables to configure Zammad's behavior at runtime.

.. note:: 🙋 **What's an environment variable, and how do I “use” it?**

   Unfortunately, that question has a very long answer
   that goes beyond the scope of this article.
   How you set environment variables will depend on how you installed Zammad
   (*e.g.,* source, package, or Docker).

   But for package installations, here's a short answer:

   .. code-block:: sh

      # set OPTION to "value"
      $ zammad config:set OPTION=value
      $ systemctl restart zammad

      # get OPTION
      $ zammad config:get OPTION

      # unset OPTION
      $ zammad config:unset OPTION
      $ systemctl restart zammad

   To learn more, do some googling on environment variables
   and the shell environment (or execution environment) in Unix.

.. important::

   While below options and remarks affect all installation types of Zammad,
   please note that environment variables mentioned may be named different for
   installations based on :doc:`docker-compose </install/docker-compose>` and
   :doc:`kubernetes </install/kubernetes>`.

General Options
---------------

GPG_PATH
   Defines the path to the GPG installation. This is only needed if you
   installed Zammad from Source, if you want to use different versions of PGP
   on your machine or if your PGP installation differs from the standard
   installation.

   Default: **unset**

RAILS_LOG_TO_STDOUT
   Print output directly to standard output
   instead of ``/var/log/zammad/production.log``.

   This setting can be overwritten during update on package installations.
   Use ``enabled`` to turn this option on only until the next update.
   Use ``true`` to turn it on permanently.

   Default: **unset**

.. _safe_mode:

ZAMMAD_SAFE_MODE
   Ignore availability of third-party services when running Zammad commands.
   Possible values: ``1`` or ``true``

   .. warning::

      **Be careful** when running Zammad commands on production systems in
      safe mode.

      While it may allow an escape hatch for certain commands, it has a
      potential to break regular Zammad operations.

   Default: **unset**

.. _http_type:

ZAMMAD_HTTP_TYPE
   Defines the HTTP protocol of your instance.
   Possible values: ``http`` or ``https``

   Default: unset

.. _fqdn:

ZAMMAD_FQDN
   Defines the fully qualified domain name of the system.

   Default: unset

.. _network_options:

Network Options
---------------

.. note::

   Remember to update your web server config to reflect any changes you
   make here.

ZAMMAD_BIND_IP
   The IP address that the web server is bound to.

   Default: ``127.0.0.1``

ZAMMAD_RAILS_PORT
   The port that the web server is exposed on.

   Default: ``3000``

ZAMMAD_WEBSOCKET_PORT
   The port that the web socket server is exposed on.

   Default: ``6042``

.. _performance_tuning:

Performance Tuning
------------------

**Each of below settings comes with its own tradeoffs.**

There are no “recommended values” here;
the optimal configuration will depend on
your system's resources and typical application load.

Proceed with caution; when adjusting any of these settings,
there is a point at which performance will begin to degrade rather than
improve, or other problems will begin to crop up.

Below settings *may* consume all available database connections.
Please consider the
:doc:`database server configuration </appendix/configure-database-server>`
section for more.

To find out how many users are currently on Zammad, you can use the rails
command below:

.. code-block:: sh

   $ zammad run rails r "p Sessions.list.uniq.count"

WEB_CONCURRENCY
   How many instances of the application server to keep open at a time. It only
   applies if the value is set to ``2`` or higher.

   Increasing this can reduce loading times
   when too many users are on Zammad at once.

   Default: **unset**

ZAMMAD_PROCESS_SESSIONS_JOBS_WORKERS
   How many instances of the session worker to run at a time. It only
   applies if the value is set to ``2`` or higher.

   Increasing this can speed up background jobs (like the scheduler)
   when many users are on Zammad at once.

   It is not useful to adjust this setting if you have less than 40 active
   users at a time. Increasing the amount of workers can consume a lot of
   resources!

   Default: **unset**

ZAMMAD_PROCESS_SCHEDULED_JOBS_WORKERS
   Allows spawning an independent process just for processing scheduled jobs
   like LDAP syncs. This can free up Zammad's background worker for other tasks
   when running tasks that take rather long.

   | Default: **unset**
   | Maximum number of workers: ``1``

   .. danger::

      Disable processing of scheduled jobs by setting
      ``ZAMMAD_PROCESS_SCHEDULED_JOBS_DISABLE``.

      Doing so on productive instances will draw important parts of your
      instance not working. **WE STRONGLY** encourage against using this flag.

ZAMMAD_PROCESS_DELAYED_JOBS_WORKERS
   How many processes should work on delayed jobs? It only
   applies if the value is set to ``2`` or higher.

   Increasing this *can* improve issues with delayed jobs stacking up in your
   system. You may want to try to use ``ZAMMAD_SESSION_JOBS_CONCURRENT`` before
   though.

   | Default: **unset**
   | Maximum number of workers: ``16``

   .. warning:: 🥵 **This option can be very CPU-intensive.**

   .. danger::

      Disable processing of delayed jobs by setting
      ``ZAMMAD_PROCESS_DELAYED_JOBS_DISABLE``.

      Doing so on productive instances will draw important parts of your
      instance not working. **WE STRONGLY** encourage against using this flag.


ZAMMAD_PROCESS_DELAYED_AI_JOBS_WORKERS
   How many instances of AI workers should run simultaneously. AI workers handle
   Zammad's AI requests and fetch the responses from the configured AI provider.
   By default, one worker is running.

   Self hosted AI users should be careful in increasing it. Depending on your
   hardware, it may cause your AI service to collapse.

   For AI cloud service users with a big Zammad instance, it could make sense
   to increase it to have some kind of parallelization.

   | Default: **unset**
   | Maximum number of workers: ``16``


ZAMMAD_PROCESS_DELAYED_AI_JOBS_WORKERS_THREADS
   How many threads should be processed by **one** AI worker (if you have more
   than one worker, it is multiplied by the amount of workers). This may speed
   up the AI processing, but be aware that a ruby worker can only span across 1
   core anyway.

   | Default: ``5``
   | Maximum number of threads: ``16``


--------------------------------------------------------------------------------

.. note::

   The options listed below allow you to distribute Zammad processes
   over several application nodes. Even if that's not your goal, they may
   provide great benefits on bigger installations.

   Please note that distribution of processes on several nodes is out of
   the scope of this documentation for various reasons.

REDIS_URL
   | Store your web socket connection information within Redis.
   | To do so, tell Zammad where to find your Redis instance:
     ``redis://your.redis.server:6379``

   If not provided, Zammad falls back to file system
   (``/opt/zammad/tmp/websocket_*``).

   Default: **unset**

MEMCACHE_SERVERS
   | Store your application cache files within Memcached.
   | To do so, tell Zammad where to find your Memcached instance:
     ``your.memcached.server:11211``

   If not provided, Zammad falls back to file system
   (``/opt/zammad/tmp/cache*``).

   Memcached allows you to restrict the maximum size Zammad may store
   as cache. This comes in handy in terms of performance and keeping
   caching files small. ``1 GB`` should be a reasonable size.

Storage Options
---------------

S3_URL
   Allows you to provide your S3 configuration. Please have a look in our admin
   documentation, where the :admin-docs:`setup of S3 storage </settings/system/storage.html>`
   is described.

   Format / example: ``https://key:secret@s3.eu-central-1.amazonaws.com/zammad-storage-bucket?region=eu-central-1&force_path_style=true``
