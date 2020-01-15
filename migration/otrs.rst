from OTRS
*********

Install plugins on OTRS
=======================

.. note:: Currently only passwords of OTRS >= 3.3 can be reused in Zammad! Passwords that were stored in another format than the default SHA2 are not possible to use. Users then have to use the password reset procedure.

Install Znuny4OTRS-Repo
-----------------------

This is a dependency of the OTRS migration plugin

* On OTRS 6:

  *  https://addons.znuny.com/api/addon_repos/public/1029/latest

* On OTRS 5:

  *  https://addons.znuny.com/api/addon_repos/public/615/latest

* On OTRS 4:

  *  https://addons.znuny.com/api/addon_repos/public/309/latest

* On OTRS 3:

  *  https://addons.znuny.com/api/addon_repos/public/142/latest


Install OTRS migration plugin
-----------------------------

* OTRS 6:

  * https://addons.znuny.com/api/addon_repos/public/1085/latest

* OTRS 5:

  * https://addons.znuny.com/api/addon_repos/public/617/latest

* OTRS 4:

  * https://addons.znuny.com/api/addon_repos/public/383/latest

* OTRS 3.1 - 3.3:

  * https://addons.znuny.com/api/addon_repos/public/287/latest


Import via Browser
==================

.. note:: If your OTRS installation is rather huge, you might want to consider using the command line version of this feature.

After installing Zammad, open http://localhost:3000 with your browser and follow the installation wizard.
From there you're able to start the migration from OTRS.

See the Video at `this site <https://days.zammad.org/features/migrator>`_ .


Import via command line
=======================

If you miss this at the beginning or you want to re-import again you have to use the command line at the moment.

Stop all Zammad processes and switch Zammad to import mode (no events are fired - e. g. notifications, sending emails, ...)


If you installed the Zammad DEB or RPM package
----------------------------------------------

::

 zammad run rails c


If you installed from source
----------------------------

::

 su zammad
 cd /opt/zammad
 rails c


Extending import time for big installations (optional)
------------------------------------------------------

Optional, if you're having a bigger installation or running in timeouts like:
``Delayed::Worker.max_run_time is only 14400 seconds (4 hours)`` you need to do the following:

For importing via console
^^^^^^^^^^^^^^^^^^^^^^^^^

* open the file ``config/initializers/delayed_jobs_settings_reset.rb`` and add the following at the end of it:
  ::

    Delayed::Worker.max_run_time = 7.days

* Restart the Zammad-Service (``systemctl restart zammad``)

For importing via browser (not recommended on big installations)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run below in a Zammad console and ensure to not close it during import:
  ::

    Delayed::Worker.max_run_time = 7.days


.. note:: The above setting is only valid for the lifetime of the Zammad rails console.
  If you close the console, the change is reset to the default value.

Enter the following commands in the rails console
-------------------------------------------------

::

 Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 Setting.set('import_otrs_endpoint_key', 'xxx')
 Setting.set('import_mode', true)
 Import::OTRS.start


After the import is done switch Zammad back to non-import mode and mark the system initialization as done.

::

 Setting.set('import_mode', false)
 Setting.set('system_init_done', true)

Start all Zammad processes again. Done.

Importing a diff
================

.. note:: This is only possible after finishing an earlier OTRS import **successful**.

In some cases it might be desirable to update the already imported data from OTRS. This is possible with the following commands.

Enter the following commands in the rails console
-------------------------------------------------

::

 Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 Setting.set('import_otrs_endpoint_key', 'xxx')
 Setting.set('import_mode', true)
 Setting.set('system_init_done', false)
 Import::OTRS.diff_worker

After the import is done switch Zammad back to non-import mode and mark the system initialization as done.

::

 Setting.set('import_mode', false)
 Setting.set('system_init_done', true)

Start all Zammad processes again. Done.


Restarting from scratch
=======================

First make sure all Zammad processes are stopped. After that reset your database.

If you installed the Zammad DEB or RPM package
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
