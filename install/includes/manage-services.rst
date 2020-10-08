Manage services of Zammad
=========================

Zammad
------

.. code-block:: sh

   $ sudo systemctl status zammad
   $ sudo systemctl stop zammad
   $ sudo systemctl start zammad
   $ sudo systemctl restart zammad

Only web application server
---------------------------

.. code-block:: sh

   $ sudo systemctl status zammad-web
   $ sudo systemctl stop zammad-web
   $ sudo systemctl start zammad-web
   $ sudo systemctl restart zammad-web

Only worker process
-------------------

.. code-block:: sh

   $ sudo systemctl status zammad-worker
   $ sudo systemctl stop zammad-worker
   $ sudo systemctl start zammad-worker
   $ sudo systemctl restart zammad-worker

Only websocket server
---------------------

.. code-block:: sh

   $ sudo systemctl status zammad-websocket
   $ sudo systemctl stop zammad-websocket
   $ sudo systemctl start zammad-websocket
   $ sudo systemctl restart zammad-websocket