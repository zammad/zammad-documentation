Manage Services of Zammad
-------------------------

In general Zammad uses three services - these can be (re)started & stopped
with the parent ``zammad``.

Zammad service to start all services at once:

.. code-block:: sh

   $ systemctl (status|start|stop|restart) zammad:

Zammad's internal puma server (relevant for displaying the web app)

.. code-block:: sh

   $ systemctl (status|start|stop|restart) zammad-web:

Zammad's background worker - relevant for all delayed- and background jobs:

.. code-block:: sh

   $ systemctl (status|start|stop|restart) zammad-worker

Zammad's websocket server for session related information:

.. code-block:: sh

   $ systemctl (status|start|stop|restart) zammad-websocket
