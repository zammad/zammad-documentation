Configure Database Server
=========================

.. note::

   We can't provide a complete how to and will only enlighten the relevant parts for Zammad.

Within ``database.yml`` (``config/`` directory) you can define the allowed pool size.
By default each Zammad process takes up to ``50`` connections (``pool: 50``).

This should be fairly enough for *every* use case.
If you experience database connection timeouts or similar pool errors, this usually
indicates to other issues that are relevant to your PostgreSQL.

Below you can the locations of the relevant PostgreSQL configuration files to adjust.
Keep in mind that versions may differ from your setup - adapt where needed.

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: console

         $ /etc/postgresql/{your version}/main/postgresql.conf

   .. tab:: CentOS / OpenSUSE

      .. code-block:: console

         $ /var/lib/pgsql/data/postgresql.conf

   .. tab:: other

      Can't find your configuration files?
      You can run the following command to get the path:

      .. code-block:: console

         $ sudo -u postgres psql -c 'SHOW config_file'

Adjust ``max_connections`` (mandatory)
   Zammad uses up to 200 connections by default. Depending on your setup
   and load, you may want to change this value.

   Determine Value
      To help you determine a number, Zammad ships a function to calculate a
      suggestion. If executed, it asks you to input some integer values and
      additionally uses internally known values for the calculation. Be aware
      that the suggestion is instance specific. That means you must run the
      calculation on the system you want to adjust the ``max_connection`` value.

      Run it by using the command:

      .. code-block:: console

         $ rake zammad:db:max_connections

   Adjust Value
      Raise the maximum allowed number of connections:

      .. code-block:: console

         $ sed -i "/max_connections/c\max_connections = 2000" <postgresql-configuration-file>

      Apply changes by restarting postgresql and Zammad (in this order):

      .. code-block:: console

         $ sudo systemctl restart postgresql zammad

Adjust PostgreSQL for bigger instances (optional)
   .. warning::

      Check below settings first and ensure your system is able to provide the requirements!
      Below settings are what we found to be useful, everything else is out of scope of this documentation!

   Caching improvements:

   .. code-block:: console

      $ sed -i "/shared_buffers/c\shared_buffers = 2GB" <postgresql-configuration-file>

   .. code-block:: console

      $ sed -i "/temp_buffers/c\temp_buffers = 256MB" <postgresql-configuration-file>

   .. code-block:: console

      $ sed -i "/work_mem/c\work_mem = 10MB" <postgresql-configuration-file>

   .. code-block:: console

      $ sed -i "/max_stack_depth/c\max_stack_depth = 5MB" <postgresql-configuration-file>

   Apply changes by restarting postgresql and Zammad (in this order):

   .. code-block:: console

      $ sudo systemctl restart postgresql zammad
