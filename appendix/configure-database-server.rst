Configure Database server
*************************

.. note:: 

   Parts of this page also applies to both supported database servers. 
   We can't provide a complete how to and will only enlighten the relevant parts for Zammad.

Within ``database.yml`` (``config/`` directory) you can define the allowed pool size. 
By default each Zammad process takes up to ``50`` connections (``pool: 50``).

This should be fairly enough for *every* use case. 
If you experience database connection timeouts or similar pool errors, this usually 
indicates to other issues that are relevant to your PostgreSQL.

.. note::
   
   Below only affects PostgreSQL-Servers. All relevant steps for MySQL are mentioned on 
   :doc:`/prerequisites/software` because they're relevant *before* installation.

Below you can the locations of the relevant PostgreSQL configuration files to adjust. 
Keep in mind that versions may differ from your setup - adapt where needed.

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block::

         /etc/postgresql/(10|11|12)/main/postgresql.conf

   .. tab:: CentOS / OpenSUSE

      .. code-block::

         /var/lib/pgsql/data/postgresql.conf

   .. tab:: other

      Can't find your configuration files? 
      You can run the following command to get the path:

      .. code-block:: sh

         $ sudo -u postgres psql -c 'SHOW config_file'

Adjust ``max_connections`` (mandatory)
   Zammad will take up to 200 connections by default, with below command you can raise this limit fairly high.

   .. code-block:: sh

      # Raise maximum allowed number of connections
      $ sed -i "/max_connections/c\max_connections = 2000" <postgresql-configuration-file>

      # Apply changes by restarting postgresql and Zammad (in this order)
      $ systemctl restart postgresql zammad

Adjust PostgreSQL for bigger instances (optional)
   .. warning:: 

      Check below settings first and ensure your system is able to provide the requirements! 
      Below settings are what we found to be useful, everything else is out of scope of this documentation!

   .. code-block:: sh

      # Caching improvements
      $ sed -i "/shared_buffers/c\shared_buffers = 2GB" <postgresql-configuration-file>
      $ sed -i "/temp_buffers/c\temp_buffers = 256MB" <postgresql-configuration-file>
      $ sed -i "/work_mem/c\work_mem = 10MB" <postgresql-configuration-file>
      $ sed -i "/max_stack_depth/c\max_stack_depth = 5MB" <postgresql-configuration-file>

      # Apply changes by restarting postgresql and Zammad (in this order)
      $ systemctl restart postgresql zammad
