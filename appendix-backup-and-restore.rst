Backup & Restore
****************

Zammad contains simple backup & restore scripts that can be executed via command line or cron job.
You can find the scripts in the "/opt/zammad/contrib/backup" directory.

Configuration
=============

* Rename "/opt/zammad/contrib/backup/config.dist" to "/opt/zammad/contrib/backup/config"
* Configure backup path in /opt/zammad/contrib/backup/config if you want. Standard backup path is "/var/tmp/zammad_backup"


Create Backup
=============

::

 cd /opt/zammad/contrib/backup
 ./zammad_backup.sh


Restore everything
==================

::

 cd /opt/zammad/contrib/backup

With menu for choosing backup date
----------------------------------

::

 ./zammad_restore.sh

With command line argument for backup date
------------------------------------------

::

 ./zammad_restore.sh 20170507121848
