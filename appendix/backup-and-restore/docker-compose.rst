Backup & Restore (Docker)
=========================

.. toctree::
   :hidden:

   docker-file-handling

This section shows some basics about the backup and restore process for a docker
compose based deployment of Zammad. If you already use a different method or
tool, it is fine to stick with it as long as it works. In such a case, consider
using the :ref:`disable-backup-service scenario <additional-scenarios>` so that
the built-in backup and restore mechanism of Zammad is not used. This page
describes the built-in backup and restore mechanism of Zammad's docker compose
stack.

If you're familiar with docker, the Quick Start section below includes the
information you'll need. The
:doc:`/appendix/backup-and-restore/docker-file-handling` page covers some
examples about how to handle the backup files and to copy it into a docker
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
#. Copy or move the backup files to ``/var/tmp/zammad/restore/`` inside the
   volume of the **zammad-backup** container. Be aware that the restore process
   always uses the latest backup according to the timestamp of the file name.
   Only backups from package and docker installations are supported by this
   built-in backup method. Don't provide the ``latest_zammad_*.gz`` files
   because they link to an unknown location for the restore process.
#. Start the stack. The restore process is triggered if the ``restore``
   directory is detected and the backup files are in place.
#. After the restore process has finished, the ``restore`` directory got renamed.
   You can safely delete it now.
