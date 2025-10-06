Backup & Restore (Docker)
=========================

.. toctree::
   :hidden:

   docker-file-handling

This section shows some basics about the backup and restore process for a Docker
Compose based deployment of Zammad.

If you are familiar with volume based backup and restore procedures in Docker,
and perhaps already use a different method or tool, then you can keep using it.
A backup would typically mean shutting down the stack to ensure all in-memory
files get written to disk, then backing up the volume contents, and then starting
the stack again. When using such a method, you can consider
using the :ref:`disable-backup-service scenario <additional-scenarios>` so that
the built-in backup and restore mechanism of Zammad is not activated.

The rest of this page describes the built-in backup and restore mechanism of
Zammad's Docker Compose stack.

If you're familiar with Docker, the sections below include the
information you'll need. The
:doc:`/appendix/backup-and-restore/docker-file-handling` page covers some
examples about how to handle the backup files and to copy it into a Docker
volume to restore it.

Backup
------

By default, a backup is created at each start of the stack as well as at 3
o'clock each night. The backup is stored in the volume of the
**zammad-backup** container under ``/var/tmp/zammad``.

Restore
-------

#. Start the new stack at least once so a Zammad database is available.
#. Stop the stack.
#. In case you restore to a production stack with activated file system
   storage, you should purge the content of the directory
   ``/opt/zammad/storage/`` inside the volume. The restore process only
   adds/overwrites files there, no cleanup will take place.
#. Copy or move the backup files to ``/var/tmp/zammad/restore/`` inside the
   volume of the **zammad-backup** container. Be aware that the restore process
   always uses the latest backup according to the timestamp of the file name.
   Only backups from package and Docker installations are supported by this
   built-in backup method. Don't provide the ``latest_zammad_*.gz`` files
   because they link to an unknown location for the restore process.
#. Start the stack. The restore process is triggered if the ``restore``
   directory is detected and the backup files are in place.
#. After the restore process has finished, the ``restore`` directory got renamed.
   You can safely delete it now.
