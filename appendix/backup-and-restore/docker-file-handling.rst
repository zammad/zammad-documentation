File Handling Examples
======================

If you're not sure how to handle the backup files and how to create the
``restore`` directory in the docker volume, you can find some examples below.

Restore Inside the Same Stack
-----------------------------

**Requires:** console access to the zammad-backup container.

If you want to restore a backup from the same stack, you just have to create
the directory and copy/move the files into it. The following example starts the
**zammad-backup** container and copies *all* .gz files from the backup directory
into the restore directory:

.. code-block:: sh

   docker compose run --rm zammad-backup bash -c "mkdir /var/tmp/zammad/restore; cp /var/tmp/zammad/*.gz /var/tmp/zammad/restore -v"

Now start the stack to execute the restore process.

Restore from Another Installation
---------------------------------

**Requires:** console access to the host system and the zammad-backup container.

To **obtain** your backup files from another docker compose deployment, one way
is to copy it to the host system with ``docker compose cp``:

.. code-block::

   docker compose cp zammad-backup:/var/tmp/zammad/ /path/to/your/host/directory/

In case you are searching for your backup files from a package installation,
have a look at the :doc:`/appendix/backup-and-restore/index` section. You don't
need a full dump for restoring your backup.

To **restore** the backup, place your files in a folder called ``restore``
on the host system. This folder is mounted temporarily to ``/restore_tmp`` in
the backup container. The directory then gets copied to the actual directory:

.. code-block:: sh

   docker compose run --rm -v /path/to/your/host/directory:/restore_tmp zammad-backup bash -c "cp -rv /restore_tmp /var/tmp/zammad/"

Now start the stack to execute the restore process.

Use a Web GUI
-------------

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

Now start the stack to execute the restore process. After that, you can safely
delete the renamed folder and stop the filebrowser.
