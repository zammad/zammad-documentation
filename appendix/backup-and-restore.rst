Backup and Restore
******************

Zammad contains simple backup & restore scripts that can be executed via command line or cron job.
You can find the scripts in the ``/opt/zammad/contrib/backup`` directory.

.. warning:: You'll need to rename the config file for the backup before you can use this script!


Configuration
=============

* Rename ``/opt/zammad/contrib/backup/config.dist`` to ``/opt/zammad/contrib/backup/config``
* Configure backup path in ``/opt/zammad/contrib/backup/config`` if you want. The default backup path is ``/var/tmp/zammad_backup`` (needs to be created!)
* If needed, you can also adjust the variable ``HOLD_DAYS`` to any value you need. Default value here is 10 backups before the oldest backup is deleted.

.. note:: Please note that the Backup script always creates a Full-Dump of ``/opt/zammad`` and a Full-Dump of your database. If your Zammad installation
   is rather big, you might need to ensure you have enough space.


Create Backup
=============

Creating a Backup is done very easy, you can just call the following to backup your Zammad-Instance.
You can also run this as a cronjob to have a regular backup:

.. code-block:: sh

   $ cd /opt/zammad/contrib/backup
   $ ./zammad_backup.sh

.. note:: Please note that you should run the cronjob as User ``zammad`` (ensure this user can write to the backup-directory). If you're using the root user, you might want to consider the following issues `"Permission issue for Backup" <https://github.com/zammad/zammad/issues/2508>`_ and `"Backup script asks for password" <https://github.com/zammad/zammad/issues/2705>`_.

.. warning:: If you plan on migrating your Zammad-Installation to another system, ensure to stop Zammad before creating a Backup. Other wise, data might change!
   You can do this with:

   .. code-block:: sh

      $ systemctl disable zammad && systemctl stop zammad


Migrating from another Zammad-Host
==================================

Migration between different Zammad installations is very easy.
Before you migrate, please ensure the following requirenments are met:

* The Zammad-Version on the destination system has to be the same or newer
* You can't mix database types (postgresql or MySQL), as this needs conversion of your dump (which the script does not perform)
   * We can offer you Dump-Migrations from MySQL to postgresql and postgresql to MySQL if need to change the 
     database for whatever reason, as a commercial service.
* Ensure you have enough free space on your drive (at least double as the size of your Dump!)
* **If not source code installation:** You need a fresh Zammad installation

If above requirenments are met, you can continue with restoring.

.. hint:: Source code installations have to supply the old ruby version that has been used earlier.
   This is because the restore script partly uses Zammad commands which will fail if you don't! 

   You can find a version list on the :doc:`/prerequisites/software` page.

Restore everything
==================

.. code-block:: sh

   # Change into the folder of Zammads backup-script:
   $ cd /opt/zammad/contrib/backup


With menu for choosing backup date
----------------------------------

.. code-block:: sh

   # When called without arguments, Zammad will show you a list of available backups.
   $ ./zammad_restore.sh


With command line argument for backup date
------------------------------------------

.. warning:: Only use the following option if you know what you're doing! The following command will overwrite existing data without further prompts!

.. code-block:: sh

   # When called with a timestamp argument (matching the backup's filename),
   # Zammad will proceed immediately to restoring the specified backup.
   $ ./zammad_restore.sh 20170507121848


What to do after restoration has been completed
===============================================

When migrated from a self hosted Zammad system
----------------------------------------------

.. note:: This step is only needed, if one of the following points is met:

   * The source and destination Zammad-Version are not the same
   * The Zammad-installation is not a source code installation
   * The Zammad-Backup is not an Export from Hosted-Setup

   If no points affect you, just continue with `the things you need to do after migration on every system <#things-you-need-to-do-after-migration-on-every-system>`_.

If your versions differ, it might happen, that your Zammad-Service will not start cleanly.
You can update your installation

If you receive the following, you can workaround your problem with reinstalling Zammad (example on Debian, other Operating systems might differ) ::

   root@zammad:/# apt-get update && apt install zammad
   Reading package lists... Done
   Building dependency tree
   Reading state information... Done
   zammad is already the newest version (x.x.x-xxxxxx.xxxxxx.stretch).
   0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

The following will uninstall and install Zammad without resolving dependencies:

**Debian, Ubuntu**

.. code-block:: sh

   $ dpkg -r --force-depends zammad
   $ apt install zammad

**openSuSe**

.. code-block:: sh

   $ zypper remove -R zammad
   $ zypper install zammad


Things you need to do after migration on every system
-----------------------------------------------------

.. note:: This does not apply to Docker images, as the following settings should be applied upon every start.

.. warning:: For Zammad-Versions **2.9 and earlier**, please run a change owner on your Zammad folder.
   Default-Installations should be fine with ``chown -R zammad:zammad /opt/zammad/`` (Source code installations might differ).
   Please restart Zammad after the change-owner command ``systemctl restart zammad``.

Before you can use Zammad and all it's features, you'll need to ensure your Searchindex is up and running.
If you didn't install elasticsearch yet, now's a good time. If you already did, ensure to configure the ES-URL (if migrated) and also run a reindex.

You can find further information on how to do that on the following page: :doc:`/install/elasticsearch`.
