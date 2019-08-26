Updating Zammad
***************

.. Note:: Please backup your Zammad instance before update! You can learn how to back up Zammad on :ref:`backup-and-restore`.

Source update
=============

1. Download Zammad to your system
---------------------------------

You can directly download Zammad from https://ftp.zammad.com/ or use the direct URL to get the latest stable release via https://ftp.zammad.com/zammad-latest.tar.gz

::

 root@shell> cd /opt
 root@shell> wget https://ftp.zammad.com/zammad-latest.tar.gz
 root@shell> tar -C zammad -xzf zammad-latest.tar.gz
 root@shell> chown -R zammad /opt/zammad
 root@shell> su - zammad

2. Install all dependencies
---------------------------

::

 zammad@shell> cd zammad
 zammad@shell> gem install bundler

* For PostgreSQL (note, the option says "without ... mysql")::
  
   zammad@shell> bundle install --without test development mysql

* For MySQL (note, the option says "without ... postgres")::
  
   zammad@shell> bundle install --without test development postgres


3. Stop Zammad services
-----------------------

Stop the application server, websocket server and scheduler.

4. Upgrade your database
------------------------

::

 zammad@shell> export RAILS_ENV=production
 zammad@shell> export RAILS_SERVE_STATIC_FILES=true # only if you use no HTTP reverse proxy
 zammad@shell> rake db:migrate
 zammad@shell> rake assets:precompile

5. Start Zammad services
------------------------

Start the application server, websocket server and scheduler.

6. Go and login to Zammad
-------------------------


Update with RPM
===============


1. Stop Zammad
----------------

::

  shell> sudo systemctl stop zammad


3. Update Zammad
----------------

::

 shell> sudo yum update zammad

**Note: The package will automatically execute maintenance tasks like database changes and will restart Zammad for you.**


4. Start Zammad
----------------

::

  shell> sudo systemctl start zammad


5. Go and log in to Zammad
--------------------------



Update with DEB
===============


**Note: Please backup your Zammad instance before update!**


1. Stop Zammad
----------------

::

  shell> sudo systemctl stop zammad


3. Update Zammad
----------------

::

  shell> apt-get update
  shell> apt-get upgrade

**Note: The package will automatically execute maintenance tasks like database changes and will restart Zammad for you.**

4. Start Zammad
----------------

::

  shell> sudo systemctl start zammad


5. Go and log in to Zammad
--------------------------

Updating elasticsearch
======================

If you want to upgrade your elasticsearch installation, please take a look at the `elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ 
as it will have the most current information for you.

.. Note:: If your Zammad-Installation is quite busy or your ``zammad run rake searchindex:rebuild`` fails, you might want to stop the Zammad-Service: ``systemctl stop zammad``.
  
  The Reason behind this is that elasticsearch locks the indexes from deletion if you're pumbing in new data (like receiving a new ticket).
  This only affects elasticsearch single nodes and should not affect clusters.
