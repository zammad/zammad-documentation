Export Zammad on Univention for migration
*****************************************

This page will guide you through the process on how to export your instance
data on Univention systems. The provided backup suits all supported platforms
for a regular backup restore. If you require help, please contact Zammad-Sales
for a discounted migration workshop.

The provided method is provided as is and does not receive any community
support.

.. warning::

   Our export has some limitations you have to be aware of:

      * Only one running Zammad instance per host is supported.
         * If you might have several instances running on the same host,
           stop all instances except the one you're exporting.
      * | Zammad for UCS version ``5.1.1-16`` only is supported.
        | **Using older versions will fail, the backup method
          *is not* supported**!
      * The export script expects ``root`` permissions on the host in question.
      * The script ensures there's no delayed jobs left and stops parts of the
        stack. *Expect a downtime*.
      * Due to limitations on Univention, the update scripts for 5.1 are
        required to download an extra script from ``vps1337.dc.zammad.com``.

        For this reason, please ensure that above host can be connected via
        ``https`` during upgrade time.

.. hint::

   | **About our setup:**
   | We've verified our scripts function on both, Univention 4.4 and Univention
     5.0. Both test scenarios consisted on a clean ``5.1.1-16`` installation²
     and one upgrade installation from ``4.1.0-52``.
   | ² Clean installations are not available for normal UCS users as the App
     has been set to EOL.

Upgrade your Zammad app
-----------------------

Before you can run the export, please ensure to upgrade your Zammad installation
to ``5.1.1-16``. The update should run as smooth as always. 🤓

Before the actual upgrade, our pre-installation script will download an extra
export script that is required for the actual migration at an later point.
If the can't retrieve the script successful, the upgrade process will abort.

Export your Zammad data for the migration
-----------------------------------------

.. warning:: **Important**

  Ensure that your app has version ``5.1.1-16`` - if that's not the case,
  upgrade your app.

During the upgrade we've placed an export script on your system for you.
This script is located on the host that's running the Zammad app.

  .. danger:: **Downtime ahead**

    Make sure to run the migration during a planned maintenance window.

  .. tip::

    To reduce maintenance you may wanna install Zammad before hand. The easiest
    installation type is the :doc:`package installation </install/package>`.

If you're ready to go, login as to your Univention hosts SSH console as
administrative user (``administrator`` on default systems).

After logging in, ensure to have an evalated session by running ``sudo -s``.
The export script is located in ``/var/lib/univention-appcenter/apps/zammad/``.

Executing ``/var/lib/univention-appcenter/apps/zammad/ucs-export.sh`` will start
the backup process. The process will ensure that there's no delayed jobs waiting
for completion (mandatory) and also enable maintenance mode for you.

