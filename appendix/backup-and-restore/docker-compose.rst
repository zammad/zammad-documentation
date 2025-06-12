Backup & Restore (Docker)
=========================

This guide shows a basic backup and restore process for a docker compose
based deployment of Zammad. If you already use a different method or tool, it is
fine to stick with it as long as it works. In such a case, consider using the
:ref:`disable-backup-service scenario <additional-scenarios>`.

Important Information
---------------------

If you migrate from another installation method or host/stack, make sure to
start the stack once without following the restore procedure to create a new
database. This is required to execute the restore process.

Be aware that the restore process always uses the latest backup according
to the timestamp in the file name.

Quick Start
-----------

Backup
^^^^^^

By default, a backup is created at each start of the stack as well as at 3
o'clock each night. The backup is stored in the volume of the
**zammad-backup** container under ``/var/tmp/zammad``.

Restore
^^^^^^^

- Start the new stack at least once so the database is set up.
- Copy or move the backup files to ``/var/tmp/zammad/restore/`` in the volume of
  the **zammad-backup** container. Read on in the next section for some examples
  how to do that.
- Stop the stack.
- Start the stack. The restore process is triggered if the ``restore``
  directory is detected and the backup files are in place.
- After the restore process has finished, the ``restore`` directory got renamed.
  You can safely delete it now.

Backup Files Handling
---------------------

If you're not sure how to create the ``restore`` directory in the docker volume
and how to copy the backup files into it, you can find some examples below.

Copy Files Inside One Volume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Requires:** console access to the zammad-backup container.

If you want to restore a backup from the same stack, you just have to create
the directory and copy/move the files into it. The following example starts the
**zammad-backup** container and drops the unused one, gets access to the console
and creates the directory and copies *all* .gz files from the backup directory
into it.

.. code-block:: sh

   docker compose run --rm zammad-backup bash -c "mkdir /var/tmp/zammad/restore; cp /var/tmp/zammad/*.gz /var/tmp/zammad/restore -v"

Now stop the stack and restart it to execute the restore process.

Copy Files from Host Into the Volume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Requires:** console access to the host system and the zammad-backup container.

In case you have to fetch your backup from another docker deployment, the
following command might be helpful:

.. code-block::

   docker compose cp zammad-backup:/var/tmp/zammad/ /path/to/your/host/directory/restore/

On the host system, place your files in a folder called ``restore``. Copy this
restore directory via ``docker compose cp`` into the volume:

.. code-block:: sh

   docker compose cp /path/to/your/files/restore/ zammad-backup:/var/tmp/zammad/

Now stop the stack and restart it to execute the restore process.

Use a Web GUI to Upload Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Requires:** console access to the host system or Portainer access with the
permission to deploy a container.

This can be useful if you use Portainer to deploy Zammad and have limited access
to the host system.

Our example uses the tool `filebrowser <https://filebrowser.org/>`_, but any
similar tool should work too. If you'd like to use such a tool permanently, make
sure to provide additional volumes for persistence (e.g. for their database,
etc.).

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
#. Log in with the credentials ``admin`` / ``admin``.
#. You should now see at least 2 .gz files including a timestamp.
#. Create a **New folder** by using the button on the left side. Name it
   ``restore``.
#. Enter this folder and upload your backup files (on the top right corner with
   the up arrow).

Now stop the stack and restart it to execute the restore process. After that,
you can safely delete the renamed folder and stop the filebrowser.
