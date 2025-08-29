Manage Services of Zammad
-------------------------

Zammad uses three services. These services can be managed individually or all at
once by using the parent **zammad**.

- **zammad**: includes the services below

  - **zammad-web**: internal puma server (relevant for displaying the web app)
  - **zammad-worker**: background worker - relevant for all delayed- and background jobs
  - **zammad-websocket**: websocket server for session related information

Manage the services with ``systemctl``'s commands ``start``, ``restart``,
``stop``, ``status``. Example to start Zammad with all sub-services:

.. code-block:: console

   $ sudo systemctl start zammad

To stop or restart a service or to check its status, adjust the command as
mentioned above.