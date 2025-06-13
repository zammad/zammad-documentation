Backup & Restore (Docker)
=========================

This section shows some basics about the backup and restore process for a docker
compose based deployment of Zammad. If you already use a different method or
tool, it is fine to stick with it as long as it works. In such a case, consider
using the :ref:`disable-backup-service scenario <additional-scenarios>`.

If you're familiar with docker, the Quick Start section below includes the
information you'll need. The :ref:`file-handling` section covers some examples
about how to handle the backup files and to copy it into a docker volume to
restore it.

Quick Start
-----------

Backup
^^^^^^

By default, a backup is created at each start of the stack as well as at 3
o'clock each night. The backup is stored in the volume of the
**zammad-backup** container under ``/var/tmp/zammad``.

Restore
^^^^^^^

.. warning::
   Be aware that the restore process always uses the latest backup according
   to the timestamp of the file name.

#. Start the new stack at least once so a Zammad database is available.
#. Copy or move the backup files to ``/var/tmp/zammad/restore/`` inside the
   volume of the **zammad-backup** container.
#. Stop the stack.
#. Start the stack. The restore process is triggered if the ``restore``
   directory is detected and the backup files are in place.
#. After the restore process has finished, the ``restore`` directory got renamed.
   You can safely delete it now.

.. _file-handling:

File Handling
-------------

If you're not sure how to handle the backup files and how to create the
``restore`` directory in the docker volume, you can find some examples below.

Restore Inside the Same Stack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Requires:** console access to the zammad-backup container.

If you want to restore a backup from the same stack, you just have to create
the directory and copy/move the files into it. The following example starts the
**zammad-backup** container and drops the unused one, gets access to the console
and creates the directory and copies *all* .gz files from the backup directory
into it.

.. code-block:: sh

   docker compose run --rm zammad-backup bash -c "mkdir /var/tmp/zammad/restore; cp /var/tmp/zammad/*.gz /var/tmp/zammad/restore -v"

Now stop the stack and restart it to execute the restore process.

Restore from Another Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Requires:** console access to the host system and the zammad-backup container.

To **obtain** your backup files from another docker compose deployment, one way
is to copy it to the host system with ``docker compose cp``:

.. code-block::

   docker compose cp zammad-backup:/var/tmp/zammad/ /path/to/your/host/directory/

In case you are searching for your backup files from a package installation,
have a look at the :doc:`/appendix/backup-and-restore/index` section.

To **restore** the backup, place your files in a folder called ``restore``
on the host system. Copy this restore directory via ``docker compose cp`` into
the volume:

.. code-block:: sh

   docker compose cp /path/to/your/files/restore/ zammad-backup:/var/tmp/zammad/

Now stop the stack and restart it to execute the restore process.

Use a Web GUI
^^^^^^^^^^^^^

**Requires:** console access to the host system or Portainer access with the
permission to deploy a container.

This can be useful if you use Portainer to deploy Zammad and have limited access
to the host system.

Our example uses the tool `filebrowser <https://filebrowser.org/>`_, but any
similar tool should work too. If you'd like to use such a tool permanently, make
sure to provide additional volumes for persistence (e.g. for their database).

.. hint:: The steps below cover the restore process by uploading files. To get
   your backup files in the same way from another stack, you can follow steps
   1-4 below and simply map the **zammad-backup** volume of your *old* stack.
   Then you can download the files, stop and remove the filebrowser container
   and redeploy it, following the steps below.

#. Deploy filebrowser

   .. tabs::

      .. tab:: Via console

         Deploy the container and provide the volume of **zammad-backup** and a
         port under which you want to access the web UI:

         .. code-block:: sh

            docker run -v zammad-docker-compose_zammad-backup:/srv -p 8089:80 filebrowser/filebrowser

      .. tab:: Via Portainer

         In your Portainer web UI, go to **Containers** in the left menu and
         click the **Add container** button.

         Add the following information:

         - Name: enter a name which is not already in use.
         - Image: ``filebrowser/filebrowser``
         - Map additional port: choose a port and map it to port ``80`` in the
           container.
         - Advanced container settings:

           - Switch to **Volumes** and click the **map additional volume** button.
           - Enter ``/srv`` in the container section and select the volume
             containing ``zammad-backup``

         - Finally, click on **Deploy the container**.

#. After the container is started, go to the web interface by using the IP
   address and the port you defined.
#. Log in with the default credentials ``admin`` / ``admin``.
#. You should now see at least 2 .gz files including a timestamp.
#. Create a **New folder** by using the button on the left side. Name it
   ``restore``.
#. Enter this folder and upload your backup files (on the top right corner with
   the up arrow).

Now stop the stack and restart it to execute the restore process. After that,
you can safely delete the renamed folder and stop the filebrowser.
