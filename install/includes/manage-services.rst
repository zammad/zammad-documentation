Manage services of Zammad
=========================

In general Zammad uses three services - these can be (re)started & stopped with the parent ``zammad``.

.. code-block:: sh

   $ # Zammad service to start all services at once
   $ sudo systemctl (status|start|stop|restart) zammad

   $ # Zammads internal railsserver
   $ sudo systemctl (status|start|stop|restart) zammad-web

   $ # Zammads scheduler - relevant for all delayed- and background jobs
   $ sudo systemctl (status|start|stop|restart) zammad-worker
   
   $ # Zammads websocket server for session related information
   $ sudo systemctl (status|start|stop|restart) zammad-websocket
