Updating Zammad
***************

.. note:: Please backup your Zammad instance before update! You can learn how to back up Zammad on :doc:`/appendix/backup-and-restore`.

Source update
=============

1. Check your dependencies
--------------------------

Before proceeding, double-check that your system environment
matches :doc:`Zammad’s requirements </prerequisites/software>`.

2. Download Zammad to your system
---------------------------------

Get the latest stable release of Zammad `here <https://github.com/zammad/zammad/archive/stable.zip>`_,
or find an older version at https://ftp.zammad.com.

.. code-block:: sh

   $ cd /opt
   $ sudo wget https://ftp.zammad.com/zammad-latest.tar.gz
   $ sudo tar -C zammad -xzf zammad-latest.tar.gz
   $ sudo chown -R zammad /opt/zammad
   $ sudo su - zammad

3. Install all dependencies
---------------------------

.. code-block:: sh

   zammad@host $ cd zammad
   zammad@host $ gem install bundler

* For PostgreSQL (note, the option says "without ... mysql"):

.. code-block:: sh

   zammad@host $ bundle install --without test development mysql

* For MySQL (note, the option says "without ... postgres"):

.. code-block:: sh

   zammad@host $ bundle install --without test development postgres


4. Stop Zammad services
-----------------------

Stop the application server, websocket server and scheduler.

5. Upgrade your database
------------------------

.. code-block:: sh

   zammad@host $ export RAILS_ENV=production
   zammad@host $ export RAILS_SERVE_STATIC_FILES=true # only if you use no HTTP reverse proxy
   zammad@host $ rake db:migrate
   zammad@host $ rake assets:precompile

6. Start Zammad services
------------------------

Start the application server, websocket server and scheduler.

7. Go and login to Zammad
-------------------------


Update with RPM
===============


1. Stop Zammad
----------------

.. code-block:: sh

   $ sudo systemctl stop zammad


3. Update Zammad
----------------

.. code-block:: sh

   $ sudo yum update zammad

**Note: The package will automatically execute maintenance tasks like database changes and will restart Zammad for you.**


4. Start Zammad
----------------

.. code-block:: sh

   $ sudo systemctl start zammad


5. Go and log in to Zammad
--------------------------



Update with DEB
===============


**Note: Please backup your Zammad instance before update!**


1. Stop Zammad
----------------

.. code-block:: sh

   $ sudo systemctl stop zammad


3. Update Zammad
----------------

.. code-block:: sh

   $ apt-get update
   $ apt-get upgrade

**Note: The package will automatically execute maintenance tasks like database changes and will restart Zammad for you.**

4. Start Zammad
----------------

.. code-block:: sh

  $ sudo systemctl start zammad


5. Go and log in to Zammad
--------------------------

Updating elasticsearch
======================

If you want to upgrade your elasticsearch installation, please take a look at the `elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_
as it will have the most current information for you.

If, for whatever reason, you need to rebuild your search index after upgrading, use::

   $ zammad run rake searchindex:rebuild
   
.. warning:: This step may fail if Zammad is under heavy load:
   Elasticsearch locks the indices from deletion if you're pumping in new data, like receiving a new ticket.
   (This only applies to single-node deployments, not clusters.)
   
   If it does, try killing Zammad first::
   
      $ systemctl stop zammad
      $ zammad run rake searchindex:rebuild
      $ systemctl start zammad