The backup is being created without any further warnings - this process stops
Zammad containers and does not start them again.

  .. note:: **Sample output**

    To give you an idea what a successful export looks like, you can find a
    console output below. IDs and names may differ.

    .. code-block::

      # ================================= #
      # Start of Zammad UCS export ...    #
      # --------------------------------- #
      # ... Ensuring permissions ...      #
      # ... Ensuring limits ...           #
      # ... Getting container IDs         #
      # ... Enabling maintenance mode     #
      # ... Ensuring no delayed jobs      #
      # ... Checking delayed jobs (0)     #
      # Listing 'docker ps' before ...    #
      CONTAINER ID        IMAGE                                                        COMMAND                  CREATED             STATUS              PORTS                     NAMES
      d8d9ff288b95        zammad/zammad-docker-compose:zammad-5.1.1-16                 "/docker-entrypoint.…"   11 minutes ago      Up 11 minutes       0.0.0.0:40001->8080/tcp   zammad_zammad-nginx_1
      99a9600ef2e5        zammad/zammad-docker-compose:zammad-postgresql-5.1.1-16      "/usr/local/bin/back…"   11 minutes ago      Up 11 minutes       5432/tcp                  zammad_zammad-backup_1
      b5a6bd5202c8        zammad/zammad-docker-compose:zammad-5.1.1-16                 "/docker-entrypoint.…"   11 minutes ago      Up 11 minutes                                 zammad_zammad-scheduler_1
      98274f29cfbc        zammad/zammad-docker-compose:zammad-5.1.1-16                 "/docker-entrypoint.…"   11 minutes ago      Up 11 minutes                                 zammad_zammad-websocket_1
      91427e08cc4f        zammad/zammad-docker-compose:zammad-5.1.1-16                 "/docker-entrypoint.…"   11 minutes ago      Up 11 minutes                                 zammad_zammad-railsserver_1
      10dc586b3253        redis:6.2.5-alpine                                           "docker-entrypoint.s…"   11 minutes ago      Up 11 minutes       6379/tcp                  zammad_zammad-redis_1
      0df28c6f2575        memcached:1.6.10-alpine                                      "docker-entrypoint.s…"   11 minutes ago      Up 11 minutes       11211/tcp                 zammad_zammad-memcached_1
      b1502ebdd1fe        zammad/zammad-docker-compose:zammad-postgresql-5.1.1-16      "docker-entrypoint.s…"   11 minutes ago      Up 11 minutes       5432/tcp                  zammad_zammad-postgresql_1
      b94ef91f73a6        zammad/zammad-docker-compose:zammad-elasticsearch-5.1.1-16   "/bin/tini -- /usr/l…"   11 minutes ago      Up 11 minutes       9200/tcp, 9300/tcp        zammad_zammad-elasticsearch_1
      # ... Stopping Zammad containers    #
      d8d9ff288b95
      b5a6bd5202c8
      98274f29cfbc
      b94ef91f73a6
      0df28c6f2575
      # Listing 'docker ps' after ...     #
      CONTAINER ID        IMAGE                                                     COMMAND                  CREATED             STATUS              PORTS               NAMES
      99a9600ef2e5        zammad/zammad-docker-compose:zammad-postgresql-5.1.1-16   "/usr/local/bin/back…"   11 minutes ago      Up 11 minutes       5432/tcp            zammad_zammad-backup_1
      91427e08cc4f        zammad/zammad-docker-compose:zammad-5.1.1-16              "/docker-entrypoint.…"   11 minutes ago      Up 11 minutes                           zammad_zammad-railsserver_1
      10dc586b3253        redis:6.2.5-alpine                                        "docker-entrypoint.s…"   11 minutes ago      Up 11 minutes       6379/tcp            zammad_zammad-redis_1
      b1502ebdd1fe        zammad/zammad-docker-compose:zammad-postgresql-5.1.1-16   "docker-entrypoint.s…"   11 minutes ago      Up 11 minutes       5432/tcp            zammad_zammad-postgresql_1
      # ... Creating backup ...           #
      creating file backup...
       ... only with productive data (attachments)
       ... WARNING: You don't seem to have any attachments in the file system!
       ... Please consult https://docs.zammad.org/en/latest/appendix/backup-and-restore/troubleshooting.html
       ... Creating empty storage directory so the backup can continue ...
      creating postgresql backup...
      Ensuring dump permissions ...
      # ... Created backup                #
      # ... Double check above output !   #
      # --------------------------------- #
      # Please disable Zammad UCS App ... #
      # You're now ready to import!       #
      # ================================= #

      Tip: Remove Zammad UCS app *after* successfully importing ╰（‵□′）╯

    You can safely ignore this warning:

    .. code-block::

      ... WARNING: You don't seem to have any attachments in the file system!
      ... Please consult https://docs.zammad.org/en/latest/appendix/backup-and-restore/troubleshooting.html
      ... Creating empty storage directory so the backup can continue ...

After exporting
---------------

Please ensure to check the provided console output for errors.
If there were no errors, please continue with the
:doc:`restoration process </appendix/backup-and-restore/restore>`.

You can find the relevant backup files in
``/var/lib/univention-appcenter/apps/zammad/data/backup/``.

If the migration was a success, stop and remove the Univention app.

.. hint::

  Please note that removing the app does also remove the LDAP users created
  during the installation. If you use our default LDAP mapping you may have to
  adjust it before hand!
