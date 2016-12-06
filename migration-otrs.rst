from OTRS
*********

Install plugins on OTRS
=======================

**Note: Currently only passwords of OTRS >= 3.3 can be reused in Zammad! Passwords that were stored in another format than the default SHA2 are not possible to use. Users then have to use the password reset procedure.**

Install Znuny4OTRS-Repo
-----------------------

This is a dependency for the OTRS migration plugin

* On OTRS 5:

  *  http://portal.znuny.com/api/addon_repos/public/615/latest

* On OTRS 4:

  *  http://portal.znuny.com/api/addon_repos/public/309/latest


Install OTRS migration plugin
-----------------------------

* OTRS 5:

  * https://portal.znuny.com/api/addon_repos/public/617/latest

* OTRS 4:

  * https://portal.znuny.com/api/addon_repos/public/383/latest

* OTRS 3.1 - 3.3:

  * https://portal.znuny.com/api/addon_repos/public/287/latest


Import via Browser
==================

After installing Zammad, open http://localhost:3000 with your browser and follow the installation wizard.
From there you're able to start migration from OTRS.

See the Video @ http://days.zammad.org/features/migrator


Import via command line
=======================

If you miss this at the beginning or you want to re-import again you have to use the command line at the moment.

Stop all Zammad processes and switch Zammad to import mode (no events are fired - e. g. notifications, sending emails, ...)


If you installed the zammad DEB or RPM package
----------------------------------------------

::

 zammad run rails c


If you installed from source
----------------------------

::

 su zammad
 cd /opt/zammad
 rails c


Enter the following commands in the rails console
------------------------------------------------

::

 Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 Setting.set('import_otrs_endpoint_key', 'xxx')
 Setting.set('import_mode', true)
 Import::OTRS.start


After the import is done switch Zammad back to non import mode and mark the system initialization as done

::

 Setting.set('import_mode', false)
 Setting.set('system_init_done', true)

Start all Zammad processes again. Done.

Importing a diff
================

In some cases it might be desirable to update the already imported data from OTRS. This is possible with the following commands.

Enter the following commands in the rails console
------------------------------------------------

::

 Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 Setting.set('import_otrs_endpoint_key', 'xxx')
 Setting.set('import_mode', true)
 Setting.set('system_init_done', false)
 Import::OTRS.diff_worker

After the import is done switch Zammad back to non import mode and mark the system initialization as done

::

 Setting.set('import_mode', false)
 Setting.set('system_init_done', true)

Start all Zammad processes again. Done.


Restarting from scratch
================

First make sure all Zammad processes are stopped. After that reset your database.

If you installed the zammad DEB or RPM package
----------------------------------------------

::

 zammad run rake db:drop
 zammad run rake db:create
 zammad run rake db:migrate
 zammad run rake db:seed


If you installed from source
----------------------------

::

 rake db:drop
 rake db:create
 rake db:migrate
 rake db:seed

After that your DB is reset and you can start the import right over.
