Get the latest stable release of Zammad `here <https://ftp.zammad.com/zammad-latest.tar.gz>`_.
This file will be updated whenever new bug-fixes are applied, so you can update from this URL regularly.

.. code-block:: sh

   $ cd /opt
   $ wget https://github.com/zammad/zammad/archive/stable.tar.gz
   $ tar -xzf stable.tar.gz --strip-components 1 -C zammad
   $ chown -R zammad:zammad zammad/
   $ rm -f stable.tar.gz
