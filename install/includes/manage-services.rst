Manage services of Zammad
=========================

In general Zammad uses three services - these can be (re)started & stopped 
with the parent ``zammad``.

.. code-block:: sh

   $ # Zammad service to start all services at once
   $ systemctl (status|start|stop|restart) zammad

   $ # Zammads internal puma server (relevant for display the web app)
   $ systemctl (status|start|stop|restart) zammad-web

   $ # Zammads background worker - relevant for all delayed- and background jobs
   $ systemctl (status|start|stop|restart) zammad-worker
   
   $ # Zammads websocket server for session related information
   $ systemctl (status|start|stop|restart) zammad-websocket
