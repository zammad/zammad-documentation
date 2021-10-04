Get the latest stable release of Zammad `here <https://github.com/zammad/zammad/archive/stable.tar.gz>`_,
or find the initial version at https://ftp.zammad.com.

.. code-block:: sh

   $ cd /opt
   $ wget https://github.com/zammad/zammad/archive/stable.tar.gz
   $ tar -xzf stable.tar.gz --strip-components 1 -C zammad
   $ chown -R zammad:zammad zammad/
   $ rm -f stable.tar.gz
