For security reasons, ensure that your database configuration
is readable for the Zammad user only.

.. code-block:: sh

   $ chmod 600 /opt/zammad/config/database.yml
   $ chown zammad:zammad /opt/zammad/config/database.yml
