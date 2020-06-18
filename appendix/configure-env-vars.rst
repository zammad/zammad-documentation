Configure environment variables
*******************************

If you're using the DEB or RPM packages you can change Zammads environment variables by the following commands.

Configure IP
============

.. code-block:: sh

   $ zammad config:set ZAMMAD_BIND_IP=0.0.0.0
   $ systemctl restart zammad


Configure ports
===============

Please note that you also have to reconfigure Nginx when changing the ports!

.. code-block:: sh

   $ zammad config:set ZAMMAD_RAILS_PORT=3000
   $ zammad config:set ZAMMAD_WEBSOCKET_PORT=6042
   $ systemctl restart zammad

Application Servers
===================

Per default one application server will get started. If you have more http requests (user sessions) you need to increase the amount of your application server. The typical problem is long waiting times in the web interface for opening or editing tickets.

.. code-block:: sh

   $ zammad config:set WEB_CONCURRENCY=3
   $ systemctl restart zammad

Configure Restart Command
=========================

If you need to make changes (creating objects) to Zammad, it can be necessary to restart the service.
This can be done manually or automatic. If you like to use the automatic way you need to set an special environment variable.

Note: you might need to adjust the value for APP_RESTART_CMD if you have / need a different command to restart your Zammad on your installation.

.. code-block:: sh

   $ zammad config:set APP_RESTART_CMD="systemctl restart zammad"


Configure Zammad to log to STDOUT
=================================

If you want to log to STDOUT instead of the production-logfile (``/var/log/zammad/production.log``) you can set it:

.. code-block:: sh

   $ zammad config:set RAILS_LOG_TO_STDOUT=true

To reset this back to logfile logging run:

.. code-block:: sh

   $ zammad config:set RAILS_LOG_TO_STDOUT=


.. note:: **This applies to package installations:** Do not set it to ``enabled``, because we'll then unset the variable upon Update!
   Using ``true`` is **update safe**.

Spawn multiple Session Workers
==============================

.. note:: This is a potential performance tuning option, but can also worsen performance.

Spawning multiple session workers usually only is required if you have a lot of concurrent agents working on Zammad. 
The moment this option is needed highly depends on your configuration (e.g. number and complexity of overviews) and 
thus can't be set to a fixed number. From what we've seen it usually isn't necessary to do so with less than 40 
concurrent agents.

   .. tip:: Not sure how much concurrent agents you currently have? Run ``zammad run rails r "p Sessions.list.count"`` 
      to get the number of currently active agents.

.. warning:: While launching several session workers can be handy, this also means that you might need more CPU cores! 
   A session worker can potentially utualize the whole CPU core to 100% on it's own. **Be careful.**

.. code-block:: sh
   $ # Launch 2 concurrent session workers
   $ zammad config:set ZAMMAD_SESSION_JOBS_CONCURRENT=2
   $ systemctl restart zammad

.. code-block:: sh
   $ # Reset session workers back to default
   $ zammad config:set ZAMMAD_SESSION_JOBS_CONCURRENT=
   $ systemctl restart zammad
