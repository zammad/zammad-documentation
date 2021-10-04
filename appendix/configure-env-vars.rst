Configuration via Environment Variables
***************************************

Use these environment variables to configure Zammad’s behavior at runtime.

.. note:: 🙋 **What’s an environment variable, and how do I “use” it?**

   Unfortunately, that question has a very long answer
   that goes beyond the scope of this article.
   How you set environment variables will depend on how you installed Zammad
   (*e.g.,* source, package, or Docker).

   But for package installations, here’s a short answer:

   .. code-block:: sh

      # set OPTION to "value"
      $ zammad config:set OPTION=value
      $ systemctl restart zammad

      # unset OPTION
      $ zammad config:unset OPTION
      $ systemctl restart zammad

   To learn more, do some googling on environment variables
   and the shell environment (or execution environment) in Unix.

General Options
===============

APP_RESTART_CMD
   The command Zammad will use to automatically restart the server
   after `changes have been made in the Object Manager
   <https://admin-docs.zammad.org/en/latest/system/objects.html>`_.
   (*E.g.,* ``"systemctl restart zammad"``)

   If this is undefined, you will have to restart manually
   after making changes in the Object Manager.

   Default: **unset**

RAILS_LOG_TO_STDOUT
   Print output directly to standard output
   instead of ``/var/log/zammad/production.log``.

   .. warning:: On package installations, 
      ⏫ **this setting can be overwritten during update.**

      Use ``enabled`` to turn this option on only until the next update.
      Use ``true`` to turn it on permanently.

   Default: **unset**

.. _network_options:

🖧 Network Options
=================

ZAMMAD_BIND_IP
   The IP address that the web server is bound to.

   Default: ``0.0.0.0``

ZAMMAD_RAILS_PORT
   The port that the web server is exposed on.

   Default: ``3000``

ZAMMAD_WEBSOCKET_PORT
   The port that the web socket server is exposed on.

   Default: ``6042``

.. note:: 

   Remember to update your web server config to reflect any changes you
   make here.

.. _performance_tuning:

🎛️ Performance Tuning
=====================

.. warning:: ⚖️ **Each of these settings comes with its own tradeoffs.**

   There are no “recommended values” here;
   the optimal configuration will depend on
   your system’s resources and typical application load.

   Proceed with caution; when adjusting any of these settings,
   there is a point at which performance will begin to degrade rather than
   improve, or other problems will begin to crop up.

WEB_CONCURRENCY
   How many instances of the application server to keep open at a time.

   Increasing this can reduce loading times
   when too many users are on Zammad at once.

   Default: **unset**

ZAMMAD_SESSION_JOBS_CONCURRENT
   How many instances of the session worker to run at a time.

   Increasing this can speed up background jobs (like the scheduler)
   when too many users are on Zammad at once.

   Generally speaking, it should only be useful to adjust this setting
   if you have more than 40 active users at a time.

   .. warning:: 🥵 **Session workers can be extremely CPU-intensive.**

      In some cases, they can reach 100% CPU utilization on their own.
      Increasing this setting is safer on systems with more cores.

   Default: **unset**

.. tip:: 🤔 **How can I find out how many users are currently on Zammad?**

   .. code-block:: sh

      $ zammad run rails r "p Sessions.list.uniq.count" 

.. hint::

   Above settings *may* consume all available database connections. Please consider the 
   :doc:`database server configuration </appendix/configure-database-server>` 
   section for more.
